# ¿Título, origen o competencias? Educación, empleo y IA

Análisis exploratorio de datos (EDA) sobre qué se asocia con tener empleo: **el título, el origen migratorio o las competencias reales**. Proyecto individual del Data Science Bootcamp.

**Autora:** Maryna Kapiton · **Presentación:** `presentation/presentacion_mixta_ES.pptx` (la versión `_RU.pptx` es solo para ensayar) · **Memoria:** `docs/Memoria_EDA.pdf` · **Guion de 15 min:** `docs/guion_15min.md`

## Pregunta

El proyecto parte de una experiencia personal: máster en finanzas, diez años de experiencia directiva, emigrante en España y cuatro años hasta un puesto junior. ¿Es un caso aislado o refleja un patrón? El recorrido va de **Europa** (H1 y H2) a **España** (H3 y análisis de IA) y termina en ese caso.

## Resultados

| Hipótesis | Ámbito y datos | Resultado |
|---|---|---|
| **H1.** Más educación, más empleo; la magnitud varía por país. | Europa · Eurostat, 36 países, 2015-2025 | **Confirmada.** Diferencia media de 31 p.p. entre educación alta y baja; de 16 p.p. (Islandia) a 55 p.p. (Bosnia y Herz.). |
| **H2.** A igual educación, los migrantes tienen menos empleo. | Europa · Eurostat, 34 países, 2021-2025 | **Parcial.** Con estudios superiores, menos empleo en 34 de 34 países (mediana −8,4 p.p.); con estudios básicos, más empleo (+5,3). En España la diferencia se reduce de −11 a −7 p.p. y es mayor en mujeres. |
| **H3.** Más competencias, mejores resultados laborales, a igual educación. | Solo España · OECD PIAAC, n = 5.192 | **Parcial.** Asociación positiva pero débil; el título pesa más (OR 4,4 frente a 1,05 por +10 puntos de competencias; con pesos, 1,02). |

**Análisis complementario (no es una cuarta hipótesis; solo España):** el porcentaje de personas que trabaja en ocupaciones muy expuestas a la IA (índice DAIOE 2025) sube con el título (27 % → 40 % → 63 %) y con las competencias (36 % → 58 %); el título pesa más. El índice describe ocupaciones, no empleos que se vayan a perder.

Todos los resultados son **asociaciones**, no efectos causales.

## Tecnologías

Python · pandas · NumPy · matplotlib · SciPy (chi-cuadrado, test de Welch) · scikit-learn (regresión logística) · Jupyter.

## Estructura

```
├── README.md
├── requirements.txt
├── docs/                 # memoria (Memoria_EDA .md/.docx/.pdf) y guion de la presentación
├── presentation/         # presentación (.pptx)
├── results/figures/      # gráficos generados por main.ipynb
└── src/
    ├── main.ipynb        # cuaderno principal: todos los pasos del análisis
    ├── data/             # datos (ver src/data/README.md)
    ├── notebooks/        # borradores de trabajo H1, H2 y H3 (autora)
    └── utils/eda_utils.py  # carga de datos, estilo de gráficos y funciones estadísticas
```

## Cómo ejecutarlo

```bash
pip install -r requirements.txt
cd src && jupyter notebook main.ipynb
```

Los archivos de datos pesados (PIAAC y DAIOE) no están en el repositorio; las instrucciones para descargarlos están en `src/data/README.md`. Si están en otra carpeta: `EDA_DATA=/ruta/a/los/datos jupyter notebook main.ipynb`.

## Uso de herramientas de IA

Las preguntas, las hipótesis, el análisis de H1, H2 y H3 y las conclusiones son de la autora (borradores en `src/notebooks/`). En `main.ipynb`, las celdas marcadas con **[Añadido con ayuda de IA]** (gráficos para la presentación, comprobaciones de robustez y el análisis complementario de IA) se prepararon con un asistente de IA y fueron revisadas por la autora. La presentación y el guion se prepararon con el mismo apoyo.

## Limitaciones

Datos observacionales; promedios simples de países; análisis PIAAC sin el diseño muestral complejo (solo una comprobación con pesos, que debilita el resultado sobre competencias); `PAIDWORK5` mide haber trabajado en los últimos cinco años, no el empleo actual; el índice de IA describe ocupaciones, no personas.
