# Proyecto: Tablero de Indicadores de Pobreza y Proyecciones de Población

## Resumen del Trabajo Realizado

Este documento presenta un resumen del trabajo realizado para crear un tablero en Power BI que ilustra los resultados de proyecciones de población e indicadores de pobreza del departamento de ANTIOQUIA.

### 1. Análisis de Datos Disponibles

Se analizaron tres archivos de Excel proporcionados:

1. **anex-DCD-Proypoblacion-PerteneniaEtnicoRacialmun.xlsx**: Contiene datos de proyecciones de población por municipio, año y pertenencia étnico-racial.
2. **anex-PM-Departamental-2023.xlsx**: Contiene indicadores de pobreza monetaria por departamento.
3. **anex-PMultidimensional-Departamental-2024.xlsx**: Contiene indicadores de pobreza multidimensional por departamento.

### 2. Procesamiento de Datos

Se extrajeron datos específicos para el departamento de ANTIOQUIA de cada archivo, incluyendo:

- Proyecciones de población
- Indicadores de pobreza monetaria (16 hojas de indicadores)
- Indicadores de pobreza multidimensional (12 hojas de indicadores)

Los datos procesados se guardaron en archivos CSV individuales en la carpeta `datos`, facilitando su importación a Power BI.

### 3. Indicadores Incluidos

El tablero incluye los siguientes indicadores solicitados:

1. Incidencia de Pobreza Multidimensional
2. Incidencia de la Pobreza Monetaria
3. Incidencia de la Pobreza Monetaria Extrema
4. Personas en situación de Pobreza Monetaria
5. Personas en situación de Pobreza Monetaria Extrema
6. Coeficiente de Gini
7. Promedio del Ingreso per cápita de la unidad de gasto de la población
8. Líneas de Pobreza Monetaria
9. Líneas de Pobreza Monetaria Extrema
10. Brecha de la Pobreza Monetaria
11. Brecha de la Pobreza Monetaria Extrema
12. Severidad de la Pobreza Monetaria
13. Severidad de la Pobreza Monetaria Extrema
14. Incidencia de la Pobreza Monetaria según sexo de la persona
15. Incidencia de la Pobreza Monetaria Extrema según sexo de la persona

### 4. Estructura del Tablero Propuesto

El tablero se estructura en cinco páginas:

1. **Resumen Ejecutivo**: Muestra los indicadores clave más recientes y su evolución.
2. **Análisis de Pobreza Monetaria**: Presenta tendencias y comparativas de los indicadores de pobreza monetaria.
3. **Análisis de Pobreza Multidimensional**: Analiza la pobreza multidimensional y sus componentes.
4. **Análisis por Género**: Compara indicadores por sexo y sexo del jefe de hogar.
5. **Proyecciones de Población**: Muestra datos demográficos y proyecciones.

### 5. Visualizaciones Creadas

Se generaron visualizaciones de ejemplo en la carpeta `visualizaciones`, incluyendo:

- Gráficos de tendencia de pobreza monetaria
- Gráficos comparativos de pobreza monetaria y extrema
- Visualización del coeficiente de Gini
- Análisis por género
- Un mockup del tablero completo

### 6. Documentación Generada

Se han generado los siguientes documentos para facilitar la implementación del tablero:

1. **guia_power_bi.md**: Guía detallada para crear el tablero en Power BI.
2. **instrucciones_powerbi.md**: Instrucciones generales sobre la estructura y contenido del tablero.
3. **datos/resumen_analisis.json**: Metadatos con información sobre los archivos procesados.
4. **datos/instrucciones_powerbi.txt**: Instrucciones específicas para trabajar con los datos procesados.

## Conclusiones y Recomendaciones

### Conclusiones

- Los datos proporcionados permiten un análisis completo de indicadores de pobreza para el departamento de ANTIOQUIA.
- La información está disponible principalmente para los años 2022-2023 en pobreza monetaria, y 2018-2024 en pobreza multidimensional.
- Los indicadores muestran tendencias importantes que pueden visualizarse efectivamente en Power BI.

### Recomendaciones

1. **Para la creación del tablero**:
   - Prestar atención a los nombres de columnas en los archivos CSV, que pueden requerir renombrado en Power BI.
   - Utilizar medidas calculadas (DAX) para enriquecer el análisis.
   - Mantener una estética consistente en todas las páginas.

2. **Para el análisis**:
   - Comparar los valores del departamento con promedios nacionales cuando sea posible.
   - Analizar las tendencias temporales para identificar patrones.
   - Explorar las relaciones entre diferentes indicadores (por ejemplo, Gini vs. Pobreza).

## Próximos Pasos

1. Abrir Power BI Desktop
2. Importar los archivos CSV de la carpeta `datos`
3. Seguir la guía proporcionada para crear el tablero
4. Personalizar según necesidades específicas
5. Guardar el archivo `.pbix` final

## Recursos Disponibles

- **Carpeta `datos`**: Contiene todos los archivos CSV procesados
- **Carpeta `visualizaciones`**: Contiene gráficos de ejemplo y mockup del tablero
- **Documentación**: Guías e instrucciones detalladas
- **Scripts Python**: Código fuente para el procesamiento de datos

---

*Este proyecto fue desarrollado como parte de la actividad "Proyecciones de Población e Indicadores de Pobreza" del curso Fundamentos de Economía.*
