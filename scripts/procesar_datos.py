import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import numpy as np

print("Iniciando análisis de datos para tablero de Power BI...")

# Definir rutas a los archivos
current_dir = os.getcwd()
file_pob = os.path.join(current_dir, 'anex-DCD-Proypoblacion-PerteneniaEtnicoRacialmun.xlsx')
file_pm = os.path.join(current_dir, 'anex-PM-Departamental-2023.xlsx')
file_pmd = os.path.join(current_dir, 'anex-PMultidimensional-Departamental-2024.xlsx')

print(f"Archivos a procesar:\n{file_pob}\n{file_pm}\n{file_pmd}")

# Crear directorio para datos procesados
output_dir = os.path.join(current_dir, 'datos')
os.makedirs(output_dir, exist_ok=True)
print(f"Directorio para datos procesados: {output_dir}")

# Función para mostrar las hojas de un archivo Excel
def show_excel_sheets(file_path):
    try:
        xl = pd.ExcelFile(file_path)
        print(f"Hojas en {os.path.basename(file_path)}:")
        for sheet in xl.sheet_names:
            print(f"  - {sheet}")
        return xl.sheet_names
    except Exception as e:
        print(f"Error al leer {file_path}: {e}")
        return None

# Mostrar las hojas disponibles en cada archivo
print("\n--- Estructura de los archivos ---")
sheets_pob = show_excel_sheets(file_pob)
sheets_pm = show_excel_sheets(file_pm)
sheets_pmd = show_excel_sheets(file_pmd)

# 1. Procesar datos de proyección de población
print("\n--- Procesando datos de población ---")
try:
    # Cargar datos de población
    df_pob_raw = pd.read_excel(file_pob, skiprows=10)
    print(f"Datos cargados con forma: {df_pob_raw.shape}")
    
    # Limpiar datos
    column_mapping = {
        'Unnamed: 0': 'COD_DPTO',
        'Unnamed: 1': 'DEPARTAMENTO',
        'Unnamed: 2': 'COD_DPTO-MPIO',
        'Unnamed: 3': 'MUNICIPIO',
        'Unnamed: 4': 'AÑO',
        'Unnamed: 5': 'ÁREA GEOGRÁFICA',
        'Unnamed: 6': 'Total',
        'Unnamed: 7': 'Indígena',
        'Unnamed: 8': 'Gitano(a) o Rrom',
        'Unnamed: 9': 'Raizal del Archipiélago de San Andrés, Providencia y Santa Catalina',
        'Unnamed: 10': 'Palenquero(a) de San Basilio',
        'Unnamed: 11': 'Negro(a), mulato(a), afrodescendiente, afrocolombiano(a)',
        'Unnamed: 12': 'Ningún grupo étnico-racial'
    }
    
    df_pob_clean = df_pob_raw.rename(columns=column_mapping)
    print("Columnas después de la limpieza:")
    print(df_pob_clean.columns.tolist())
    
    # Guardar una muestra de los datos para visualización
    pob_sample_file = os.path.join(output_dir, 'poblacion_muestra.csv')
    df_pob_clean.head(1000).to_csv(pob_sample_file, index=False)
    print(f"Muestra de datos de población guardada en: {pob_sample_file}")
    
    # Extraer lista de departamentos
    departamentos = df_pob_clean['DEPARTAMENTO'].unique().tolist()
    print(f"\nDepartamentos disponibles ({len(departamentos)}):")
    for i, dept in enumerate(sorted(departamentos), 1):
        print(f"{i}. {dept}")
    
    # Seleccionar un departamento para el análisis detallado
    # Para este ejemplo, usaremos Antioquia
    assigned_department = "Antioquia"
    print(f"\nDepartamento seleccionado para análisis: {assigned_department}")
    
    # Filtrar datos para el departamento asignado
    dept_pop = df_pob_clean[df_pob_clean['DEPARTAMENTO'] == assigned_department]
    print(f"Registros para {assigned_department}: {dept_pop.shape[0]}")
    
    # Guardar datos filtrados
    pop_output_file = os.path.join(output_dir, f'poblacion_{assigned_department}.csv')
    dept_pop.to_csv(pop_output_file, index=False)
    print(f"Datos de población para {assigned_department} guardados en: {pop_output_file}")
    
    # Crear visualización de población por año
    try:
        # Agrupar por año y sumar población total
        pop_by_year = dept_pop.groupby('AÑO')['Total'].sum().reset_index()
        
        # Crear gráfico
        plt.figure(figsize=(10, 6))
        plt.plot(pop_by_year['AÑO'], pop_by_year['Total'], marker='o', linestyle='-', linewidth=2)
        plt.title(f'Proyección de Población - {assigned_department}')
        plt.xlabel('Año')
        plt.ylabel('Población Total')
        plt.grid(True, linestyle='--', alpha=0.7)
        
        # Guardar gráfico
        pop_chart_file = os.path.join(output_dir, f'poblacion_proyeccion_{assigned_department}.png')
        plt.savefig(pop_chart_file)
        plt.close()
        print(f"Gráfico de proyección de población guardado en: {pop_chart_file}")
    except Exception as viz_error:
        print(f"Error al crear visualización de población: {viz_error}")
    
except Exception as e:
    print(f"Error al procesar datos de población: {e}")

# 2. Procesar datos de pobreza monetaria
print("\n--- Procesando datos de pobreza monetaria ---")
try:
    # Función para cargar indicadores
    def load_poverty_indicators(file_path, sheet_names):
        indicators = {}
        for sheet in sheet_names:
            if sheet != 'Índice':  # Omitir la hoja de índice
                try:
                    # Cargar cada hoja y guardarla en un diccionario
                    # Ajustar skiprows según sea necesario
                    df = pd.read_excel(file_path, sheet_name=sheet, skiprows=5)
                    # Limpiar el dataframe
                    df = df.dropna(how='all').dropna(how='all', axis=1)
                    indicators[sheet] = df
                    print(f"Cargado {sheet} con forma {df.shape}")
                except Exception as e:
                    print(f"Error al cargar {sheet}: {e}")
        return indicators
    
    # Cargar indicadores de pobreza monetaria
    pm_indicators = load_poverty_indicators(file_pm, sheets_pm)
    
    # Verificar si se cargaron los indicadores
    if pm_indicators and len(pm_indicators) > 0:
        print(f"Indicadores de pobreza monetaria cargados: {len(pm_indicators)}")
        
        # Para cada indicador, filtrar por departamento y guardar
        for indicator_name, df in pm_indicators.items():
            try:
                # Buscar columna de departamento
                potential_dept_cols = [col for col in df.columns if any(term in str(col).lower() for term in ['depart', 'dpto', 'entidad'])]
                
                if potential_dept_cols:
                    dept_col = potential_dept_cols[0]
                    print(f"\nProcesando indicador: {indicator_name}")
                    print(f"Columna de departamento identificada: {dept_col}")
                    
                    # Filtrar por departamento (usando contains para ser más flexible)
                    filtered_df = df[df[dept_col].str.contains(assigned_department, case=False, na=False)]
                    
                    if not filtered_df.empty:
                        print(f"Datos encontrados para {assigned_department}")
                        
                        # Guardar individualmente
                        indicator_file = os.path.join(output_dir, f'{indicator_name}_{assigned_department}.csv')
                        filtered_df.to_csv(indicator_file, index=False)
                        print(f"Indicador {indicator_name} guardado en: {indicator_file}")
                        
                        # Si hay columnas de años, crear visualización
                        year_cols = [col for col in filtered_df.columns if str(col).isdigit()]
                        if year_cols:
                            try:
                                # Crear gráfico
                                plt.figure(figsize=(10, 6))
                                plt.title(f'{indicator_name} - {assigned_department}')
                                
                                # Datos para gráfico
                                years = [int(col) for col in year_cols]
                                values = filtered_df[year_cols].values[0]
                                
                                if indicator_name in ['Gini']:
                                    # Gráfico de barras para Gini
                                    plt.bar(years, values, color='teal')
                                    plt.ylim(0, 1)  # Gini va de 0 a 1
                                else:
                                    # Gráfico de líneas para otros indicadores
                                    plt.plot(years, values, marker='o', linestyle='-', color='darkblue', linewidth=2)
                                
                                plt.grid(True, linestyle='--', alpha=0.7)
                                plt.xlabel('Año')
                                plt.ylabel('Valor')
                                plt.xticks(years)
                                
                                # Guardar gráfico
                                chart_file = os.path.join(output_dir, f'{indicator_name}_{assigned_department}.png')
                                plt.savefig(chart_file)
                                plt.close()
                                print(f"Gráfico de {indicator_name} guardado en: {chart_file}")
                            except Exception as viz_error:
                                print(f"Error al crear visualización para {indicator_name}: {viz_error}")
                    else:
                        print(f"No se encontraron datos para {assigned_department} en {indicator_name}")
                else:
                    print(f"No se pudo identificar columna de departamento en {indicator_name}")
            except Exception as ind_error:
                print(f"Error al procesar indicador {indicator_name}: {ind_error}")
    else:
        print("No se pudieron cargar correctamente los indicadores de pobreza monetaria")
except Exception as e:
    print(f"Error general al procesar pobreza monetaria: {e}")

# 3. Procesar datos de pobreza multidimensional
print("\n--- Procesando datos de pobreza multidimensional ---")
try:
    # Cargar indicadores de pobreza multidimensional
    pmd_indicators = load_poverty_indicators(file_pmd, sheets_pmd)
    
    # Verificar si se cargaron los indicadores
    if pmd_indicators and len(pmd_indicators) > 0:
        print(f"Indicadores de pobreza multidimensional cargados: {len(pmd_indicators)}")
        
        # Para cada indicador, filtrar por departamento y guardar
        for indicator_name, df in pmd_indicators.items():
            try:
                # Buscar columna de departamento
                potential_dept_cols = [col for col in df.columns if any(term in str(col).lower() for term in ['depart', 'dpto', 'entidad'])]
                
                if potential_dept_cols:
                    dept_col = potential_dept_cols[0]
                    print(f"\nProcesando indicador multidimensional: {indicator_name}")
                    print(f"Columna de departamento identificada: {dept_col}")
                    
                    # Filtrar por departamento (usando contains para ser más flexible)
                    filtered_df = df[df[dept_col].str.contains(assigned_department, case=False, na=False)]
                    
                    if not filtered_df.empty:
                        print(f"Datos encontrados para {assigned_department}")
                        
                        # Guardar individualmente
                        indicator_file = os.path.join(output_dir, f'{indicator_name}_{assigned_department}.csv')
                        filtered_df.to_csv(indicator_file, index=False)
                        print(f"Indicador {indicator_name} guardado en: {indicator_file}")
                        
                        # Si hay columnas de años, crear visualización
                        year_cols = [col for col in filtered_df.columns if str(col).isdigit()]
                        if year_cols:
                            try:
                                # Crear gráfico
                                plt.figure(figsize=(10, 6))
                                plt.title(f'{indicator_name} - {assigned_department}')
                                
                                # Datos para gráfico
                                years = [int(col) for col in year_cols]
                                values = filtered_df[year_cols].values[0]
                                
                                plt.plot(years, values, marker='s', linestyle='-', color='darkgreen', linewidth=2)
                                plt.grid(True, linestyle='--', alpha=0.7)
                                plt.xlabel('Año')
                                plt.ylabel('Valor')
                                plt.xticks(years)
                                
                                # Guardar gráfico
                                chart_file = os.path.join(output_dir, f'{indicator_name}_{assigned_department}.png')
                                plt.savefig(chart_file)
                                plt.close()
                                print(f"Gráfico de {indicator_name} guardado en: {chart_file}")
                            except Exception as viz_error:
                                print(f"Error al crear visualización para {indicator_name}: {viz_error}")
                    else:
                        print(f"No se encontraron datos para {assigned_department} en {indicator_name}")
                else:
                    print(f"No se pudo identificar columna de departamento en {indicator_name}")
            except Exception as ind_error:
                print(f"Error al procesar indicador {indicator_name}: {ind_error}")
    else:
        print("No se pudieron cargar correctamente los indicadores de pobreza multidimensional")
except Exception as e:
    print(f"Error general al procesar pobreza multidimensional: {e}")

# 4. Crear un resumen consolidado para Power BI
print("\n--- Creando resumen consolidado para Power BI ---")
try:
    # Crear un archivo JSON con metadatos del análisis
    import json
    
    metadata = {
        "fecha_analisis": pd.Timestamp.now().strftime("%Y-%m-%d"),
        "departamento_analizado": assigned_department,
        "archivos_procesados": [
            os.path.basename(file_pob),
            os.path.basename(file_pm),
            os.path.basename(file_pmd)
        ],
        "indicadores_disponibles": {
            "pobreza_monetaria": list(pm_indicators.keys()) if 'pm_indicators' in locals() else [],
            "pobreza_multidimensional": list(pmd_indicators.keys()) if 'pmd_indicators' in locals() else []
        },
        "archivos_generados": [f for f in os.listdir(output_dir) if f.endswith('.csv') or f.endswith('.png')],
        "recomendaciones_powerbi": [
            "Importar archivos CSV desde la carpeta 'datos'",
            "Crear relaciones entre tablas por departamento y año",
            "Usar visualizaciones de líneas para tendencias temporales",
            "Usar tarjetas para mostrar valores recientes",
            "Implementar filtros por año y área geográfica",
            "Estructurar el tablero en 5 páginas según las recomendaciones"
        ]
    }
    
    # Guardar metadatos
    metadata_file = os.path.join(output_dir, 'metadatos_analisis.json')
    with open(metadata_file, 'w', encoding='utf-8') as f:
        json.dump(metadata, f, indent=4, ensure_ascii=False)
    
    print(f"Metadatos del análisis guardados en: {metadata_file}")
    
    print("\nProceso de análisis completo. Los archivos generados están disponibles en la carpeta 'datos'.")
    print("Ahora puede importar estos archivos a Power BI para crear su tablero.")
    
except Exception as e:
    print(f"Error al crear resumen consolidado: {e}")
