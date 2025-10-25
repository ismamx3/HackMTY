"""Funciones de Machine Learning con Prophet"""

import pandas as pd
import numpy as np
from prophet import Prophet
import pickle
import os
from typing import Dict, Tuple

def preparar_datos_prophet(df: pd.DataFrame, columna_producto: str) -> pd.DataFrame:
    """
    Prepara datos para Prophet (requiere columnas 'ds' y 'y')
    
    Args:
        df: DataFrame con datos históricos
        columna_producto: nombre de columna (ej: 'consumo_sandwiches_pollo')
    
    Returns:
        DataFrame con columnas 'ds' (fecha) y 'y' (valor)
    """
    # Asegurar que existe columna de fecha
    if 'fecha' not in df.columns:
        raise ValueError("DataFrame debe tener columna 'fecha'")
    
    # Crear dataframe para Prophet
    df_prophet = pd.DataFrame({
        'ds': pd.to_datetime(df['fecha']),
        'y': df[columna_producto]
    })
    
    # Eliminar nulos
    df_prophet = df_prophet.dropna()
    
    # Ordenar por fecha
    df_prophet = df_prophet.sort_values('ds')
    
    return df_prophet


def entrenar_modelo_prophet(df: pd.DataFrame, nombre_producto: str, 
                           agregar_regresores: bool = True) -> Prophet:
    """
    Entrena modelo Prophet para un producto específico
    
    Args:
        df: DataFrame original con todas las columnas
        nombre_producto: nombre del producto (ej: 'sandwiches_pollo')
        agregar_regresores: si añadir features adicionales
    
    Returns:
        Modelo Prophet entrenado
    """
    # Preparar datos
    columna_consumo = f'consumo_{nombre_producto}'
    df_prophet = preparar_datos_prophet(df, columna_consumo)
    
    # Si hay regresores adicionales, añadirlos
    if agregar_regresores:
        if 'pasajeros_business' in df.columns:
            df_prophet['pasajeros_business'] = df['pasajeros_business'].values[:len(df_prophet)]
        
        if 'duracion_horas' in df.columns:
            df_prophet['duracion_horas'] = df['duracion_horas'].values[:len(df_prophet)]
    
    # Crear y configurar modelo
    modelo = Prophet(
        yearly_seasonality=True,
        weekly_seasonality=True,
        daily_seasonality=False,
        seasonality_mode='multiplicative',
        interval_width=0.8
    )
    
    # Añadir regresores si existen
    if agregar_regresores:
        if 'pasajeros_business' in df_prophet.columns:
            modelo.add_regressor('pasajeros_business')
        if 'duracion_horas' in df_prophet.columns:
            modelo.add_regressor('duracion_horas')
    
    # Entrenar
    print(f"Entrenando modelo para {nombre_producto}...")
    modelo.fit(df_prophet)
    
    return modelo


def predecir_consumo(modelo: Prophet, fecha_futura: pd.Timestamp, 
                     features: Dict = None) -> Dict:
    """
    Hace predicción para una fecha futura
    
    Args:
        modelo: modelo Prophet entrenado
        fecha_futura: fecha para predecir
        features: dict con regresores {'pasajeros_business': 45, 'duracion_horas': 8}
    
    Returns:
        {
            'prediccion': float,
            'lower': float,
            'upper': float,
            'confidence_score': int (0-100)
        }
    """
    # Crear dataframe futuro
    future_df = pd.DataFrame({'ds': [fecha_futura]})
    
    # Añadir regresores si los hay
    if features:
        for key, value in features.items():
            future_df[key] = value
    
    # Predecir
    forecast = modelo.predict(future_df)
    
    # Extraer valores
    prediccion = forecast['yhat'].values[0]
    lower = forecast['yhat_lower'].values[0]
    upper = forecast['yhat_upper'].values[0]
    
    # Calcular confidence score (inverso del ancho del intervalo)
    ancho_intervalo = (upper - lower) / prediccion if prediccion > 0 else 1.0
    confidence_score = max(0, min(100, 100 - (ancho_intervalo * 50)))
    
    return {
        'prediccion': max(0, round(prediccion)),
        'lower': max(0, round(lower)),
        'upper': max(0, round(upper)),
        'confidence_score': round(confidence_score)
    }


def guardar_modelo(modelo: Prophet, nombre_archivo: str):
    """Guarda modelo en archivo pickle"""
    os.makedirs('models', exist_ok=True)
    ruta = os.path.join('models', f'{nombre_archivo}.pkl')
    with open(ruta, 'wb') as f:
        pickle.dump(modelo, f)
    print(f"✓ Modelo guardado: {ruta}")


def cargar_modelo(nombre_archivo: str) -> Prophet:
    """Carga modelo desde archivo pickle"""
    ruta = os.path.join('models', f'{nombre_archivo}.pkl')
    if not os.path.exists(ruta):
        raise FileNotFoundError(f"No se encuentra el modelo: {ruta}")
    
    with open(ruta, 'rb') as f:
        modelo = pickle.load(f)
    return modelo


def calcular_metricas_accuracy(y_true: np.ndarray, y_pred: np.ndarray) -> Dict:
    """Calcula métricas de error del modelo"""
    mae = np.mean(np.abs(y_true - y_pred))
    mape = np.mean(np.abs((y_true - y_pred) / y_true)) * 100
    rmse = np.sqrt(np.mean((y_true - y_pred) ** 2))
    
    return {
        'MAE': round(mae, 2),
        'MAPE': round(mape, 2),
        'RMSE': round(rmse, 2),
        'Accuracy': round(100 - mape, 2)
    }
