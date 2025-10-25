"""Script para entrenar todos los modelos Prophet"""

import pandas as pd
from modelo import entrenar_modelo_prophet, guardar_modelo, calcular_metricas_accuracy
import numpy as np

def entrenar_todos():
    """Entrena modelos para todos los productos"""
    
    print("=" * 60)
    print("ENTRENAMIENTO DE MODELOS - NEXUS")
    print("=" * 60)
    
    # Cargar datos
    try:
        df = pd.read_csv('data/datos_historicos.csv')
        print(f"\n✓ Datos cargados: {len(df)} filas\n")
    except FileNotFoundError:
        print("\n❌ ERROR: No se encuentra data/datos_historicos.csv")
        print("Coloca el archivo CSV en la carpeta 'data/'\n")
        return
    
    # Convertir fecha a datetime
    df['fecha'] = pd.to_datetime(df['fecha'])
    
    # Identificar productos
    columnas_consumo = [col for col in df.columns if col.startswith('consumo_')]
    productos = [col.replace('consumo_', '') for col in columnas_consumo]
    
    print(f"Productos a entrenar: {len(productos)}")
    for prod in productos:
        print(f"  • {prod}")
    
    print("\n" + "=" * 60)
    
    # Entrenar cada modelo
    resultados = {}
    
    for i, producto in enumerate(productos, 1):
        print(f"\n[{i}/{len(productos)}] Entrenando: {producto}")
        print("-" * 60)
        
        try:
            # Entrenar modelo
            modelo = entrenar_modelo_prophet(df, producto, agregar_regresores=True)
            
            # Guardar modelo
            guardar_modelo(modelo, f'modelo_{producto}')
            
            # Validación simple (últimos 20% de datos)
            split_idx = int(len(df) * 0.8)
            df_train = df[:split_idx]
            df_test = df[split_idx:]
            
            # Calcular accuracy aproximado
            if len(df_test) > 0:
                col_consumo = f'consumo_{producto}'
                y_true = df_test[col_consumo].values
                y_pred = modelo.predict(modelo.history)['yhat'].values[-len(y_true):]
                
                # Asegurar misma longitud
                min_len = min(len(y_true), len(y_pred))
                y_true = y_true[:min_len]
                y_pred = y_pred[:min_len]
                
                metricas = calcular_metricas_accuracy(y_true, y_pred)
                resultados[producto] = metricas['Accuracy']
                
                print(f"  Accuracy: {metricas['Accuracy']:.1f}%")
            else:
                resultados[producto] = None
                print("  (No hay datos de validación)")
            
        except Exception as e:
            print(f"  ❌ ERROR: {str(e)}")
            resultados[producto] = None
    
    # Resumen final
    print("\n" + "=" * 60)
    print("RESUMEN DE ENTRENAMIENTO")
    print("=" * 60)
    
    for producto, accuracy in resultados.items():
        if accuracy:
            emoji = "🟢" if accuracy >= 85 else "🟡" if accuracy >= 70 else "🔴"
            print(f"{emoji} {producto:25s} → {accuracy:.1f}%")
        else:
            print(f"⚪ {producto:25s} → No evaluado")
    
    accuracy_promedio = np.mean([a for a in resultados.values() if a is not None])
    print(f"\n📊 Accuracy promedio: {accuracy_promedio:.1f}%")
    
    print("\n✓ Modelos guardados en carpeta 'models/'")
    print("=" * 60)
    print()


if __name__ == "__main__":
    entrenar_todos()
