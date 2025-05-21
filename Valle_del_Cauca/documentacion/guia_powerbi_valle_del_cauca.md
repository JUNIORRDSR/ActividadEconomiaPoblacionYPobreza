# Guía para importar datos a Power BI y crear el tablero del Valle del Cauca

## Paso 1: Preparación de archivos

### Estructura de archivos
Todos los datos necesarios se encuentran en la carpeta `Valle_del_Cauca`. Asegúrate de tener los siguientes archivos CSV:

- `pobreza_multidimensional_consolidado_valle_del_cauca.csv` - Datos principales de IPM 
- `IPM_Departamentos_valle_del_cauca.csv` - Comparativa entre departamentos
- `IPM_Variables_Departamento_valle_del_cauca.csv` - Desglose por variables
- `IPM_Sexo_valle_del_cauca.csv` - Análisis por género
- `IPM_Sexo Jefe_valle_del_cauca.csv` - Análisis por género de jefe de hogar
- `Intensidad_IPM_valle_del_cauca.csv` - Datos de intensidad de pobreza
- `Incidencia_Ajustada_IPM_valle_del_cauca.csv` - Incidencia ajustada
- `IC_IPM_Sexo_valle_del_cauca.csv` - Intervalos de confianza por género
- `IC_IPM_Sexo Jefe_valle_del_cauca.csv` - Intervalos de confianza por género de jefe

## Paso 2: Importación de datos a Power BI

1. Abre Power BI Desktop
2. Selecciona "Obtener datos" > "Texto/CSV"
3. Navega hasta la carpeta `Valle_del_Cauca` y selecciona el archivo `pobreza_multidimensional_consolidado_valle_del_cauca.csv`
4. En la ventana de vista previa, verifica que:
   - El delimitador sea "," (coma)
   - La primera fila se utilice como encabezado
   - Los tipos de datos se detecten correctamente (numéricos y texto)
5. Haz clic en "Cargar"
6. Repite los pasos 2-5 para cada uno de los archivos CSV listados arriba

## Paso 3: Transformación de datos

1. Ve a "Transformar datos" para abrir el Editor de Power Query
2. Para cada tabla:
   - Verifica los tipos de datos y corrige si es necesario
   - Elimina columnas innecesarias
   - Renombra columnas para mayor claridad
   - Crea columnas calculadas si se requiere

Transformaciones específicas recomendadas:

### Para IPM_Departamentos_valle_del_cauca
```
// Convertir valores de porcentaje a números decimales
= Table.TransformColumns(#"Tipo cambiado", {{"Valor", each _ / 100, type number}})
```

### Para datos temporales
```
// Crear columna de fecha completa
= Table.AddColumn(#"Columnas reordenadas", "Fecha", each Date.FromText(Text.From([Año]) & "/01/01"), type date)
```

## Paso 4: Creación del modelo de datos

1. Establece relaciones entre tablas:
   - Relaciona todas las tablas IPM por el campo "Año"
   - Crea una tabla de calendario si es necesario para análisis temporales

2. Crea medidas calculadas:
   ```
   // Variación anual IPM
   Var_IPM = 
   CALCULATE(
       ([IPM Actual] - [IPM Año Anterior]) / [IPM Año Anterior],
       FILTER(ALL('Tiempo'), 'Tiempo'[Año] = MAX('Tiempo'[Año]))
   )
   ```

## Paso 5: Diseño del tablero

### Página 1: Visión general
- Tarjetas con KPIs principales
- Gráfico de líneas con evolución del IPM
- Mapa del Valle del Cauca con indicadores por municipio
- Segmentaciones por año

### Página 2: Pobreza Multidimensional
- Gráfico de radar con 5 dimensiones principales
- Diagrama de barras con privaciones específicas
- Comparativa urbano/rural
- Matriz de correlación entre variables

### Página 3: Análisis Demográfico
- Pirámide poblacional
- Distribución por grupos étnicos
- Proyecciones hasta 2035
- Comparativa por género

### Página 4: Análisis Regional
- Mapa de Colombia destacando Valle del Cauca
- Comparativa con departamentos vecinos
- Ranking nacional de indicadores
- Matriz de dispersión IPM vs otras variables

## Paso 6: Personalización visual

1. Paleta de colores recomendada:
   - Azul principal: #1a5276 (Valle del Cauca)
   - Rojo comparativo: #c0392b (Nacional)
   - Verdes/naranjas para categorías

2. Elementos de marca:
   - Incluir escudo del Valle del Cauca en la cabecera
   - Mantener tipografía consistente (Segoe UI)
   - Agregar pie de página con fuentes de datos

## Paso 7: Publicación y compartir

1. Guarda el archivo como `Tablero_Valle_del_Cauca.pbix`
2. Publica en Power BI Service (si tienes cuenta)
3. Configura actualización programada si es necesario
4. Genera PDF para compartir versión estática

## Recursos adicionales

- Plantillas de Power BI específicas para análisis socioeconómico: [Microsoft AppSource](https://appsource.microsoft.com/es-es/marketplace/apps?product=power-bi)
- Documentación oficial de Power BI: [Microsoft Learn](https://learn.microsoft.com/es-es/power-bi/)
- Galería de visualizaciones personalizadas: [Power BI Visuals](https://powerbi.microsoft.com/es-es/visuals/)
