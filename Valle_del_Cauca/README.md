# Análisis de Pobreza y Proyecciones de Población: Valle del Cauca

![Banner Valle del Cauca](https://upload.wikimedia.org/wikipedia/commons/thumb/e/ef/Flag_of_Valle_del_Cauca.svg/320px-Flag_of_Valle_del_Cauca.svg.png)

## Contenido del Directorio

Este directorio contiene todos los archivos relacionados con el análisis de indicadores de pobreza y proyecciones de población para el departamento del Valle del Cauca, Colombia. El trabajo es parte del curso de Fundamentos de Economía.

### Estructura de Carpetas

- **datos/**: Archivos CSV con datos procesados específicos para Valle del Cauca
- **notebooks/**: Jupyter Notebooks con el análisis detallado
- **visualizaciones/**: Gráficos y figuras utilizadas en el análisis y presentación
- **documentacion/**: Guías, presentaciones y documentos explicativos
- **scripts/**: Scripts específicos para procesar y visualizar datos del Valle del Cauca

### Documentos Principales

Los documentos principales se encuentran en la carpeta **documentacion/**:

1. **Guía para Exposición** - Documento principal para preparar la presentación, incluye explicaciones detalladas sobre el origen de los datos y visualizaciones.

2. **Análisis de Datos (Notebook)** - Notebook de Python con el código completo para el procesamiento y análisis de datos.

3. **Presentación del Proyecto** - Resumen formal de la metodología, hallazgos y conclusiones del análisis.

4. **Guía de Análisis** - Documento técnico que detalla el proceso de análisis y generación de datos.

5. **Instrucciones para Power BI** - Guía básica para la construcción del tablero en Power BI.

6. **Guía Detallada de Power BI** - Instrucciones paso a paso para crear el tablero interactivo.

7. **Resumen del Análisis** - Síntesis del trabajo realizado y próximos pasos.

### Visualizaciones

Las visualizaciones se encuentran en la carpeta **visualizaciones/**:

#### Visualizaciones Básicas

- **Comparativa de Indicadores** - Gráfico comparativo de los principales indicadores de pobreza
- **Proyección de Población** - Gráfico con proyecciones de población hasta 2025

#### Visualizaciones para Exposición

- **Tendencia IPM Comparativa** - Evolución del Índice de Pobreza Multidimensional
- **Comparativa por Área Geográfica** - Comparación entre zonas urbanas y rurales
- **Composición Étnica** - Distribución de la población por grupos étnicos
- **Mapa de Calor de Privaciones** - Análisis de factores de pobreza multidimensional
- **Comparativa con Departamentos Vecinos** - Contexto regional

### Notebooks de Análisis

Los notebooks de análisis se encuentran en la carpeta **notebooks/**:

- **analisis_valle_del_cauca.ipynb** - Notebook principal con todo el procesamiento de datos
- **analisis_valle_del_cauca_ejecutado.ipynb** - Versión ejecutada con todos los resultados visibles

### Scripts de Procesamiento

Los scripts de procesamiento se encuentran en la carpeta **scripts/**:

- **crear_visualizaciones_valle.py** - Script para generar visualizaciones básicas
- **crear_visualizaciones_simplificadas.py** - Versión simplificada del script de visualizaciones
- **generar_visualizaciones_exposicion.py** - Script para generar visualizaciones avanzadas para la exposición

### Datos Procesados

La carpeta **datos/** contiene archivos CSV con datos filtrados específicamente para el Valle del Cauca:

- **Pobreza Multidimensional**: Archivos con el prefijo `IPM_` y `IC_IPM_`
- **Análisis por Características Demográficas**: Archivos con sufijos como `_Sexo_` y `_Sexo Jefe_`
- **Datos Consolidados**: Archivo `pobreza_multidimensional_consolidado_valle_del_cauca.csv`

## Indicadores Principales

Los indicadores clave analizados para el Valle del Cauca incluyen:

1. **Pobreza Multidimensional**: Indicador que evalúa privaciones en diferentes dimensiones de bienestar
2. **Proyecciones de Población**: Estimaciones de crecimiento poblacional por área geográfica y grupos de edad
3. **Análisis por Zona Geográfica**: Diferencias entre zonas urbanas y rurales
4. **Análisis por Grupos Étnicos**: Enfoque en población afrodescendiente e indígena

## Cómo usar este material

### Para presentaciones

1. Revisa la documentación en la carpeta **documentacion/** que contiene instrucciones detalladas sobre cómo estructurar una presentación efectiva
2. Utiliza las visualizaciones incluidas en este directorio para ilustrar puntos clave
3. Apóyate en las tablas y datos estadísticos proporcionados en la guía

### Para análisis técnico

1. Explora los notebooks en la carpeta **notebooks/** para entender el procesamiento de datos
2. Revisa los archivos CSV en la carpeta **datos/** para acceder a datos específicos para análisis adicionales
3. Utiliza las instrucciones de Power BI para construir o modificar el tablero de visualización

### Para continuar el trabajo

1. Consulta el resumen del análisis que identifica áreas para trabajo futuro
2. Considera las limitaciones mencionadas en la presentación del proyecto
3. Explora la posibilidad de incorporar datos más recientes siguiendo la metodología establecida

## Metodología

El análisis sigue los siguientes pasos metodológicos:

1. Carga y limpieza de datos de las fuentes oficiales
2. Filtrado específico para el departamento del Valle del Cauca
3. Cálculo de estadísticas descriptivas e indicadores clave
4. Generación de visualizaciones informativas
5. Análisis comparativo con promedios nacionales
6. Elaboración de conclusiones y recomendaciones

## Hallazgos Principales

Los resultados más relevantes del análisis incluyen:

- El Valle del Cauca presenta indicadores de pobreza multidimensional significativamente mejores que el promedio nacional
- Persiste una marcada brecha entre zonas urbanas y rurales en todos los indicadores
- Las dimensiones más críticas de pobreza multidimensional son el empleo formal, acceso a salud y logro educativo
- La población afrodescendiente presenta indicadores socioeconómicos menos favorables

## Fuentes de Datos

Los datos utilizados en este análisis provienen de fuentes oficiales del Departamento Administrativo Nacional de Estadística (DANE) de Colombia:

1. **Proyecciones de Población con Pertenencia Étnico-Racial**
   - Archivo: `anex-DCD-Proypoblacion-PerteneniaEtnicoRacialmun.xlsx`
   - Fuente: DANE - Proyecciones de población

2. **Indicadores de Pobreza Monetaria**
   - Archivo: `anex-PM-Departamental-2023.xlsx`
   - Fuente: DANE - Pobreza Monetaria

3. **Indicadores de Pobreza Multidimensional**
   - Archivo: `anex-PMultidimensional-Departamental-2024.xlsx`   - Fuente: DANE - Pobreza Multidimensional

---

*Este directorio fue creado como parte del curso de Fundamentos de Economía - 2025*
