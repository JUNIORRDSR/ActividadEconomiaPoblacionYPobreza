# Instrucciones para crear el Tablero de Power BI

## Introducción

Este documento proporciona instrucciones paso a paso para crear un tablero en Power BI que ilustre los resultados de proyecciones de población e indicadores de pobreza para el departamento asignado, utilizando los archivos procesados en el análisis de datos.

## Archivos de Datos

Los archivos necesarios se encuentran en la carpeta `datos` generada por el análisis. Estos incluyen:

1. Archivos de población por departamento
2. Archivos de indicadores de pobreza monetaria
3. Archivos de indicadores de pobreza multidimensional
4. Gráficos de ejemplo

## Indicadores de Pobreza a Visualizar

El tablero debe incluir los siguientes indicadores:

1. **Incidencia de Pobreza Multidimensional**
2. **Incidencia de la Pobreza Monetaria**
3. **Incidencia de la Pobreza Monetaria Extrema**
4. **Personas en situación de Pobreza Monetaria**
5. **Personas en situación de Pobreza Monetaria Extrema**
6. **Coeficiente de Gini**
7. **Promedio del Ingreso per cápita de la unidad de gasto de la población**
8. **Líneas de Pobreza Monetaria**
9. **Líneas de Pobreza Monetaria Extrema**
10. **Brecha de la Pobreza Monetaria**
11. **Brecha de la Pobreza Monetaria Extrema**
12. **Severidad de la Pobreza Monetaria**
13. **Severidad de la Pobreza Monetaria Extrema**
14. **Incidencia de la Pobreza Monetaria según sexo de la persona**
15. **Incidencia de la Pobreza Monetaria Extrema según sexo de la persona**

## Pasos para Crear el Tablero

### Paso 1: Importar los Datos

1. Abra Power BI Desktop
2. Seleccione "Obtener datos" > "Texto/CSV"
3. Navegue a la carpeta `datos` y seleccione los archivos CSV generados
4. Utilice "Transformar datos" para ajustar tipos de datos y formatos según sea necesario

### Paso 2: Crear Relaciones entre Tablas

1. Vaya a la vista "Modelo"
2. Cree relaciones entre las tablas utilizando columnas comunes como departamento y año
3. Verifique que las relaciones estén correctamente configuradas

### Paso 3: Crear Medidas Calculadas

Cree las siguientes medidas calculadas para enriquecer su análisis:

1. **Variación Anual de Pobreza**: `Variación Pobreza = ([Pobreza Año Actual] - [Pobreza Año Anterior]) / [Pobreza Año Anterior]`
2. **Comparativa con Promedio Nacional**: `Diferencia Nacional = [Indicador Departamental] - [Promedio Nacional]`

### Paso 4: Diseñar el Tablero

Organice su tablero en las siguientes páginas:

#### Página 1: Resumen Ejecutivo

1. Tarjetas con los indicadores clave más recientes
2. Gráfico de tendencia de los principales indicadores
3. Mapa del departamento con indicadores por municipio (si hay datos disponibles)

#### Página 2: Análisis de Pobreza Monetaria

1. Gráfico de líneas para la tendencia de Incidencia de Pobreza Monetaria
2. Gráfico de barras para comparar Pobreza Monetaria y Pobreza Monetaria Extrema
3. Tabla detallada con todos los indicadores monetarios
4. Segmentadores para filtrar por año

#### Página 3: Análisis de Pobreza Multidimensional

1. Gráfico de líneas para la tendencia de Incidencia de Pobreza Multidimensional
2. Gráficos de contribución de variables a la pobreza multidimensional
3. Comparativa con promedios nacionales

#### Página 4: Análisis por Género

1. Gráficos comparativos de pobreza por sexo
2. Tendencia histórica de brechas de género en pobreza
3. Tabla detallada con valores por sexo y año

#### Página 5: Proyecciones de Población

1. Pirámide poblacional (si hay datos por edad)
2. Gráfico de tendencia de población total
3. Distribución por grupos étnicos
4. Distribución urbano/rural

### Paso 5: Añadir Interactividad

1. Configure filtros cruzados entre visualizaciones
2. Añada segmentadores para filtrar por año, área geográfica, etc.
3. Configure acciones de obtención de detalles para navegar entre páginas

### Paso 6: Mejorar la Estética

1. Aplique un tema coherente con colores significativos
2. Añada títulos descriptivos a cada visualización
3. Incluya texto explicativo para contextualizar los datos
4. Añada logotipos e información de fuentes de datos

### Paso 7: Publicar y Compartir

1. Guarde el archivo .pbix
2. Publique en Power BI Service (opcional)
3. Exporte a PDF para entrega

## Recomendaciones Adicionales

1. **Simplicidad**: No sobrecargue cada página con demasiadas visualizaciones
2. **Consistencia**: Mantenga un diseño coherente en todas las páginas
3. **Contextualización**: Incluya definiciones de los indicadores para mejor comprensión
4. **Interactividad**: Asegúrese de que los filtros funcionen de manera lógica entre visualizaciones
5. **Narrativa**: Organice el tablero para contar una historia coherente sobre la situación de pobreza

## Ejemplo de Visualizaciones Recomendadas

1. **Para Incidencia de Pobreza**: Gráficos de líneas para mostrar tendencias
2. **Para Coeficiente de Gini**: Gráfico de barras con comparativa nacional
3. **Para distribución étnica**: Gráficos circulares o de anillos
4. **Para datos geográficos**: Mapas de calor o coropletas
5. **Para comparativas**: Gráficos de barras o columnas agrupadas

## Entrega Final

La entrega del tablero debe incluir:
1. El archivo .pbix del tablero
2. Un informe breve explicando las principales conclusiones
3. Instrucciones sobre cómo interactuar con el tablero
