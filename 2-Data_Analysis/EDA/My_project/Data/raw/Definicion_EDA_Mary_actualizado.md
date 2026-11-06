# Propuesta de fuentes de datos para el proyecto

**Tema:** Education & Economic Opportunity Gap

**Pregunta de investigación:**

¿La educación garantiza mejores oportunidades económicas? ¿Qué importancia tienen las competencias reales frente al nivel de educación formal?

Para desarrollar el proyecto, propongo utilizar las siguientes fuentes de datos oficiales:

### 1. Eurostat — `lfsa_ergaed`

**Employment rates by educational attainment level**

- Fuente: Eurostat.
- Periodo: 2015–2025.
- Cobertura: países de la Unión Europea.
- Objetivo: analizar la relación entre el nivel educativo y las tasas de empleo en diferentes países europeos.

Enlace: https://ec.europa.eu/eurostat/databrowser/view/lfsa_ergaed/default/table?lang=en

### 2. Eurostat — `lfsa_erganedm`

**Employment rates by migration status, citizenship and educational attainment level**

- Fuente: Eurostat.
- Periodo: 2021–2025.
- Cobertura: países europeos disponibles.
- Objetivo: comparar las tasas de empleo según el nivel educativo y la situación migratoria.

Enlace: https://ec.europa.eu/eurostat/databrowser/view/lfsa_erganedm/default/table?lang=en

### 3. OECD — PIAAC Cycle 2, Spain

**Survey of Adult Skills**

- Fuente: OECD.
- País: España.
- Archivo descargado: `prgespp2.csv`.
- Contenido: información individual sobre educación, competencias cognitivas, empleo e ingresos.
- Objetivo: estudiar la relación entre el nivel educativo, las competencias reales y los resultados económicos.

Enlace: https://www.oecd.org/en/data/datasets/piaac-2nd-cycle-database.html

## Hipótesis de análisis

A partir de la pregunta de investigación y de las fuentes de datos seleccionadas, se plantean las siguientes hipótesis iniciales. Se comprobarán mediante el análisis exploratorio y podrán revisarse si los datos disponibles no permiten contrastarlas.

### H1. Educación y empleo en Europa

**Hipótesis:** Las personas con un nivel educativo más alto presentan una mayor tasa de empleo. La magnitud de esta relación varía entre los países europeos.

- **Fuente:** Eurostat, `lfsa_ergaed`.
- **Variables principales:** nivel educativo, tasa de empleo, país y año.
- **Análisis previsto:** comparar las tasas de empleo por nivel educativo y país, y observar su evolución temporal.

### H2. Diferencias de empleo según la situación migratoria

**Hipótesis:** Entre personas con el mismo nivel educativo, la tasa de empleo es menor para la población migrante que para la población no migrante.

- **Fuente:** Eurostat, `lfsa_erganedm`.
- **Variables principales:** situación migratoria/c ciudadanía (según las categorías disponibles), nivel educativo y tasa de empleo.
- **Análisis previsto:** comparar las tasas de empleo entre grupos con el mismo nivel educativo.

### H3. La brecha de empleo y el nivel educativo

**Hipótesis exploratoria:** La diferencia en la tasa de empleo entre población migrante y no migrante aumenta en los niveles educativos más altos.

- **Fuente:** Eurostat, `lfsa_erganedm`.
- **Variables principales:** situación migratoria, nivel educativo y tasa de empleo.
- **Análisis previsto:** calcular y comparar la brecha de empleo entre grupos para cada nivel educativo.
- **Nota:** esta hipótesis se contrastará únicamente si las categorías y observaciones disponibles permiten una comparación consistente.

### H4. Competencias cognitivas e ingresos en España

**Hipótesis:** En España, unas competencias cognitivas más altas se relacionan con mayores ingresos, incluso al comparar personas con un nivel educativo similar.

- **Fuente:** OECD, PIAAC Cycle 2, Spain (`prgespp2.csv`).
- **Variables principales:** competencias cognitivas, nivel educativo e ingresos.
- **Análisis previsto:** explorar la relación entre competencias e ingresos, controlando o agrupando por nivel educativo.
- **Nota:** la interpretación deberá tener en cuenta la estructura y las variables disponibles en el archivo PIAAC.

## Relación entre hipótesis y fuentes

| Hipótesis | Fuente de datos                              | Enfoque                                                              |
| ---------- | -------------------------------------------- | -------------------------------------------------------------------- |
| H1         | Eurostat `lfsa_ergaed`                     | Educación y tasa de empleo por país y año                         |
| H2         | Eurostat `lfsa_erganedm`                   | Comparación de empleo por situación migratoria y nivel educativo   |
| H3         | Eurostat `lfsa_erganedm`                   | Diferencias de empleo según nivel educativo y situación migratoria |
| H4         | OECD PIAAC Cycle 2, Spain (`prgespp2.csv`) | Competencias cognitivas e ingresos dentro de niveles educativos      |

**Alcance:** Las hipótesis expresan relaciones que se van a explorar con los datos; no implican causalidad. Los resultados finales dependerán de la disponibilidad, calidad y comparabilidad de las variables.
