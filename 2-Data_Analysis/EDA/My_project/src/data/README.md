# Datos

| Archivo | Fuente | ¿Incluido en el repositorio? |
|---|---|---|
| `eurostat_employment_education.csv` | Eurostat, `lfsa_ergaed` (empleo por nivel educativo) | Sí |
| `eurostat_employment_migration_education.csv` | Eurostat, `lfsa_erganedm` (empleo por situación migratoria y educación) | Sí |
| `datos_educacion_habilidades_empleo_espana.csv` | OECD, PIAAC Ciclo 2, Public Use File de España (separador `;`, 57 MB) | No (pesado) |
| `daioe_isco08.xlsx` | DAIOE, índice de exposición ocupacional a IA (ISCO-08) | No (pesado) |

## Cómo obtener los archivos que faltan

1. **PIAAC Ciclo 2 (España):** https://www.oecd.org/en/data/datasets/piaac-2nd-cycle-database.html. Guardar el CSV de España en esta carpeta con el nombre `datos_educacion_habilidades_empleo_espana.csv`.
2. **DAIOE:** https://ai-econlab.com/daioe/. Guardar la hoja ISCO-08 como `daioe_isco08.xlsx`.

Si los archivos están en otra carpeta, se puede indicar la ruta con la variable de entorno `EDA_DATA`:

```bash
EDA_DATA=/ruta/a/los/datos jupyter notebook src/main.ipynb
```
