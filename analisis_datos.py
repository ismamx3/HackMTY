"""Script de análisis exploratorio de datos"""

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os

def analizar_datos(ruta_csv: str = 'data/datos_historicos.csv'):
    """
    Realiza análisis exploratorio completo
    """
    print("=" * 60)
    print("ANÁLISIS EXPLORATORIO DE DATOS - NEXUS")
    print("=" * 60)
    
    # Cargar datos
    try:
        df = pd.read_csv(ruta_csv)
        print(f"\n✓ Datos cargados: {len(df)} filas\n")
    except FileNotFoundError:
        print(f"\n❌ ERROR: No se encuentra {ruta_csv}")
        print("Coloca el archivo CSV en la carpeta 'data/'\n")
        return
    
    # Información básica
    print("COLUMNAS DISPONIBLES:")
    print("-" * 60)
    for i, col in enumerate(df.columns, 1):
        print(f"{i}. {col}")
    
    print("\n" + "=" * 60)
    print("PRIMERAS 5 FILAS:")
    print("=" * 60)
    print(df.head())
    
    print("\n" + "=" * 60)
    print("INFORMACIÓN DE TIPOS DE DATOS:")
    print("=" * 60)
    print(df.info())
    
    print("\n" + "=" * 60)
    print("ESTADÍSTICAS DESCRIPTIVAS:")
    print("=" * 60)
    print(df.describe())
    
    print("\n" + "=" * 60)
    print("VALORES NULOS:")
    print("=" * 60)
    print(df.isnull().sum())
    
    # Crear carpeta outputs
    os.makedirs('outputs', exist_ok=True)
    
    # GRÁFICO 1: Consumo por producto en el tiempo
    print("\n📊 Generando gráfico de tendencias...")
    
    columnas_consumo = [col for col in df.columns if col.startswith('consumo_')]
    
    if columnas_consumo and 'fecha' in df.columns:
        df_melted = df.melt(id_vars=['fecha'], value_vars=columnas_consumo,
                           var_name='Producto', value_name='Consumo')
        df_melted['Producto'] = df_melted['Producto'].str.replace('consumo_', '')
        
        fig1 = px.line(df_melted, x='fecha', y='Consumo', color='Producto',
                      title='Evolución de Consumo por Producto')
        fig1.write_html('outputs/tendencia_consumo.html')
        print("  ✓ Guardado: outputs/tendencia_consumo.html")
    
    # GRÁFICO 2: Consumo promedio por ruta
    if 'ruta' in df.columns and columnas_consumo:
        print("\n📊 Generando gráfico por ruta...")
        
        df_rutas = df.groupby('ruta')[columnas_consumo].mean().reset_index()
        df_rutas_melted = df_rutas.melt(id_vars=['ruta'], value_vars=columnas_consumo,
                                        var_name='Producto', value_name='Consumo_Promedio')
        df_rutas_melted['Producto'] = df_rutas_melted['Producto'].str.replace('consumo_', '')
        
        fig2 = px.bar(df_rutas_melted, x='ruta', y='Consumo_Promedio', color='Producto',
                     title='Consumo Promedio por Ruta', barmode='group')
        fig2.write_html('outputs/consumo_por_ruta.html')
        print("  ✓ Guardado: outputs/consumo_por_ruta.html")
    
    # GRÁFICO 3: Distribución por día de semana
    if 'dia_semana' in df.columns and columnas_consumo:
        print("\n📊 Generando gráfico por día de semana...")
        
        dias_nombres = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
        
        # Tomar primer producto como ejemplo
        producto_ejemplo = columnas_consumo[0]
        
        df_temp = df.copy()
        df_temp['dia_nombre'] = df_temp['dia_semana'].map(lambda x: dias_nombres[int(x)] if pd.notna(x) and 0 <= int(x) <= 6 else 'Desconocido')
        
        fig3 = px.box(df_temp, x='dia_nombre', y=producto_ejemplo,
                     title=f'Distribución de Consumo por Día de Semana ({producto_ejemplo.replace("consumo_", "")})')
        fig3.write_html('outputs/consumo_dia_semana.html')
        print("  ✓ Guardado: outputs/consumo_dia_semana.html")
    
    # INSIGHTS AUTOMÁTICOS
    print("\n" + "=" * 60)
    print("💡 INSIGHTS AUTOMÁTICOS:")
    print("=" * 60)
    
    if 'ruta' in df.columns and columnas_consumo:
        for producto in columnas_consumo[:3]:  # Primeros 3 productos
            ruta_max = df.groupby('ruta')[producto].mean().idxmax()
            valor_max = df.groupby('ruta')[producto].mean().max()
            print(f"\n{producto.replace('consumo_', '').upper()}:")
            print(f"  → Ruta con mayor consumo: {ruta_max} ({valor_max:.1f} unidades promedio)")
    
    if 'pasajeros_total' in df.columns and columnas_consumo:
        correlaciones = df[columnas_consumo + ['pasajeros_total']].corr()['pasajeros_total']
        print(f"\n📈 CORRELACIÓN CON NÚMERO DE PASAJEROS:")
        for prod in columnas_consumo[:3]:
            corr = correlaciones[prod]
            print(f"  → {prod.replace('consumo_', '')}: {corr:.2f}")
    
    print("\n" + "=" * 60)
    print("✓ ANÁLISIS COMPLETO")
    print("=" * 60)
    print("\nRevisa los gráficos generados en la carpeta 'outputs/'")
    print()


if __name__ == "__main__":
    analizar_datos()
