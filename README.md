# ✈️ NEXUS - Sistema de Predicción de Consumo de Catering

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.31-red.svg)
![Prophet](https://img.shields.io/badge/Prophet-ML-green.svg)

## 🎯 Descripción

NEXUS es un sistema inteligente de predicción de consumo para optimización de carga de catering en aviación. Resuelve el problema de que los vuelos regresan con 50%+ de ítems sin usar mediante:

- 🤖 **Machine Learning con Prophet** - Predicción granular por producto
- 📊 **Dashboard interactivo** - Visualización en tiempo real
- 💰 **Impacto multi-dimensional** - $$$, CO2, waste, combustible
- 🎮 **Gamificación** - Captura de datos mediante app móvil (concepto)

## 🚀 Instalación Rápida

```bash
# 1. Clonar repositorio
git clone https://github.com/ismamx3/HackMTY.git
cd HackMTY

# 2. Crear entorno virtual (recomendado)
python -m venv venv
venv\Scripts\activate     # Windows

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Colocar datos
# Pon tu CSV en: data/datos_historicos.csv
```

## 📊 Uso

```bash
# 1. Análisis exploratorio
python analisis_datos.py

# 2. Entrenar modelos
python entrenar_modelos.py

# 3. Ejecutar dashboard
streamlit run app.py
```

El dashboard se abrirá en: `http://localhost:8501`

## 📁 Estructura del Proyecto

```
HackMTY/
├── app.py                    # Dashboard Streamlit principal
├── modelo.py                 # Funciones ML (Prophet)
├── utils.py                  # Cálculos de impacto
├── analisis_datos.py         # Análisis exploratorio
├── entrenar_modelos.py       # Entrenamiento de modelos
├── requirements.txt          # Dependencias Python
├── .gitignore               # Archivos a ignorar
├── README.md                # Este archivo
├── data/                    # Datos CSV (agregar aquí)
│   └── datos_historicos.csv
├── models/                  # Modelos entrenados (.pkl)
└── outputs/                 # Gráficos generados
```

## 🎨 Características

### 1. Predicción Inteligente
- Modelos Prophet por producto
- Estacionalidad múltiple (semanal, anual)
- Intervalos de confianza
- Sistema de semáforos de confianza

### 2. Dashboard Multi-Tab
- **Tab 1 - Nueva Predicción**: Inputs de vuelo y recomendaciones
- **Tab 2 - Analytics**: Evolución del modelo y tendencias
- **Tab 3 - Leaderboard**: Sistema de gamificación para crew

### 3. Impacto Cuantificado
- 💵 Ahorro económico ($$$)
- ⚖️ Peso reducido (kg)
- ✈️ Combustible ahorrado (L)
- ♻️ Waste evitado (kg)
- 🌍 CO2 evitado (kg)
- 🌳 Árboles equivalentes

### 4. Closed-Loop Learning
- Re-entrenamiento automático nocturno
- Mejora continua sin intervención manual
- Tracking de accuracy por ruta y producto

## 🛠️ Tecnologías

- **Python 3.10+**
- **Streamlit** - Dashboard web interactivo
- **Prophet (Meta)** - Forecasting con ML
- **Plotly** - Gráficos interactivos
- **Pandas** - Manipulación de datos
- **Scikit-learn** - Métricas de ML

## 📝 Formato de Datos

El CSV en `data/datos_historicos.csv` debe contener:

```csv
fecha,ruta,pasajeros_total,pasajeros_business,duracion_horas,dia_semana,consumo_sandwiches_pollo,consumo_sandwiches_veggie,consumo_galletas,consumo_cafe,consumo_agua
2024-01-01,FRA-JFK,245,45,8.0,0,67,23,145,89,234
...
```

**Columnas requeridas:**
- `fecha`: Fecha del vuelo (YYYY-MM-DD)
- `ruta`: Código de ruta (ej: FRA-JFK)
- Columnas de consumo: `consumo_[producto]`

## 👥 Equipo

Desarrollado para **Hackathon GateGroup 2025**

## 📄 Licencia

MIT License

---

## 🚀 Quick Start para Hackathon

### Paso 1: Setup inicial
```powershell
git clone https://github.com/ismamx3/HackMTY.git
cd HackMTY
pip install -r requirements.txt
```

### Paso 2: Agregar datos
Coloca tu archivo CSV en `data/datos_historicos.csv`

### Paso 3: Entrenar
```powershell
python entrenar_modelos.py
```

### Paso 4: Ejecutar dashboard
```powershell
streamlit run app.py
```

### Paso 5: ¡Presentar! 🎤
Abre el navegador en `http://localhost:8501`

---

**¡Listo para ganar el hackathon! 🏆**
HackMTY, project made by:
Ismael Alvarez Rodriguez
Juan Pablo Garcia Villareal
Albert Gerardo Constantino
Daniel Gonzalez Morejon
