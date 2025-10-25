"""Utilidades y cálculos de impacto"""

import pandas as pd
import numpy as np
from typing import Dict

# Costos y pesos por producto
PRODUCTOS_INFO = {
    'sandwiches_pollo': {'costo': 8.50, 'peso_g': 180, 'perecedero': True},
    'sandwiches_veggie': {'costo': 7.80, 'peso_g': 160, 'perecedero': True},
    'galletas': {'costo': 2.50, 'peso_g': 60, 'perecedero': False},
    'cafe': {'costo': 3.50, 'peso_g': 280, 'perecedero': False},
    'agua': {'costo': 1.50, 'peso_g': 500, 'perecedero': False},
}

def calcular_impacto(cantidad_ahorrada: Dict[str, float], vuelo_info: Dict) -> Dict:
    """
    Calcula impacto multi-dimensional
    
    Args:
        cantidad_ahorrada: {'sandwiches_pollo': 23, 'galletas': 55, ...}
        vuelo_info: {'duracion_horas': 8.0, 'pasajeros': 245}
    
    Returns:
        {
            'ahorro_dinero': float,
            'peso_reducido_kg': float,
            'combustible_ahorrado_litros': float,
            'waste_evitado_kg': float,
            'co2_evitado_kg': float,
            'arboles_equivalentes': float
        }
    """
    ahorro_dinero = 0.0
    peso_reducido_g = 0.0
    waste_evitado_g = 0.0
    
    for producto, cantidad in cantidad_ahorrada.items():
        if producto in PRODUCTOS_INFO:
            info = PRODUCTOS_INFO[producto]
            ahorro_dinero += cantidad * info['costo']
            peso_reducido_g += cantidad * info['peso_g']
            if info['perecedero']:
                waste_evitado_g += cantidad * info['peso_g']
    
    peso_reducido_kg = peso_reducido_g / 1000.0
    waste_evitado_kg = waste_evitado_g / 1000.0
    
    # Fórmula aeronáutica: cada kg = 0.003 L fuel/hora
    duracion = vuelo_info.get('duracion_horas', 8.0)
    combustible_litros = peso_reducido_kg * 0.003 * duracion
    
    # 1L jet fuel = 2.5 kg CO2
    co2_kg = combustible_litros * 2.5
    
    # 1 árbol captura ~22 kg CO2/año
    arboles = co2_kg / 22.0
    
    return {
        'ahorro_dinero': round(ahorro_dinero, 2),
        'peso_reducido_kg': round(peso_reducido_kg, 2),
        'combustible_ahorrado_litros': round(combustible_litros, 2),
        'waste_evitado_kg': round(waste_evitado_kg, 2),
        'co2_evitado_kg': round(co2_kg, 2),
        'arboles_equivalentes': round(arboles, 2)
    }


def generar_explicacion(ruta: str, hora: str, consumo_historico: float, 
                       confidence: float, num_vuelos: int) -> str:
    """Genera explicación en lenguaje natural"""
    
    hora_num = int(hora.split(':')[0])
    
    if 6 <= hora_num <= 9:
        periodo = "matutino (alta demanda de café)"
    elif 12 <= hora_num <= 14:
        periodo = "mediodía (pico de comidas)"
    elif 20 <= hora_num <= 23:
        periodo = "nocturno (más snacks)"
    else:
        periodo = "moderado"
    
    texto = f"""
**Análisis basado en:**

- 📊 Consumo histórico promedio en ruta {ruta}: **{consumo_historico:.0f}%**
- ⏰ Horario de salida ({hora}): período **{periodo}**
- 📈 Basado en **{num_vuelos} vuelos similares** en últimos 90 días
- 🎯 Nivel de confianza: **{confidence:.0f}%**

{'✅ **Muy confiable** - puede proceder sin revisión' if confidence >= 95 else 
 '⚠️ **Confianza media** - revisión recomendada' if confidence >= 75 else 
 '🔴 **Baja confianza** - requiere validación manual'}
"""
    return texto


def obtener_semaforo(confidence: float) -> tuple:
    """Retorna (emoji, color, mensaje) según confianza"""
    if confidence >= 95:
        return ("🟢", "green", "Alta confianza")
    elif confidence >= 75:
        return ("🟡", "orange", "Confianza media")
    else:
        return ("🔴", "red", "Requiere revisión")
