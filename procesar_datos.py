"""
Procesar los datos históricos reales (615K registros) para el sistema NEXUS
"""

import pandas as pd
import numpy as np
from datetime import datetime
import os

def cargar_y_procesar_datos(archivo='data/datos_historicos.csv'):
    """
    Carga y procesa el archivo CSV de 615K registros
    
    Returns:
        DataFrame procesado y agrupado por vuelo
    """
    print("📊 Cargando datos históricos...")
    
    # Leer CSV con separador ; (punto y coma)
    df = pd.read_csv(archivo, sep=';', low_memory=False)
    
    print(f"✅ Cargados {len(df):,} registros")
    print(f"📋 Columnas: {list(df.columns)}")
    
    # Limpiar nombres de columnas (quitar espacios)
    df.columns = df.columns.str.strip()
    
    # Convertir fecha
    df['FECHA'] = pd.to_datetime(df['FECHA'], format='%d/%m/%Y', errors='coerce')
    
    # Crear ruta (ORIGEN-DESTINO)
    df['RUTA'] = df['ORIGEN'].astype(str) + '-' + df['DESTINO'].astype(str)
    
    print("\n📊 Estructura de datos:")
    print(f"  - Vuelos únicos: {df['FLIGHT KEY'].nunique():,}")
    print(f"  - Rutas únicas: {df['RUTA'].nunique():,}")
    print(f"  - Aerolíneas: {df['NOMBRE DE AEROLINEA'].nunique():,}")
    print(f"  - Categorías: {df['CATEGORY'].nunique()}")
    print(f"  - Supercategorías: {df['SUPERCATEGORY'].nunique()}")
    
    # Mostrar categorías disponibles
    print("\n🏷️ Categorías de productos:")
    categorias = df.groupby('CATEGORY')['SALES'].sum().sort_values(ascending=False)
    for cat, sales in categorias.head(15).items():
        print(f"  - {cat}: {int(sales):,} ventas")
    
    return df


def agrupar_por_vuelo(df):
    """
    Agrupa los datos por vuelo para obtener consumo total por categoría
    
    Returns:
        DataFrame con consumo agregado por vuelo
    """
    print("\n🔄 Agrupando datos por vuelo...")
    
    # Crear pivot table: cada fila = un vuelo, cada columna = categoría de producto
    vuelos = df.groupby(['FLIGHT KEY', 'RUTA', 'FECHA', 'PASSENGERS', 'ORIGEN', 'DESTINO']).agg({
        'SALES': 'sum',  # Total de ventas
        'CATEGORY': lambda x: x.value_counts().to_dict()  # Conteo por categoría
    }).reset_index()
    
    # Crear columnas separadas por categoría
    categorias_principales = [
        'Sweet Snacks', 'Cold Drink', 'Savoury Snacks', 'Alcohol',
        'Hot Drink', 'Sandwiches', 'Meal', 'Water'
    ]
    
    # Pivot para obtener ventas por categoría
    pivot = df.groupby(['FLIGHT KEY', 'CATEGORY'])['SALES'].sum().unstack(fill_value=0)
    
    # Merge con info del vuelo
    vuelos_info = df.groupby('FLIGHT KEY').agg({
        'PASSENGERS': 'first',
        'RUTA': 'first',
        'FECHA': 'first',
        'ORIGEN': 'first',
        'DESTINO': 'first',
        'FLIGHT NO': 'first'
    }).reset_index()
    
    resultado = vuelos_info.merge(pivot, on='FLIGHT KEY', how='left')
    resultado = resultado.fillna(0)
    
    print(f"✅ {len(resultado):,} vuelos únicos procesados")
    print(f"📊 Columnas de productos: {[col for col in resultado.columns if col not in ['FLIGHT KEY', 'PASSENGERS', 'RUTA', 'FECHA', 'ORIGEN', 'DESTINO', 'FLIGHT NO']]}")
    
    return resultado


def calcular_estadisticas_por_ruta(df_vuelos):
    """
    Calcula estadísticas de consumo por ruta
    
    Returns:
        DataFrame con promedios y desviaciones por ruta
    """
    print("\n📈 Calculando estadísticas por ruta...")
    
    # Columnas de productos
    cols_productos = [col for col in df_vuelos.columns 
                     if col not in ['FLIGHT KEY', 'PASSENGERS', 'RUTA', 'FECHA', 'ORIGEN', 'DESTINO', 'FLIGHT NO']]
    
    # Agrupar por ruta
    stats = df_vuelos.groupby('RUTA').agg({
        'PASSENGERS': ['mean', 'std', 'count'],
        **{col: ['mean', 'std', 'min', 'max'] for col in cols_productos}
    }).reset_index()
    
    # Aplanar columnas multi-nivel
    stats.columns = ['_'.join(col).strip('_') for col in stats.columns.values]
    
    print(f"✅ Estadísticas calculadas para {len(stats):,} rutas")
    
    return stats


def guardar_datos_procesados(df_vuelos, df_stats, carpeta='data'):
    """
    Guarda los datos procesados en archivos separados
    """
    print("\n💾 Guardando datos procesados...")
    
    # Guardar vuelos agregados
    archivo_vuelos = os.path.join(carpeta, 'vuelos_agregados.csv')
    df_vuelos.to_csv(archivo_vuelos, index=False)
    print(f"  ✅ Vuelos: {archivo_vuelos} ({len(df_vuelos):,} registros)")
    
    # Guardar estadísticas por ruta
    archivo_stats = os.path.join(carpeta, 'estadisticas_rutas.csv')
    df_stats.to_csv(archivo_stats, index=False)
    print(f"  ✅ Estadísticas: {archivo_stats} ({len(df_stats):,} rutas)")
    
    return archivo_vuelos, archivo_stats


if __name__ == "__main__":
    print("=" * 80)
    print("🚀 PROCESAMIENTO DE DATOS NEXUS")
    print("=" * 80)
    
    # 1. Cargar datos
    df = cargar_y_procesar_datos()
    
    # 2. Agrupar por vuelo
    df_vuelos = agrupar_por_vuelo(df)
    
    # 3. Calcular estadísticas
    df_stats = calcular_estadisticas_por_ruta(df_vuelos)
    
    # 4. Guardar
    guardar_datos_procesados(df_vuelos, df_stats)
    
    print("\n" + "=" * 80)
    print("✅ PROCESAMIENTO COMPLETADO")
    print("=" * 80)
    
    # Mostrar muestra de datos
    print("\n📊 Muestra de vuelos procesados:")
    print(df_vuelos.head(3).to_string())
    
    print("\n📈 Muestra de estadísticas por ruta:")
    print(df_stats.head(3).to_string())
