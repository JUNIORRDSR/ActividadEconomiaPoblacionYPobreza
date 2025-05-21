import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
import json
from datetime import datetime

print("Analizando estructura de archivos Excel para tablero de Power BI")

# Configurar visualización
plt.style.use('ggplot')
sns.set(font_scale=1.2)

# Definir rutas a los archivos
current_dir = os.getcwd()
file_pob = os.path.join(current_dir, 'anex-DCD-Proypoblacion-PerteneniaEtnicoRacialmun.xlsx')
file_pm = os.path.join(current_dir, 'anex-PM-Departamental-2023.xlsx')
file_pmd = os.path.join(current_dir, 'anex-PMultidimensional-Departamental-2024.xlsx')

# Crear directorio para datos procesados
output_dir = os.path.join(current_dir, 'datos')
os.makedirs(output_dir, exist_ok=True)
print(f"Directorio para datos procesados: {output_dir}")

# Departamento asignado (para este ejemplo)
department = "ANTIOQUIA"
print(f"Departamento seleccionado para análisis: {department}")

# 1. Examinar datos de población
print("\n--- Análisis de datos de población ---")
try:
    # Mostrar hojas disponibles
    xl_pop = pd.ExcelFile(file_pob)
    print(f"Hojas en archivo de población: {xl_pop.sheet_names}")
    
    # Intentar cargar con diferentes parámetros
    for skip in [0, 5, 10]:
        print(f"\nProbando carga con skiprows={skip}")
        df = pd.read_excel(file_pob, skiprows=skip)
        print(f"Forma: {df.shape}")
        print("Primeras columnas:")
        print(df.columns[:5].tolist())
        
    # Cargar los datos con estructura correcta
    df_pop = pd.read_excel(file_pob, skiprows=10)
    
    # Identificar columnas que contienen información de departamento
    dept_cols = [col for col in df_pop.columns if 'Unnamed: 1' == col]
    if not dept_cols:
        dept_cols = ['Unnamed: 1']  # Columna que normalmente contiene departamentos
        
    print(f"\nColumna de departamentos: {dept_cols}")
    
    # Valores únicos en la columna de departamento
    print("Algunos valores en la columna de departamento:")
    dept_values = df_pop[dept_cols[0]].unique()[:10]  # Mostrar algunos ejemplos
    print(dept_values)
    
    # Filtrar por departamento seleccionado
    dept_data = df_pop[df_pop[dept_cols[0]] == department]
    print(f"\nRegistros encontrados para {department}: {len(dept_data)}")
    
    # Guardar datos filtrados
    if not dept_data.empty:
        output_file = os.path.join(output_dir, f'poblacion_{department}.csv')
        dept_data.to_csv(output_file, index=False)
        print(f"Datos de población guardados en: {output_file}")
    
    # Crear una visualización
    if not dept_data.empty:
        try:
            # Intentar agrupar por año
            year_col = 'Unnamed: 4'  # Columna que normalmente contiene el año
            total_col = 'Unnamed: 6'  # Columna que normalmente contiene el total
            
            # Agrupar por año
            pop_by_year = dept_data.groupby(year_col)[total_col].sum().reset_index()
            
            # Crear gráfico
            plt.figure(figsize=(10, 6))
            plt.plot(pop_by_year[year_col], pop_by_year[total_col], marker='o', linewidth=2)
            plt.title(f'Población Total por Año - {department}')
            plt.xlabel('Año')
            plt.ylabel('Población Total')
            plt.grid(True, alpha=0.3)
            
            # Guardar gráfico
            chart_file = os.path.join(output_dir, f'poblacion_por_anio_{department}.png')
            plt.savefig(chart_file)
            plt.close()
            print(f"Gráfico de población guardado en: {chart_file}")
        except Exception as e:
            print(f"Error al crear visualización: {e}")
        
except Exception as e:
    print(f"Error al procesar datos de población: {e}")

# 2. Examinar datos de pobreza monetaria
print("\n--- Análisis de pobreza monetaria ---")
try:
    # Mostrar hojas disponibles
    xl_pm = pd.ExcelFile(file_pm)
    print(f"Hojas en archivo de pobreza monetaria: {xl_pm.sheet_names}")
    
    # Analizar estructura de cada hoja
    for sheet in xl_pm.sheet_names:
        if sheet != 'Índice':  # Omitir la hoja de índice
            print(f"\nAnalizando hoja: {sheet}")
            
            # Cargar hoja
            df = pd.read_excel(file_pm, sheet_name=sheet, nrows=10)  # Cargar primeras filas para inspección
            print(f"Forma: {df.shape}")
            
            # Intentar encontrar departamento ANTIOQUIA en las primeras filas
            found = False
            for i, row in df.iterrows():
                if any(str(val).upper() == department for val in row.values if pd.notna(val)):
                    print(f"Encontrado {department} en fila {i}")
                    found = True
                    break
            
            if not found:
                print(f"No se encontró {department} en las primeras filas. Verificando con más filas...")
                # Cargar más filas
                df_more = pd.read_excel(file_pm, sheet_name=sheet)
                
                # Buscar en todas las filas
                for i, row in df_more.iterrows():
                    if any(str(val).upper() == department for val in row.values if pd.notna(val)):
                        print(f"Encontrado {department} en fila {i}")
                        found = True
                        break
                
                if not found:
                    print(f"No se encontró {department} en la hoja {sheet}")
            
            # Intentar cargar datos desde la fila 5 (omitir encabezados)
            df_data = pd.read_excel(file_pm, sheet_name=sheet, skiprows=5)
            print(f"Datos desde fila 5. Forma: {df_data.shape}")
            print("Columnas disponibles:")
            print(df_data.columns.tolist()[:5])  # Mostrar primeras 5 columnas
            
            # Buscar columna que contiene departamentos
            dept_found = False
            for col in df_data.columns:
                col_vals = df_data[col].astype(str).str.upper()
                if department in col_vals.values:
                    print(f"Columna {col} contiene {department}")
                    dept_found = True
                    
                    # Filtrar por departamento
                    dept_rows = df_data[col_vals == department]
                    print(f"Filas para {department}: {len(dept_rows)}")
                    
                    # Guardar datos filtrados
                    if not dept_rows.empty:
                        output_file = os.path.join(output_dir, f'{sheet}_{department}.csv')
                        dept_rows.to_csv(output_file, index=False)
                        print(f"Datos de {sheet} guardados en: {output_file}")
                    
                    break
            
            if not dept_found:
                print(f"No se encontró {department} en ninguna columna")
    
except Exception as e:
    print(f"Error al procesar datos de pobreza monetaria: {e}")

# 3. Examinar datos de pobreza multidimensional
print("\n--- Análisis de pobreza multidimensional ---")
try:
    # Mostrar hojas disponibles
    xl_pmd = pd.ExcelFile(file_pmd)
    print(f"Hojas en archivo de pobreza multidimensional: {xl_pmd.sheet_names}")
    
    # Analizar estructura de cada hoja
    for sheet in xl_pmd.sheet_names:
        if sheet != 'Índice':  # Omitir la hoja de índice
            print(f"\nAnalizando hoja: {sheet}")
            
            # Cargar hoja
            df = pd.read_excel(file_pmd, sheet_name=sheet, nrows=10)  # Cargar primeras filas para inspección
            print(f"Forma: {df.shape}")
            
            # Intentar encontrar departamento ANTIOQUIA en las primeras filas
            found = False
            for i, row in df.iterrows():
                if any(str(val).upper() == department for val in row.values if pd.notna(val)):
                    print(f"Encontrado {department} en fila {i}")
                    found = True
                    break
            
            if not found:
                print(f"No se encontró {department} en las primeras filas. Verificando con más filas...")
                # Cargar más filas
                df_more = pd.read_excel(file_pmd, sheet_name=sheet)
                
                # Buscar en todas las filas
                for i, row in df_more.iterrows():
                    if any(str(val).upper() == department for val in row.values if pd.notna(val)):
                        print(f"Encontrado {department} en fila {i}")
                        found = True
                        break
                
                if not found:
                    print(f"No se encontró {department} en la hoja {sheet}")
            
            # Intentar cargar datos desde la fila 5 (omitir encabezados)
            df_data = pd.read_excel(file_pmd, sheet_name=sheet, skiprows=5)
            print(f"Datos desde fila 5. Forma: {df_data.shape}")
            print("Columnas disponibles:")
            print(df_data.columns.tolist()[:5])  # Mostrar primeras 5 columnas
            
            # Buscar columna que contiene departamentos
            dept_found = False
            for col in df_data.columns:
                col_vals = df_data[col].astype(str).str.upper()
                if department in col_vals.values:
                    print(f"Columna {col} contiene {department}")
                    dept_found = True
                    
                    # Filtrar por departamento
                    dept_rows = df_data[col_vals == department]
                    print(f"Filas para {department}: {len(dept_rows)}")
                    
                    # Guardar datos filtrados
                    if not dept_rows.empty:
                        output_file = os.path.join(output_dir, f'{sheet}_{department}.csv')
                        dept_rows.to_csv(output_file, index=False)
                        print(f"Datos de {sheet} guardados en: {output_file}")
                    
                    break
            
            if not dept_found:
                print(f"No se encontró {department} en ninguna columna")
                
except Exception as e:
    print(f"Error al procesar datos de pobreza multidimensional: {e}")

# 4. Crear archivos de resumen
print("\n--- Creando resumen de indicadores ---")
try:
    # Crear archivo de resumen con los indicadores solicitados
    indicators = [
        "Incidencia de Pobreza Multidimensional",
        "Incidencia de la Pobreza Monetaria",
        "Incidencia de la Pobreza Monetaria Extrema",
        "Personas en situación de Pobreza Monetaria",
        "Personas en situación de Pobreza Monetaria Extrema",
        "Coeficiente de Gini",
        "Promedio del Ingreso per cápita de la unidad de gasto de la población",
        "Líneas de Pobreza Monetaria",
        "Líneas de Pobreza Monetaria Extrema",
        "Brecha de la Pobreza Monetaria",
        "Brecha de la Pobreza Monetaria Extrema",
        "Severidad de la Pobreza Monetaria",
        "Severidad de la Pobreza Monetaria Extrema",
        "Incidencia de la Pobreza Monetaria según sexo de la persona",
        "Incidencia de la Pobreza Monetaria Extrema según sexo de la persona"
    ]
    
    # Correspondencia entre indicadores y hojas de Excel
    indicator_mapping = {
        "Incidencia de Pobreza Multidimensional": ["IPM_Departamentos"],
        "Incidencia de la Pobreza Monetaria": ["IP Act.Met."],
        "Incidencia de la Pobreza Monetaria Extrema": ["IPE Act.Met."],
        "Personas en situación de Pobreza Monetaria": ["AP Act.Met."],
        "Personas en situación de Pobreza Monetaria Extrema": ["APE Act.Met."],
        "Coeficiente de Gini": ["Gini"],
        "Promedio del Ingreso per cápita de la unidad de gasto de la población": ["IPUG"],
        "Líneas de Pobreza Monetaria": ["LP Act.Met."],
        "Líneas de Pobreza Monetaria Extrema": ["LPE Act.Met."],
        "Brecha de la Pobreza Monetaria": ["BP Act.Met."],
        "Brecha de la Pobreza Monetaria Extrema": ["BPE Act.Met."],
        "Severidad de la Pobreza Monetaria": ["SP Act.Met."],
        "Severidad de la Pobreza Monetaria Extrema": ["SPE Act.Met."],
        "Incidencia de la Pobreza Monetaria según sexo de la persona": ["IP_Sexo Act.Met."],
        "Incidencia de la Pobreza Monetaria Extrema según sexo de la persona": ["IPE_Sexo Act.Met."]
    }
    
    # Crear resumen de archivos generados
    generated_files = [f for f in os.listdir(output_dir) if os.path.isfile(os.path.join(output_dir, f))]
    
    # Crear un archivo de resumen para facilitar la importación a Power BI
    summary = {
        "departamento": department,
        "fecha_analisis": datetime.now().strftime("%Y-%m-%d"),
        "archivos_procesados": [
            os.path.basename(file_pob),
            os.path.basename(file_pm),
            os.path.basename(file_pmd)
        ],
        "archivos_generados": generated_files,
        "indicadores": indicators,
        "mapeo_indicadores_hojas": indicator_mapping,
        "recomendaciones": [
            "Importar todos los archivos CSV de la carpeta datos",
            "Crear relaciones entre tablas usando la columna de departamento",
            "Crear visualizaciones para cada indicador por año",
            "Organizar el tablero en 5 páginas según las instrucciones"
        ]
    }
    
    # Guardar el resumen
    summary_file = os.path.join(output_dir, 'resumen_analisis.json')
    with open(summary_file, 'w', encoding='utf-8') as f:
        json.dump(summary, f, indent=4, ensure_ascii=False)
    
    print(f"Resumen de análisis guardado en: {summary_file}")
    
    # Crear un archivo con instrucciones para Power BI
    instructions = f"""
    # Instrucciones para crear el Tablero de Power BI - {department}
    
    ## Archivos generados
    
    Se han generado {len(generated_files)} archivos en la carpeta 'datos', incluyendo:
    - Archivos CSV con datos filtrados por departamento para cada indicador
    - Visualizaciones de ejemplo en formato PNG
    - Un archivo de resumen en formato JSON
    
    ## Pasos para crear el Tablero
    
    1. Abrir Power BI Desktop
    2. Importar los archivos CSV desde la carpeta 'datos'
    3. Crear relaciones entre tablas según sea necesario
    4. Crear visualizaciones para cada uno de los indicadores
    5. Organizar el tablero en 5 páginas según se indica en las instrucciones
    
    ## Indicadores a incluir
    
    {chr(10).join(f"- {ind}" for ind in indicators)}
    
    ## Sugerencias de visualización
    
    - Usar gráficos de líneas para tendencias temporales
    - Usar tarjetas para mostrar valores actuales
    - Usar gráficos de barras para comparaciones
    - Incluir filtros por año y otras variables relevantes
    
    ## Notas importantes
    
    - Asegurarse de incluir todos los indicadores solicitados
    - Mantener una estética consistente en todo el tablero
    - Incluir títulos descriptivos en todas las visualizaciones
    """
    
    # Guardar las instrucciones
    instructions_file = os.path.join(output_dir, 'instrucciones_powerbi.txt')
    with open(instructions_file, 'w', encoding='utf-8') as f:
        f.write(instructions)
    
    print(f"Instrucciones para Power BI guardadas en: {instructions_file}")
    
except Exception as e:
    print(f"Error al crear resumen: {e}")

print("\nProceso de análisis completado. Los archivos generados están disponibles en la carpeta 'datos'.")
print("Ahora puede crear su tablero en Power BI siguiendo las instrucciones proporcionadas.")
