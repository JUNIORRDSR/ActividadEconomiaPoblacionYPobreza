import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import numpy as np

# Configurar visualización
plt.style.use('ggplot')
sns.set(font_scale=1.2)
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['axes.grid'] = True

# Definir directorio de datos
current_dir = os.getcwd()
data_dir = os.path.join(current_dir, 'datos')
output_dir = os.path.join(current_dir, 'visualizaciones')
os.makedirs(output_dir, exist_ok=True)

print("Creando visualizaciones de ejemplo para Power BI...")

# Cargar datos de pobreza monetaria
try:
    # Incidencia de Pobreza Monetaria
    ip_file = os.path.join(data_dir, 'IP Act.Met._ANTIOQUIA.csv')
    if os.path.exists(ip_file):
        df_ip = pd.read_csv(ip_file)
        print(f"Datos cargados: {ip_file}")
        print(f"Columnas: {df_ip.columns.tolist()}")
        
        # Renombrar columnas para mejor claridad
        df_ip.columns = ['Indicador', 'Desconocido', '2022', '2023']
        
        # Crear gráfico
        plt.figure(figsize=(10, 6))
        plt.plot(['2022', '2023'], [df_ip['2022'].iloc[0], df_ip['2023'].iloc[0]], 
                marker='o', linewidth=2, color='#1f77b4')
        plt.title('Incidencia de Pobreza Monetaria - ANTIOQUIA', fontsize=16)
        plt.ylabel('Porcentaje (%)', fontsize=14)
        plt.xlabel('Año', fontsize=14)
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.tight_layout()
        
        # Guardar gráfico
        output_file = os.path.join(output_dir, 'pobreza_monetaria.png')
        plt.savefig(output_file)
        plt.close()
        print(f"Gráfico guardado: {output_file}")
    
    # Incidencia de Pobreza Monetaria Extrema
    ipe_file = os.path.join(data_dir, 'IPE Act.Met._ANTIOQUIA.csv')
    if os.path.exists(ipe_file):
        df_ipe = pd.read_csv(ipe_file)
        df_ipe.columns = ['Indicador', 'Desconocido', '2022', '2023']
        
        # Crear gráfico
        plt.figure(figsize=(10, 6))
        plt.plot(['2022', '2023'], [df_ipe['2022'].iloc[0], df_ipe['2023'].iloc[0]], 
                marker='o', linewidth=2, color='#d62728')
        plt.title('Incidencia de Pobreza Monetaria Extrema - ANTIOQUIA', fontsize=16)
        plt.ylabel('Porcentaje (%)', fontsize=14)
        plt.xlabel('Año', fontsize=14)
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.tight_layout()
        
        # Guardar gráfico
        output_file = os.path.join(output_dir, 'pobreza_monetaria_extrema.png')
        plt.savefig(output_file)
        plt.close()
        print(f"Gráfico guardado: {output_file}")
    
    # Gráfico comparativo de Pobreza Monetaria y Extrema
    if os.path.exists(ip_file) and os.path.exists(ipe_file):
        plt.figure(figsize=(10, 6))
        
        # Crear barras agrupadas
        bar_width = 0.35
        years = ['2022', '2023']
        index = np.arange(len(years))
        
        plt.bar(index, [df_ip['2022'].iloc[0], df_ip['2023'].iloc[0]], 
                bar_width, label='Pobreza Monetaria', color='#1f77b4')
        plt.bar(index + bar_width, [df_ipe['2022'].iloc[0], df_ipe['2023'].iloc[0]], 
                bar_width, label='Pobreza Monetaria Extrema', color='#d62728')
        
        plt.title('Comparativa de Pobreza Monetaria - ANTIOQUIA', fontsize=16)
        plt.ylabel('Porcentaje (%)', fontsize=14)
        plt.xlabel('Año', fontsize=14)
        plt.xticks(index + bar_width/2, years)
        plt.legend()
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.tight_layout()
        
        # Guardar gráfico
        output_file = os.path.join(output_dir, 'comparativa_pobreza.png')
        plt.savefig(output_file)
        plt.close()
        print(f"Gráfico guardado: {output_file}")
    
    # Coeficiente de Gini
    gini_file = os.path.join(data_dir, 'Gini_ANTIOQUIA.csv')
    if os.path.exists(gini_file):
        df_gini = pd.read_csv(gini_file)
        df_gini.columns = ['Indicador', 'Desconocido', '2022', '2023']
        
        # Crear gráfico
        plt.figure(figsize=(10, 6))
        plt.bar(['2022', '2023'], [df_gini['2022'].iloc[0], df_gini['2023'].iloc[0]], 
                color=['#2ca02c', '#ff7f0e'])
        plt.title('Coeficiente de Gini - ANTIOQUIA', fontsize=16)
        plt.ylabel('Valor', fontsize=14)
        plt.xlabel('Año', fontsize=14)
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.ylim(0, 1)  # Gini va de 0 a 1
        plt.tight_layout()
        
        # Guardar gráfico
        output_file = os.path.join(output_dir, 'gini.png')
        plt.savefig(output_file)
        plt.close()
        print(f"Gráfico guardado: {output_file}")
    
    # Pobreza por género
    ip_sexo_file = os.path.join(data_dir, 'IP_Sexo Act.Met._ANTIOQUIA.csv')
    if os.path.exists(ip_sexo_file):
        df_ip_sexo = pd.read_csv(ip_sexo_file)
        # Asumiendo estructura específica basada en la exploración previa
        # Ajustar según sea necesario después de examinar los datos reales
        try:
            df_ip_sexo.columns = ['Indicador', 'Desconocido', '2022_H', '2022_M', '2023_H', '2023_M', 'Desconocido2']
            
            # Crear gráfico
            plt.figure(figsize=(10, 6))
            
            # Datos para el gráfico
            years = ['2022', '2023']
            hombres = [df_ip_sexo['2022_H'].iloc[0], df_ip_sexo['2023_H'].iloc[0]]
            mujeres = [df_ip_sexo['2022_M'].iloc[0], df_ip_sexo['2023_M'].iloc[0]]
            
            # Crear barras agrupadas
            bar_width = 0.35
            index = np.arange(len(years))
            
            plt.bar(index, hombres, bar_width, label='Hombres', color='#1f77b4')
            plt.bar(index + bar_width, mujeres, bar_width, label='Mujeres', color='#d62728')
            
            plt.title('Incidencia de Pobreza Monetaria por Sexo - ANTIOQUIA', fontsize=16)
            plt.ylabel('Porcentaje (%)', fontsize=14)
            plt.xlabel('Año', fontsize=14)
            plt.xticks(index + bar_width/2, years)
            plt.legend()
            plt.grid(True, linestyle='--', alpha=0.7)
            plt.tight_layout()
            
            # Guardar gráfico
            output_file = os.path.join(output_dir, 'pobreza_por_sexo.png')
            plt.savefig(output_file)
            plt.close()
            print(f"Gráfico guardado: {output_file}")
        except Exception as e:
            print(f"Error al procesar datos de pobreza por sexo: {e}")
    
    # Pobreza multidimensional
    ipm_file = os.path.join(data_dir, 'IPM_Departamentos_ANTIOQUIA.csv')
    if os.path.exists(ipm_file):
        df_ipm = pd.read_csv(ipm_file)
        print(f"Datos cargados: {ipm_file}")
        print(f"Columnas IPM: {df_ipm.columns.tolist()}")
        
        # Intentar crear un gráfico con los datos disponibles
        try:
            # Identificar columnas numéricas (probablemente años)
            numeric_cols = [col for col in df_ipm.columns if col.isdigit() or 
                            (isinstance(col, str) and col.replace('.', '').isdigit())]
            
            if numeric_cols:
                print(f"Columnas numéricas identificadas: {numeric_cols}")
                
                # Extraer los valores para el gráfico
                years = sorted(numeric_cols)
                values = [df_ipm[year].iloc[0] if year in df_ipm.columns else np.nan for year in years]
                
                # Crear gráfico
                plt.figure(figsize=(12, 6))
                plt.plot(years, values, marker='o', linewidth=2, color='#9467bd')
                plt.title('Incidencia de Pobreza Multidimensional - ANTIOQUIA', fontsize=16)
                plt.ylabel('Porcentaje (%)', fontsize=14)
                plt.xlabel('Año', fontsize=14)
                plt.grid(True, linestyle='--', alpha=0.7)
                plt.xticks(rotation=45)
                plt.tight_layout()
                
                # Guardar gráfico
                output_file = os.path.join(output_dir, 'pobreza_multidimensional.png')
                plt.savefig(output_file)
                plt.close()
                print(f"Gráfico guardado: {output_file}")
            else:
                print("No se encontraron columnas numéricas en los datos de IPM")
        except Exception as e:
            print(f"Error al crear gráfico de pobreza multidimensional: {e}")
    
    # Crear un mock-up del tablero completo
    plt.figure(figsize=(15, 10))
    
    # Configurar grid para el layout
    gs = plt.GridSpec(3, 2, height_ratios=[1, 2, 2])
    
    # Título principal
    plt.figtext(0.5, 0.95, 'TABLERO DE INDICADORES DE POBREZA - ANTIOQUIA', 
                fontsize=20, ha='center', va='center', weight='bold')
    
    # Tarjetas de indicadores clave
    ax1 = plt.subplot(gs[0, 0])
    ax1.axis('off')
    if os.path.exists(ip_file):
        valor_pobreza = df_ip['2023'].iloc[0]
        ax1.text(0.5, 0.7, f"Pobreza Monetaria", fontsize=14, ha='center', weight='bold')
        ax1.text(0.5, 0.35, f"{valor_pobreza:.1f}%", fontsize=18, ha='center', color='#1f77b4')
    
    ax2 = plt.subplot(gs[0, 1])
    ax2.axis('off')
    if os.path.exists(gini_file):
        valor_gini = df_gini['2023'].iloc[0]
        ax2.text(0.5, 0.7, f"Coeficiente de Gini", fontsize=14, ha='center', weight='bold')
        ax2.text(0.5, 0.35, f"{valor_gini:.3f}", fontsize=18, ha='center', color='#ff7f0e')
    
    # Gráfico de tendencia de pobreza monetaria
    ax3 = plt.subplot(gs[1, 0])
    if os.path.exists(ip_file) and os.path.exists(ipe_file):
        ax3.bar(['2022 PM', '2023 PM'], [df_ip['2022'].iloc[0], df_ip['2023'].iloc[0]], color='#1f77b4')
        ax3.bar(['2022 PE', '2023 PE'], [df_ipe['2022'].iloc[0], df_ipe['2023'].iloc[0]], color='#d62728')
        ax3.set_title('Pobreza Monetaria vs. Extrema', fontsize=12)
        ax3.set_ylabel('Porcentaje (%)')
        ax3.grid(True, linestyle='--', alpha=0.3)
    
    # Gráfico de pobreza por género
    ax4 = plt.subplot(gs[1, 1])
    if os.path.exists(ip_sexo_file):
        try:
            ax4.bar(['H 2022', 'M 2022', 'H 2023', 'M 2023'], 
                   [df_ip_sexo['2022_H'].iloc[0], df_ip_sexo['2022_M'].iloc[0], 
                    df_ip_sexo['2023_H'].iloc[0], df_ip_sexo['2023_M'].iloc[0]], 
                   color=['#1f77b4', '#d62728', '#1f77b4', '#d62728'])
            ax4.set_title('Pobreza por Género', fontsize=12)
            ax4.set_ylabel('Porcentaje (%)')
            ax4.grid(True, linestyle='--', alpha=0.3)
        except Exception as e:
            print(f"Error al crear gráfico de pobreza por género en el mockup: {e}")
    
    # Gráfico de tendencia de Gini
    ax5 = plt.subplot(gs[2, 0])
    if os.path.exists(gini_file):
        ax5.plot(['2022', '2023'], [df_gini['2022'].iloc[0], df_gini['2023'].iloc[0]], 
                marker='o', linewidth=2, color='#ff7f0e')
        ax5.set_title('Tendencia del Coeficiente de Gini', fontsize=12)
        ax5.set_ylabel('Valor')
        ax5.grid(True, linestyle='--', alpha=0.3)
        ax5.set_ylim(0, 1)  # Gini va de 0 a 1
    
    # Gráfico de pobreza multidimensional
    ax6 = plt.subplot(gs[2, 1])
    ax6.text(0.5, 0.5, "Gráfico de Pobreza Multidimensional\n(Datos disponibles en archivos)", 
             ha='center', va='center', fontsize=12)
    ax6.axis('off')
    
    plt.tight_layout(rect=[0, 0, 1, 0.95])  # Ajustar layout dejando espacio para título
    
    # Guardar mockup
    output_file = os.path.join(output_dir, 'mockup_tablero.png')
    plt.savefig(output_file, dpi=150)
    plt.close()
    print(f"Mockup del tablero guardado en: {output_file}")
    
except Exception as e:
    print(f"Error al crear visualizaciones: {e}")

print("Proceso de creación de visualizaciones completado.")
print(f"Las visualizaciones están disponibles en: {output_dir}")
