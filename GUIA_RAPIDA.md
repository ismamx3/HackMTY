# 🚀 GUÍA RÁPIDA - NEXUS

## ⚡ Setup en 3 minutos

### 1️⃣ Instalar dependencias
```powershell
pip install -r requirements.txt
```

**Nota:** Si Prophet da error, instala primero:
```powershell
pip install pystan
pip install prophet
```

### 2️⃣ Preparar datos

Opción A - **Usar datos de ejemplo:**
```powershell
# Ya hay un archivo de ejemplo en data/datos_historicos_ejemplo.csv
# Cópialo como datos_historicos.csv
Copy-Item data\datos_historicos_ejemplo.csv data\datos_historicos.csv
```

Opción B - **Usar tus propios datos:**
- Coloca tu CSV en `data/datos_historicos.csv`
- Debe tener estas columnas:
  - `fecha`, `ruta`, `pasajeros_total`, `pasajeros_business`, `duracion_horas`, `dia_semana`
  - `consumo_sandwiches_pollo`, `consumo_sandwiches_veggie`, `consumo_galletas`, `consumo_cafe`, `consumo_agua`

### 3️⃣ Explorar datos (opcional)
```powershell
python analisis_datos.py
```
Esto genera gráficos en `outputs/`

### 4️⃣ Entrenar modelos (opcional para demo)
```powershell
python entrenar_modelos.py
```
**Nota:** Puedes saltarte esto para la demo, el dashboard funciona con valores simulados.

### 5️⃣ Ejecutar dashboard
```powershell
streamlit run app.py
```

Se abrirá automáticamente en: `http://localhost:8501`

---

## 📱 Cómo usar el Dashboard

### Tab 1: Nueva Predicción
1. Llena los datos del vuelo (número, ruta, fecha, hora, pasajeros)
2. Ajusta la duración del vuelo
3. Click en **"GENERAR PREDICCIÓN"**
4. ¡Listo! Verás:
   - Tabla con recomendaciones vs método estándar
   - Explicación del análisis
   - Impacto económico y ambiental
   - Botones para exportar/compartir

### Tab 2: Analytics
- Evolución del accuracy del modelo
- Top rutas con mejor rendimiento
- Precisión por tipo de producto

### Tab 3: Leaderboard
- Sistema de gamificación para crew
- Rankings y premios
- Mockups de la app móvil

---

## 🎤 Tips para la Presentación

1. **Abre el dashboard ANTES de presentar**
2. **Ten un vuelo de ejemplo listo:**
   - Vuelo: LH123
   - Ruta: FRA-JFK
   - Pasajeros: 245 (45 business)
   - Duración: 8h
3. **Muestra el flujo completo:**
   - Input → Predicción → Impacto → Export
4. **Destaca los números:**
   - Ahorro de dinero
   - Reducción de CO2
   - Waste evitado
5. **Menciona la gamificación** (Tab 3)

---

## ❓ Troubleshooting

### Prophet no se instala
```powershell
pip install pystan==2.19.1.1
pip install prophet
```

### Streamlit no abre automáticamente
Abre manualmente: `http://localhost:8501`

### "No se encuentra el CSV"
Verifica que existe: `data/datos_historicos.csv`

### Modelos no cargan
El dashboard funciona sin modelos entrenados (usa valores simulados para demo)

---

## 🏆 Checklist Pre-Presentación

- [ ] Dependencies instaladas (`pip install -r requirements.txt`)
- [ ] CSV en `data/datos_historicos.csv`
- [ ] Dashboard corriendo (`streamlit run app.py`)
- [ ] Browser abierto en `http://localhost:8501`
- [ ] Vuelo de ejemplo preparado
- [ ] Pantalla compartida lista
- [ ] Pitch ensayado (3-5 min)

---

## 📊 Estructura de Archivos

```
HackMTY/
├── app.py                 # 👈 EJECUTA ESTE para el dashboard
├── modelo.py              # Funciones ML
├── utils.py               # Cálculos
├── analisis_datos.py      # EDA
├── entrenar_modelos.py    # Training
├── requirements.txt       # Dependencias
├── data/
│   ├── datos_historicos_ejemplo.csv  # Datos de ejemplo
│   └── datos_historicos.csv          # 👈 TUS DATOS AQUÍ
├── models/                # Modelos entrenados
└── outputs/               # Gráficos
```

---

## 💡 Comandos Útiles

```powershell
# Instalar todo
pip install -r requirements.txt

# Correr dashboard
streamlit run app.py

# Análisis de datos
python analisis_datos.py

# Entrenar modelos
python entrenar_modelos.py

# Ver estructura de carpetas
tree /F

# Limpiar cache de Streamlit
streamlit cache clear
```

---

**¡Éxito en el hackathon! 🚀**