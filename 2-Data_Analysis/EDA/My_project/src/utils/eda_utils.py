"""Funciones auxiliares del proyecto: carga y limpieza de datos, estilo de gráficos y tests."""
import os
from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import chi2_contingency
from sklearn.linear_model import LogisticRegression

DATA = Path(os.environ.get("EDA_DATA", "data"))
LEVELS = ["ED0-2", "ED3_4", "ED5-8"]
LEVEL_NAMES = {"ED0-2": "Bajo", "ED3_4": "Medio", "ED5-8": "Alto"}
AGGREGATES = ["EU27_2020", "EA21"]

# Paleta del proyecto
NAVY, TEAL, ORANGE, PURPLE, GREY = "#1B2A41", "#2A9D8F", "#E76F51", "#6654A3", "#8A94A6"


def set_style():
    plt.rcParams.update({
        "figure.dpi": 110, "savefig.dpi": 200, "axes.spines.top": False,
        "axes.spines.right": False, "axes.grid": True, "grid.alpha": 0.2,
        "axes.grid.axis": "y", "axes.titleweight": "bold", "axes.titlesize": 13,
        "axes.titlelocation": "left", "font.size": 10, "axes.edgecolor": "#C8CED8",
    })


# ---------- Carga y limpieza ----------
def load_education():
    """H1: empleo por nivel educativo (Eurostat lfsa_ergaed). 25-64 años, ambos sexos, sin agregados."""
    df = pd.read_csv(DATA / "eurostat_employment_education.csv")
    df = df.dropna(axis=1, how="all")
    df = df[(df["age"] == "Y25-64") & (df["sex"] == "T") & (~df["geo"].isin(AGGREGATES))]
    return df[["geo", "TIME_PERIOD", "isced11", "OBS_VALUE"]].copy()


def load_migration():
    """H2: empleo por situación migratoria y educación (Eurostat lfsa_erganedm). 15-64 años."""
    df = pd.read_csv(DATA / "eurostat_employment_migration_education.csv")
    df = df.dropna(axis=1, how="all")
    df = df[df["isced11"].isin(LEVELS) & df["mgstatus"].isin(["FBO", "NBO_NAT"])]
    return df[["geo", "sex", "TIME_PERIOD", "isced11", "mgstatus", "OBS_VALUE"]].copy()


def migration_gap(df):
    """Brecha FBO - NBO_NAT (p.p.) por geo, año, nivel educativo y sexo."""
    p = df.pivot_table(index=["geo", "sex", "TIME_PERIOD", "isced11"],
                       columns="mgstatus", values="OBS_VALUE").dropna()
    p["gap"] = p["FBO"] - p["NBO_NAT"]
    return p.reset_index()


def load_piaac():
    """H3: PIAAC Ciclo 2, España. Solo las columnas necesarias (el CSV tiene 2.483)."""
    pv = [f"PVLIT{i}" for i in range(1, 11)] + [f"PVNUM{i}" for i in range(1, 11)]
    use = ["EDLEVEL3", "PAIDWORK5", "ISCO08_C", "EARNMTHALLPPPC2", "SPFWT0"] + pv
    df = pd.read_csv(DATA / "datos_educacion_habilidades_empleo_espana.csv",
                     sep=";", usecols=use, dtype=str)
    for c in pv + ["EARNMTHALLPPPC2", "SPFWT0"]:
        df[c] = pd.to_numeric(df[c], errors="coerce")
    df["literacy"] = df[pv[:10]].mean(axis=1)   # media de plausible values (exploratorio)
    df["numeracy"] = df[pv[10:]].mean(axis=1)
    df["cognitive"] = df[["literacy", "numeracy"]].mean(axis=1)
    df = df[df["EDLEVEL3"].isin(["1", "2", "3"]) & df["PAIDWORK5"].isin(["0", "1"])].copy()
    df["education"] = df["EDLEVEL3"].map({"1": "Low", "2": "Medium", "3": "High"})
    df["paid_work"] = df["PAIDWORK5"].astype(int)
    df["cognitive_10"] = df["cognitive"] / 10
    return df.drop(columns=[c for c in pv])


def load_piaac_migration():
    """PIAAC España: origen (BORNLANG: 1-2 nacido en España, 3-4 nacido fuera), educación, trabajo, ocupación y edad."""
    use = ["BORNLANG", "EDLEVEL3", "PAIDWORK5", "ISCO1C", "AGE_R", "SPFWT0"]
    df = pd.read_csv(DATA / "datos_educacion_habilidades_empleo_espana.csv", sep=";", usecols=use, dtype=str)
    df = df[df["BORNLANG"].isin(["1", "2", "3", "4"]) & df["EDLEVEL3"].isin(["1", "2", "3"])].copy()
    df["foreign_born"] = df["BORNLANG"].isin(["3", "4"])
    df["education"] = df["EDLEVEL3"].map({"1": "Low", "2": "Medium", "3": "High"})
    df["age"] = pd.to_numeric(df["AGE_R"], errors="coerce")
    df["paid_work"] = df["PAIDWORK5"].map({"1": 1, "0": 0})
    occ = pd.to_numeric(df["ISCO1C"], errors="coerce")
    df["occ"] = occ.where(occ.between(1, 9))
    return df


def load_daioe(year=2025):
    x = pd.read_excel(DATA / "daioe_isco08.xlsx")
    x = x[x["year"] == year][["occ_code_isco08", "occ_title_isco08", "daioe_allapps"]]
    x = x.dropna(subset=["daioe_allapps"]).copy()
    x["isco"] = pd.to_numeric(x["occ_code_isco08"], errors="coerce")
    return x


# ---------- Estadística ----------
def design_matrix(d):
    return np.column_stack([d["cognitive_10"], (d["education"] == "Medium").astype(int),
                           (d["education"] == "High").astype(int)])


def logit_odds_ratios(d, weights=None):
    """Regresión logística sin penalización. Devuelve OR (cognitive_10, Medium, High) y pseudo-R² de McFadden."""
    X, y = design_matrix(d), d["paid_work"].values
    m = LogisticRegression(C=np.inf, max_iter=2000).fit(X, y, sample_weight=weights)
    p = m.predict_proba(X)[:, 1]
    w = np.ones(len(y)) if weights is None else weights
    ll = np.sum(w * (y * np.log(p) + (1 - y) * np.log(1 - p)))
    p0 = np.average(y, weights=w)
    ll0 = np.sum(w * (y * np.log(p0) + (1 - y) * np.log(1 - p0)))
    return np.exp(m.coef_[0]), 1 - ll / ll0


def bootstrap_or(d, n=300, seed=1):
    """IC 95 % bootstrap de los odds ratios (sin pesos muestrales)."""
    rng = np.random.default_rng(seed)
    res = [logit_odds_ratios(d.sample(len(d), replace=True, random_state=int(rng.integers(1e9))))[0]
           for _ in range(n)]
    res = np.array(res)
    return np.percentile(res, 2.5, axis=0), np.percentile(res, 97.5, axis=0)


def income_model(d):
    """log(ingreso mensual, USD PPP) ~ competencias(+10 pts) + educación. Solo personas con ingreso declarado > 0."""
    s = d[d["EARNMTHALLPPPC2"].notna() & (d["EARNMTHALLPPPC2"] > 0)].copy()
    y = np.log(s["EARNMTHALLPPPC2"].values)
    A = np.column_stack([np.ones(len(s)), design_matrix(s)])
    b = np.linalg.lstsq(A, y, rcond=None)[0]
    r = y - A @ b
    se = np.sqrt(np.diag(r @ r / (len(y) - A.shape[1]) * np.linalg.inv(A.T @ A)))
    r2 = 1 - r @ r / ((y - y.mean()) @ (y - y.mean()))
    return len(s), b, b / se, r2


def chi2_by_level(d):
    out = []
    for lvl in ["Low", "Medium", "High"]:
        s = d[d["education"] == lvl]
        t = pd.crosstab(s["cog_quartile"], s["paid_work"])
        c2, p, _, _ = chi2_contingency(t)
        v = np.sqrt(c2 / (t.values.sum() * (min(t.shape) - 1)))
        out.append({"Nivel": lvl, "chi2": round(c2, 2), "p-valor": round(p, 4), "V de Cramér": round(v, 3)})
    return pd.DataFrame(out)
