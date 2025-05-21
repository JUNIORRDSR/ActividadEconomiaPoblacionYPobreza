# Guía para Crear el Tablero en Power BI

## Introducción

Esta guía proporciona instrucciones detalladas sobre cómo crear un tablero en Power BI utilizando los datos generados para el departamento de ANTIOQUIA, que incluyen proyecciones de población e indicadores de pobreza.

## Requisitos

- Power BI Desktop (Descargar desde [powerbi.microsoft.com](https://powerbi.microsoft.com) si aún no lo tiene instalado)
- Los archivos CSV generados en la carpeta `datos`

## Paso 1: Importar los Datos

1. Abrir Power BI Desktop
2. Seleccionar "Obtener datos" → "Texto/CSV"
3. Navegar hasta la carpeta `datos` y seleccionar los archivos CSV uno por uno (o seleccionar múltiples archivos manteniendo presionada la tecla Ctrl)
4. Para cada archivo:
   - Verificar que los tipos de datos se detecten correctamente
   - Usar "Transformar datos" si es necesario ajustar formatos
   - Seleccionar "Cargar" para importar los datos

## Paso 2: Organizar el Modelo de Datos

1. Ir a la vista "Modelo" (icono en la barra lateral izquierda)
2. Organizar las tablas para mejor visualización
3. Crear relaciones si es necesario (aunque en este caso, la mayoría de los análisis serán por separado)
4. Asegurarse de que los datos estén correctamente tipados:
   - Las columnas numéricas deben ser de tipo numérico
   - Las fechas y años deben ser de tipo fecha/año
   - Los porcentajes deben estar formateados como porcentajes

## Paso 3: Crear Medidas Calculadas (DAX)

Para enriquecer el análisis, puedes crear las siguientes medidas:

1. **Variación Anual de Pobreza Monetaria**:
   ```
   Variación IP = 
   VAR AñoActual = MAX('IP Act.Met._ANTIOQUIA'[Unnamed: 3])
   VAR AñoAnterior = AñoActual - 1
   VAR ValorActual = CALCULATE(SUM('IP Act.Met._ANTIOQUIA'[Unnamed: 3]), 'IP Act.Met._ANTIOQUIA'[Unnamed: 3] = AñoActual)
   VAR ValorAnterior = CALCULATE(SUM('IP Act.Met._ANTIOQUIA'[Unnamed: 3]), 'IP Act.Met._ANTIOQUIA'[Unnamed: 3] = AñoAnterior)
   RETURN
   DIVIDE(ValorActual - ValorAnterior, ValorAnterior, 0)
   ```

2. **Diferencia entre Pobreza Monetaria y Pobreza Extrema**:
   ```
   Diferencia IP-IPE = 
   CALCULATE(SUM('IP Act.Met._ANTIOQUIA'[Unnamed: 3])) - CALCULATE(SUM('IPE Act.Met._ANTIOQUIA'[Unnamed: 3]))
   ```

3. **Promedio de Coeficiente de Gini**:
   ```
   Promedio Gini = 
   AVERAGE('Gini_ANTIOQUIA'[Unnamed: 3])
   ```

## Paso 4: Diseñar el Tablero (5 Páginas)

### Página 1: Resumen Ejecutivo

1. Añadir un título: "Indicadores de Pobreza - ANTIOQUIA"
2. Añadir tarjetas para mostrar los valores más recientes de:
   - Incidencia de Pobreza Monetaria
   - Incidencia de Pobreza Monetaria Extrema
   - Coeficiente de Gini
   - Incidencia de Pobreza Multidimensional
3. Añadir gráfico de líneas para mostrar la tendencia de la incidencia de pobreza monetaria
4. Añadir gráfico de líneas para mostrar la tendencia de la pobreza multidimensional
5. Añadir segmentador de datos para filtrar por año

Ejemplo:
- Panel superior: Tarjetas con valores actuales
- Panel central: Gráficos de tendencia
- Panel inferior: Segmentadores de datos

### Página 2: Análisis de Pobreza Monetaria

1. Título: "Pobreza Monetaria - ANTIOQUIA"
2. Gráfico de líneas: Tendencia de Incidencia de Pobreza Monetaria (2018-2023)
3. Gráfico de líneas: Tendencia de Incidencia de Pobreza Monetaria Extrema (2018-2023)
4. Gráfico de barras comparativo: Pobreza Monetaria vs. Pobreza Monetaria Extrema por año
5. Gráfico de barras: Número de personas en situación de pobreza
6. Gráfico de líneas: Tendencia de la brecha y severidad de la pobreza
7. Tabla: Valores detallados de todos los indicadores de pobreza monetaria

### Página 3: Análisis de Pobreza Multidimensional

1. Título: "Pobreza Multidimensional - ANTIOQUIA"
2. Gráfico de líneas: Tendencia de Incidencia de Pobreza Multidimensional (2018-2024)
3. Gráfico de barras: Intensidad de la Pobreza Multidimensional
4. Gráfico de barras: Incidencia Ajustada de la Pobreza Multidimensional
5. Visualización de tabla de calor: Privaciones por variable (si están disponibles en los datos)
6. Gráfico circular: Distribución de contribuciones a la pobreza multidimensional (si están disponibles)

### Página 4: Análisis por Género

1. Título: "Pobreza por Género - ANTIOQUIA"
2. Gráfico de barras comparativo: Incidencia de Pobreza Monetaria por sexo
3. Gráfico de barras comparativo: Incidencia de Pobreza Monetaria Extrema por sexo
4. Gráfico de líneas: Tendencia de la brecha de género en pobreza monetaria
5. Gráfico de barras comparativo: Incidencia de Pobreza Multidimensional por sexo
6. Gráfico de barras comparativo: Incidencia de Pobreza Multidimensional por sexo del jefe de hogar

### Página 5: Proyecciones de Población

1. Título: "Proyecciones de Población - ANTIOQUIA"
2. Gráfico de líneas: Proyección de población total por año
3. Gráfico de barras: Distribución de población urbana/rural
4. Gráfico circular: Distribución por grupos étnicos
5. Tabla: Datos detallados de proyección de población

## Paso 5: Mejorar la Apariencia Visual

1. Seleccionar un tema coherente desde "Vista" → "Temas"
2. Usar una paleta de colores consistente para todos los gráficos
3. Añadir títulos descriptivos a cada visualización
4. Añadir etiquetas de datos donde sea útil
5. Incluir notas explicativas usando cuadros de texto
6. Añadir información sobre fuentes de datos

## Paso 6: Añadir Interactividad

1. Configurar filtros cruzados entre visualizaciones
2. Añadir botones de navegación entre páginas
3. Implementar información sobre herramientas (tooltips) personalizadas
4. Configurar acciones de obtención de detalles (drill-through) para ver más información

## Paso 7: Verificar y Finalizar

1. Probar todos los filtros y segmentadores
2. Verificar que todas las visualizaciones se actualicen correctamente
3. Comprobar que todos los indicadores solicitados estén incluidos
4. Guardar el archivo como `Tablero_Pobreza_ANTIOQUIA.pbix`

## Notas Importantes

- Los nombres de columnas en los CSV pueden no ser ideales (como "Unnamed: 1", "Unnamed: 2", etc.). Considera renombrarlas en Power BI para mayor claridad.
- Algunos archivos pueden requerir transformaciones adicionales antes de su uso.
- Si encuentras dificultades con algún indicador específico, consulta el archivo `resumen_analisis.json` para entender la estructura de los datos.

## Ejemplo de Visualización

A continuación se muestra un ejemplo de cómo podría verse la página de resumen:

```
+-------------------------------------------------------+
|                                                       |
|  INDICADORES DE POBREZA - ANTIOQUIA                   |
|                                                       |
+------------------------+----------------------------+--+
|                        |                            |  |
| Pobreza Monetaria:     | [Gráfico de tendencia de   |  |
| 24.3%                  | pobreza monetaria]         |  |
|                        |                            |  |
| Pobreza Extrema:       |                            |  |
| 5.7%                   |                            |  |
|                        |                            |  |
| Gini: 0.48             |                            |  |
|                        |                            |  |
+------------------------+----------------------------+--+
|                                                       |
| [Gráfico de tendencia de pobreza multidimensional]    |
|                                                       |
+-------------------------------------------------------+
|                                                       |
| Año: [Segmentador de datos] 2018 2019 2020 2021 2022  |
|                                                       |
+-------------------------------------------------------+
```

Con esta guía, podrás crear un tablero completo y profesional que muestre todos los indicadores solicitados para el departamento de ANTIOQUIA.
