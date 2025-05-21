# Presentación del Proyecto: Análisis de Indicadores de Pobreza y Proyecciones de Población del Valle del Cauca

## 1. Introducción

Este proyecto analiza y visualiza los datos de indicadores de pobreza y proyecciones de población para el departamento del Valle del Cauca, Colombia. El objetivo es crear un tablero interactivo en Power BI que permita comprender la evolución y el estado actual de estos indicadores en el departamento.

## 2. Fuentes de Datos

El análisis se basa en tres conjuntos de datos oficiales:

1. **Proyecciones de Población con Pertenencia Étnico-Racial** (DANE)
   - Archivo: `anex-DCD-Proypoblacion-PerteneniaEtnicoRacialmun.xlsx`
   - Contiene proyecciones por municipio, área geográfica y grupos étnico-raciales
   - Período: 2018-2035

2. **Indicadores de Pobreza Monetaria** (DANE)
   - Archivo: `anex-PM-Departamental-2023.xlsx`
   - Incluye incidencia de pobreza, brecha, severidad y coeficiente de Gini
   - Período: 2018-2023

3. **Indicadores de Pobreza Multidimensional** (DANE)
   - Archivo: `anex-PMultidimensional-Departamental-2024.xlsx`
   - Contiene IPM y privaciones por hogar
   - Período: 2018-2022

## 3. Metodología

El proceso de análisis siguió estos pasos:

1. **Extracción y limpieza de datos**
   - Procesamiento de archivos Excel usando Python (pandas)
   - Filtrado específico para el departamento del Valle del Cauca
   - Transformación a formatos adecuados para visualización

2. **Análisis exploratorio**
   - Identificación de tendencias en indicadores de pobreza
   - Comparación con promedios nacionales
   - Análisis por subgrupos (sexo, área geográfica, pertenencia étnica)

3. **Visualización de datos**
   - Generación de gráficos estáticos usando matplotlib y seaborn
   - Creación de un tablero interactivo en Power BI

## 4. Principales Hallazgos para el Valle del Cauca

### Indicadores de Pobreza

- **Pobreza Multidimensional**:
  - Tendencia a la baja en el período 2018-2022
  - El Valle del Cauca presenta indicadores más favorables que el promedio nacional
  - Diferencias significativas entre zonas urbanas y rurales

- **Distribución por Género**:
  - Los hogares con jefatura femenina muestran mayor incidencia de pobreza
  - La brecha de género ha disminuido ligeramente en los últimos años

### Proyecciones de Población

- **Tendencia demográfica**:
  - Crecimiento poblacional moderado proyectado hasta 2035
  - Concentración en centros urbanos principales (Cali, Buenaventura, Palmira)

- **Composición étnica**:
  - Importante presencia de población afrocolombiana (una de las más altas del país)
  - Distribución heterogénea de grupos étnicos en el territorio

## 5. Estructura del Tablero en Power BI

El tablero está organizado en las siguientes páginas:

1. **Resumen Ejecutivo**
   - Indicadores clave a nivel departamental
   - Comparativa con promedios nacionales
   - Evolución temporal general

2. **Pobreza Monetaria**
   - Incidencia, brecha y severidad de la pobreza
   - Coeficiente de Gini y desigualdad
   - Análisis por subgrupos

3. **Pobreza Multidimensional**
   - Incidencia general y por dimensiones
   - Privaciones específicas más comunes
   - Evolución temporal

4. **Análisis Demográfico**
   - Proyecciones de población total
   - Distribución por grupos étnicos
   - Distribución geográfica

5. **Análisis Municipal**
   - Indicadores desagregados por municipios principales
   - Mapa coroplético con variables clave

## 6. Conclusiones

- El Valle del Cauca muestra una tendencia positiva en la reducción de indicadores de pobreza, con mejores resultados que el promedio nacional en varias dimensiones.
  
- Persisten brechas significativas entre áreas urbanas y rurales, así como entre grupos poblacionales, que requieren atención específica.
  
- La importante presencia de población afrocolombiana en el departamento destaca la necesidad de políticas con enfoque diferencial.
  
- Las proyecciones demográficas muestran un crecimiento moderado y sostenido, con mayor concentración en los centros urbanos principales.

## 7. Recomendaciones

- Fortalecer las políticas de reducción de pobreza en zonas rurales, donde los indicadores son menos favorables.
  
- Implementar programas específicos para hogares con jefatura femenina, que muestran mayor vulnerabilidad.
  
- Desarrollar estrategias de inclusión económica para la población afrocolombiana, considerando su importante presencia en el departamento.
  
- Utilizar el tablero como herramienta de seguimiento y evaluación de políticas públicas, actualizándolo periódicamente con nuevos datos.

---

*Este proyecto fue desarrollado como parte del curso de Fundamentos de Economía, utilizando datos oficiales del DANE para analizar la situación socioeconómica del Valle del Cauca.*
