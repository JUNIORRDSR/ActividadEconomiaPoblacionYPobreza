"""
Script para generar visualizaciones para el Valle del Cauca basadas en los datos procesados.
Este script crea gráficos específicos para el análisis de pobreza en el Valle del Cauca.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import numpy as np
from matplotlib.ticker import PercentFormatter

# Configuración de estilo
plt.style.use('seaborn-v0_8-whitegrid')
sns.set(font_scale=1.2)
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.family'] = 'sans-serif'

# Definir directorios
current_dir = os.getcwd()
data_dir = os.path.join(current_dir, 'datos_valle')
vis_dir = os.path.join(current_dir, 'visualizaciones_valle')

# Crear directorio de visualizaciones si no existe
if not os.path.exists(vis_dir):
    os.makedirs(vis_dir)
    print(f"Directorio creado: {vis_dir}")

# Definir paleta de colores
colors = sns.color_palette("viridis", 10)
main_color = colors[3]  # Color principal para Valle del Cauca
comparison_color = colors[0]  # Color para comparaciones

# 1. Visualización de Pobreza Multidimensional
try:
    # Cargar datos de IPM
    ipm_file = os.path.join(data_dir, 'IPM_Departamentos_valle_del_cauca.csv')
    if os.path.exists(ipm_file):
        ipm_df = pd.read_csv(ipm_file)
        
        # Identificar columnas de años y departamento
        dept_col = [col for col in ipm_df.columns if any(term in col.lower() for term in ['depart', 'dpto', 'entidad'])][0]
        year_cols = [col for col in ipm_df.columns if col.isdigit()]
        
        if year_cols:
            # Preparar datos para el gráfico
            years = [int(col) for col in year_cols]
            valle_values = ipm_df[year_cols].values[0]
            
            # Crear gráfico
            plt.figure(figsize=(12, 7))
            plt.title('Índice de Pobreza Multidimensional - Valle del Cauca', fontsize=16, pad=20)
            
            plt.plot(years, valle_values, marker='o', markersize=10, linewidth=3, 
                     color=main_color, label='Valle del Cauca')
            
            # Añadir etiquetas de valores
            for i, val in enumerate(valle_values):
                plt.text(years[i], val + 0.8, f'{val:.1f}%', ha='center', fontsize=12, fontweight='bold')
            
            # Formatear ejes
            plt.xlabel('Año', fontsize=14)
            plt.ylabel('Incidencia (%)', fontsize=14)
            plt.xticks(years, fontsize=12)
            plt.yticks(fontsize=12)
            plt.grid(True, linestyle='--', alpha=0.7)
            
            # Guardar
            plt.savefig(os.path.join(vis_dir, 'pobreza_multidimensional_valle.png'), 
                        bbox_inches='tight', dpi=300)
            plt.close()
            print("Visualización de pobreza multidimensional creada")
    else:
        print(f"No se encontró el archivo: {ipm_file}")
except Exception as e:
    print(f"Error al crear visualización de pobreza multidimensional: {e}")

# 2. Visualización por Sexo del Jefe de Hogar
try:
    # Cargar datos de IPM por sexo
    ipm_sexo_file = os.path.join(data_dir, 'IPM_Sexo_valle_del_cauca.csv')
    if os.path.exists(ipm_sexo_file):
        ipm_sexo_df = pd.read_csv(ipm_sexo_file)
        
        # Identificar columnas relevantes
        cols = ipm_sexo_df.columns
        year_cols = [col for col in cols if col.isdigit()]
        sexo_cols = [col for col in cols if any(term in col.lower() for term in ['hombre', 'mujer', 'sexo'])]
        
        if year_cols and len(ipm_sexo_df) >= 2:
            # Preparar datos - asumiendo que las primeras filas son hombre/mujer
            years = [int(col) for col in year_cols]
            
            # Extraer datos (ajustar según estructura real)
            if 'Sexo' in cols:
                hombres_df = ipm_sexo_df[ipm_sexo_df['Sexo'].str.contains('Hombre', case=False)]
                mujeres_df = ipm_sexo_df[ipm_sexo_df['Sexo'].str.contains('Mujer', case=False)]
            else:
                # Si no hay columna específica, asumimos orden
                hombres_df = ipm_sexo_df.iloc[0:1]
                mujeres_df = ipm_sexo_df.iloc[1:2]
            
            if not hombres_df.empty and not mujeres_df.empty:
                hombres_values = hombres_df[year_cols].values[0]
                mujeres_values = mujeres_df[year_cols].values[0]
                
                # Crear gráfico
                plt.figure(figsize=(14, 8))
                plt.title('Pobreza Multidimensional por Sexo del Jefe de Hogar - Valle del Cauca', 
                          fontsize=16, pad=20)
                
                # Ancho de las barras
                bar_width = 0.35
                index = np.arange(len(years))
                
                # Gráfico de barras
                plt.bar(index - bar_width/2, hombres_values, bar_width, 
                        color=colors[2], label='Hombres')
                plt.bar(index + bar_width/2, mujeres_values, bar_width, 
                        color=colors[5], label='Mujeres')
                
                # Añadir etiquetas de valores
                for i, val in enumerate(hombres_values):
                    plt.text(i - bar_width/2, val + 0.5, f'{val:.1f}%', 
                             ha='center', fontsize=11)
                
                for i, val in enumerate(mujeres_values):
                    plt.text(i + bar_width/2, val + 0.5, f'{val:.1f}%', 
                             ha='center', fontsize=11)
                
                # Formatear ejes
                plt.xlabel('Año', fontsize=14)
                plt.ylabel('Incidencia (%)', fontsize=14)
                plt.xticks(index, years, fontsize=12)
                plt.yticks(fontsize=12)
                plt.grid(True, linestyle='--', alpha=0.7, axis='y')
                plt.legend(fontsize=12, loc='upper right')
                
                # Guardar
                plt.savefig(os.path.join(vis_dir, 'pobreza_sexo_valle.png'), 
                            bbox_inches='tight', dpi=300)
                plt.close()
                print("Visualización por sexo creada")
    else:
        print(f"No se encontró el archivo: {ipm_sexo_file}")
except Exception as e:
    print(f"Error al crear visualización por sexo: {e}")

# 3. Visualización de Dimensiones de Pobreza
try:
    # Cargar datos de variables de pobreza
    ipm_vars_file = os.path.join(data_dir, 'IPM_Variables_Departamento _valle_del_cauca.csv')
    if os.path.exists(ipm_vars_file):
        ipm_vars_df = pd.read_csv(ipm_vars_file)
        
        # Buscar el año más reciente
        years = [col for col in ipm_vars_df.columns if col.isdigit()]
        if years:
            latest_year = max(years)
            
            # Extraer nombres de variables y valores para el año más reciente
            variable_col = [col for col in ipm_vars_df.columns if any(term in col.lower() for term in ['variable', 'privación', 'dimension'])][0]
            variables = ipm_vars_df[variable_col].tolist()
            values = ipm_vars_df[latest_year].tolist()
            
            # Seleccionar las primeras 15 variables (para no saturar el gráfico)
            if len(variables) > 15:
                variables = variables[:15]
                values = values[:15]
            
            # Crear gráfico de barras horizontales
            plt.figure(figsize=(14, 10))
            plt.title(f'Dimensiones de Pobreza Multidimensional - Valle del Cauca ({latest_year})', 
                      fontsize=16, pad=20)
            
            # Ordenar de mayor a menor
            sorted_indices = np.argsort(values)[::-1]
            sorted_vars = [variables[i] for i in sorted_indices]
            sorted_vals = [values[i] for i in sorted_indices]
            
            # Crear barras horizontales
            bars = plt.barh(range(len(sorted_vars)), sorted_vals, color=colors)
            
            # Añadir etiquetas de valores
            for i, bar in enumerate(bars):
                width = bar.get_width()
                plt.text(width + 0.5, bar.get_y() + bar.get_height()/2, 
                         f'{width:.1f}%', va='center', fontsize=11)
            
            # Formatear ejes
            plt.xlabel('Porcentaje (%)', fontsize=14)
            plt.yticks(range(len(sorted_vars)), sorted_vars, fontsize=11)
            plt.xticks(fontsize=12)
            plt.grid(True, linestyle='--', alpha=0.7, axis='x')
            
            # Ajustar diseño
            plt.tight_layout()
            
            # Guardar
            plt.savefig(os.path.join(vis_dir, 'dimensiones_pobreza_valle.png'), 
                        bbox_inches='tight', dpi=300)
            plt.close()
            print("Visualización de dimensiones de pobreza creada")
    else:
        print(f"No se encontró el archivo: {ipm_vars_file}")
except Exception as e:
    print(f"Error al crear visualización de dimensiones: {e}")

# 4. Comparativa Nacional (si hay datos disponibles)
try:
    # Cargar datos de IPM departamental
    ipm_file = os.path.join(data_dir, 'IPM_Departamentos_valle_del_cauca.csv')
    
    # Buscar datos nacionales en los originales
    national_data_file = os.path.join(current_dir, 'anex-PMultidimensional-Departamental-2024.xlsx')
    
    if os.path.exists(ipm_file) and os.path.exists(national_data_file):
        # Cargar datos del Valle
        valle_df = pd.read_csv(ipm_file)
        
        # Cargar datos nacionales
        try:
            national_df = pd.read_excel(national_data_file, sheet_name='IPM_Departamentos', skiprows=5)
            national_df = national_df.dropna(how='all').dropna(how='all', axis=1)
            
            # Buscar fila del total nacional
            dept_col = [col for col in national_df.columns if any(term in str(col).lower() for term in ['depart', 'dpto', 'entidad'])][0]
            national_row = national_df[national_df[dept_col].str.contains('Nacional', case=False, na=False)]
            
            if not national_row.empty:
                # Identificar columnas de años
                year_cols = [col for col in valle_df.columns if col.isdigit()]
                
                if year_cols:
                    # Extraer valores
                    years = [int(col) for col in year_cols]
                    valle_values = valle_df[year_cols].values[0]
                    
                    # Extraer valores nacionales para los mismos años
                    national_values = []
                    for year in year_cols:
                        if year in national_row.columns:
                            national_values.append(national_row[year].values[0])
                        else:
                            national_values.append(None)
                    
                    # Crear gráfico comparativo
                    plt.figure(figsize=(14, 8))
                    plt.title('Pobreza Multidimensional: Valle del Cauca vs Nacional', 
                              fontsize=16, pad=20)
                    
                    # Graficar líneas
                    plt.plot(years, valle_values, marker='o', markersize=10, linewidth=3, 
                             color=main_color, label='Valle del Cauca')
                    plt.plot(years, national_values, marker='s', markersize=8, linewidth=3, 
                             color=comparison_color, label='Total Nacional')
                    
                    # Añadir etiquetas
                    for i, val in enumerate(valle_values):
                        plt.text(years[i], val + 0.7, f'{val:.1f}%', ha='center', fontsize=11)
                    
                    for i, val in enumerate(national_values):
                        if val is not None:
                            plt.text(years[i], val - 0.7, f'{val:.1f}%', ha='center', fontsize=11)
                    
                    # Formatear ejes
                    plt.xlabel('Año', fontsize=14)
                    plt.ylabel('Incidencia (%)', fontsize=14)
                    plt.xticks(years, fontsize=12)
                    plt.yticks(fontsize=12)
                    plt.grid(True, linestyle='--', alpha=0.7)
                    plt.legend(fontsize=12, loc='upper right')
                    
                    # Guardar
                    plt.savefig(os.path.join(vis_dir, 'comparativa_nacional_valle.png'), 
                                bbox_inches='tight', dpi=300)
                    plt.close()
                    print("Visualización comparativa nacional creada")
        except Exception as e:
            print(f"Error al procesar datos nacionales: {e}")
    else:
        print("No se encontraron archivos necesarios para la comparativa nacional")
except Exception as e:
    print(f"Error al crear visualización comparativa: {e}")

print("Proceso de generación de visualizaciones completado.")
