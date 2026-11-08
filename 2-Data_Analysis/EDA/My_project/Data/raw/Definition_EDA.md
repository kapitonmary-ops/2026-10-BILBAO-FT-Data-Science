# Definición de hipótesis y fuentes de datos — Proyecto EDA

**Proyecto:** Education, Cognitive Skills and Employment in the Age of Artificial Intelligence

**Pregunta general de investigación:**

¿Qué nos permiten comprender la educación formal, la situación migratoria y las competencias cognitivas sobre las perspectivas laborales de las personas en el contexto del desarrollo de la inteligencia artificial?

**Marco conceptual común**

El proyecto reúne tres dimensiones:

- **Educación:** cualificación formal.
- **Situación migratoria:** factor social asociado a diferencias en las perspectivas laborales.
- **Competencias cognitivas:** capacidades para trabajar con información, relevantes en un contexto de transformación digital.

Las tres hipótesis deben contribuir a una historia de investigación común. El proyecto no pretende demostrar causalmente el impacto de la IA. Los resultados se interpretarán dentro de los límites de los datos disponibles.

## Fuentes de datos

### 1. Eurostat — Employment rates by educational attainment level

- **Fuente:** Eurostat.
- **Cobertura:** países de la Unión Europea.
- **Periodo previsto:** 2015–2025, sujeto a disponibilidad.
- **Objetivo:** analizar la relación entre nivel educativo y tasa de empleo, comparar países y observar la evolución temporal.
- **Enlace:** https://ec.europa.eu/eurostat/databrowser/view/lfsa_ergaed/default/table?lang=en

### 2. Eurostat — Employment rates by migration status, citizenship and educational attainment level

- **Fuente:** Eurostat.
- **Cobertura:** países europeos disponibles.
- **Periodo previsto:** 2021–2025, sujeto a disponibilidad.
- **Objetivo:** comparar tasas de empleo por situación migratoria/c ciudadanía y nivel educativo.
- **Enlace:** https://ec.europa.eu/eurostat/databrowser/view/lfsa_erganedm/default/table?lang=en

### 3. OECD — PIAAC Cycle 2, Spain (Survey of Adult Skills)

- **Fuente:** OECD, PIAAC Cycle 2, Public Use File de España.
- **Contenido relevante:** nivel educativo, competencias cognitivas (literacy y numeracy), variables de empleo, ingresos y ocupación, según disponibilidad y calidad de las variables.
- **Objetivo:** estudiar cómo las competencias cognitivas se relacionan con resultados laborales, considerando educación formal y experiencia laboral.
- **Enlace:** https://www.oecd.org/en/data/datasets/piaac-2nd-cycle-database.html

### Fuente complementaria propuesta para contextualizar H3 en relación con AI

- **OECD AI Exposure Measure** (dataset descargable XLSX): índice de exposición ocupacional basado en la correspondencia entre capacidades de AI y requisitos de ocupaciones.
- **Alternativa complementaria:** DAIOE, índice abierto de exposición ocupacional a AI con clasificación ISCO-08.
- Estas fuentes se deben revisar para confirmar códigos, nivel de agregación y posibilidad de enlazarlas con la variable ocupacional ISCO-08 de PIAAC.
- **OECD AI Exposure Measure:** https://www.oecd.org/en/about/projects/artificial-intelligence-and-future-of-skills.html
- **DAIOE:** https://ai-econlab.com/daioe/

La exposición ocupacional a AI se utilizará como contexto analítico. No representa una medida directa de adopción de AI por parte de la persona, de pérdida de empleo ni de efecto causal sobre los resultados laborales.

## Hipótesis de análisis

Se establecen **tres hipótesis en total: H1, H2 y H3. No se incluye H4.**

### H1. Educación y empleo en Europa

**Hipótesis:** Las personas con un nivel educativo más alto presentan una mayor tasa de empleo. La magnitud de esta relación varía entre los países europeos.

- **Fuente:** Eurostat, Employment rates by educational attainment level.
- **Variables principales:** nivel educativo, tasa de empleo, país y año.
- **Análisis previsto:** comparar tasas de empleo por nivel educativo y país, y observar su evolución temporal.

### H2. Diferencias de empleo según la situación migratoria

**Hipótesis:** Entre personas con el mismo nivel educativo, la tasa de empleo es menor para la población migrante que para la población no migrante.

- **Fuente:** Eurostat, Employment rates by migration status, citizenship and educational attainment level.
- **Variables principales:** situación migratoria/ciudadanía (según las categorías disponibles), nivel educativo y tasa de empleo.
- **Análisis previsto:** comparar tasas de empleo entre grupos con el mismo nivel educativo.

### H3. Educación, competencias cognitivas y resultados laborales en España

**Pregunta de investigación:** En España, ¿cómo se relacionan las competencias cognitivas reales (literacy y numeracy) con los resultados laborales, considerando el nivel de educación formal?

**Hipótesis de trabajo:** Unas competencias cognitivas más altas se asocian con mejores resultados laborales, incluso al comparar personas con niveles similares de educación formal. Esta hipótesis se analizará principalmente con PIAAC y con las variables que sean adecuadas y estén disponibles.

**Análisis complementario exploratorio (no constituye una cuarta hipótesis):** Para mantener una conexión concreta y manejable con la inteligencia artificial, se propone comparar las competencias cognitivas de trabajadores en ocupaciones con mayor y menor exposición potencial a AI, utilizando un único índice de exposición ocupacional y agrupando las ocupaciones en dos grupos si la unión con ISCO-08 es viable. La pregunta complementaria será: *¿Los trabajadores de ocupaciones con mayor exposición potencial a AI presentan diferentes niveles de literacy y numeracy que los trabajadores de ocupaciones con menor exposición?* Este análisis no afirmará que AI requiere más habilidades ni que causa cambios laborales; examinará una asociación exploratoria.

- **Fuente principal:** OECD, PIAAC Cycle 2, Spain.
- **Fuente complementaria propuesta:** OECD AI Exposure Measure; DAIOE (ISCO-08) como alternativa.
- **Variables principales PIAAC:** educación formal, literacy, numeracy y un resultado laboral principal (situación de empleo o ingresos, según disponibilidad y calidad); Work_Exp podrá incluirse si su definición es adecuada.
- **Variable complementaria para el análisis exploratorio AI:** un índice de exposición ocupacional, enlazado por ISCO-08, sujeto a compatibilidad.
- **Análisis previsto:**
  1. Explorar la asociación entre competencias cognitivas y resultados laborales.
  2. Considerar educación formal y experiencia laboral al comparar grupos.
  3. Como análisis complementario y solo si la unión por ISCO-08 es viable, comparar Literacy/Numeracy entre ocupaciones con exposición potencial a AI alta y baja.
  4. Interpretar los resultados como asociaciones exploratorias, no como prueba del efecto causal de AI ni de que AI exige mayores competencias.
- **Limitaciones:** PIAAC es una encuesta observacional y transversal; la exposición a AI es un índice de ocupación, no una medida individual de uso o impacto de AI. La viabilidad final de los análisis depende de la disponibilidad, los valores missing, el tamaño de muestra y la compatibilidad de códigos.

## Relación entre hipótesis y fuentes

| Hipótesis | Fuente de datos                                                                                                         | Enfoque                                                                                                                                                        |
| ---------- | ----------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| H1         | Eurostat — Employment rates by educational attainment level                                                            | Educación formal y tasa de empleo en Europa, por país y año                                                                                                 |
| H2         | Eurostat — Employment rates by migration status, citizenship and educational attainment level                          | Diferencias de empleo según situación migratoria dentro de niveles educativos                                                                                |
| H3         | OECD PIAAC Cycle 2, Spain; como análisis adicional, un índice de exposición ocupacional a AI (solo si es compatible) | Relación entre competencias cognitivas, educación y resultados laborales; comparación exploratoria de skills entre ocupaciones con exposición AI alta/baja |

## Hilo conductor de la investigación

1. **H1:** examina la relación general entre educación formal y empleo.
2. **H2:** muestra que las perspectivas laborales también pueden diferir por un factor social —la situación migratoria— incluso al comparar niveles educativos.
3. **H3:** profundiza en las competencias cognitivas reales y los resultados laborales. Un análisis adicional pequeño puede conectar las competencias con exposición ocupacional a AI, sin añadir una nueva hipótesis.

**Alcance:** las hipótesis analizan relaciones y asociaciones; no implican causalidad. La interpretación final se ajustará a la disponibilidad, calidad y comparabilidad de las variables.
