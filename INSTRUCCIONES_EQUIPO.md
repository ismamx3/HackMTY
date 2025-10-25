# 👥 INSTRUCCIONES PARA EL EQUIPO - NEXUS

## 🚀 CÓMO OBTENER TODO EL PROYECTO

### **1. Hacer git pull (si ya tienen el repo clonado):**
```powershell
cd ruta\a\HackMTY
git pull
```

### **2. O clonar desde cero:**
```powershell
git clone https://github.com/ismamx3/HackMTY.git
cd HackMTY
```

---

## 📦 LO QUE VAN A OBTENER

### **Archivos principales:**
- ✅ `app.py` - Dashboard con **tema futurista negro/azul** y **datos reales del CSV**
- ✅ `modelo.py` - Funciones ML (Prophet)
- ✅ `utils.py` - Cálculos de impacto
- ✅ `analisis_datos.py` - Análisis exploratorio
- ✅ `entrenar_modelos.py` - Entrenamiento de modelos
- ✅ `requirements.txt` - Todas las dependencias

### **Documentación completa:**
- 📖 `README.md` - Documentación principal
- 📖 `COMO_FUNCIONA_NEXUS.md` - ⭐ Explicación técnica completa
- 📖 `PRUEBAS_EXTREMAS.md` - ⭐ 8 casos de prueba extremos
- 📖 `ACTUALIZACION_DATOS_REALES.md` - ⭐ Cómo se usan los 615K registros
- 📖 `INSTRUCCIONES_EQUIPO.md` - Este archivo

### **Datos (615K registros REALES):**
- � `data/datos_historicos.csv` (86.6 MB) - 615,791 registros originales
- ✅ `data/vuelos_agregados.csv` (5.22 MB) - 46,655 vuelos procesados
- ✅ `data/estadisticas_rutas.csv` (0.14 MB) - 356 rutas con estadísticas

### **Carpetas:**
- 📁 `models/` - Para modelos entrenados
- 📁 `outputs/` - Para gráficos generados

---

## ⚙️ SETUP RÁPIDO (3 MINUTOS)

### **Paso 1: Instalar dependencias**
```powershell
# Si tienen Python instalado
pip install -r requirements.txt
```

### **Paso 2: Ejecutar el dashboard**
```powershell
# Opción A: Con ruta completa (siempre funciona)
C:\ruta\a\HackMTY\.venv\Scripts\streamlit.exe run app.py

# Opción B: Activar entorno y ejecutar
.\.venv\Scripts\Activate.ps1
streamlit run app.py
```

### **Paso 3: Abrir en navegador**
```
http://localhost:8501
http://localhost:8502
http://localhost:8503
```
(Puede ser cualquiera de estos puertos)

---

## 🎨 NUEVAS CARACTERÍSTICAS

### **1. Tema Futurista ⭐**
- 🖤 Fondo negro con gradientes azul oscuro
- 💙 Efectos de neón azul cian (#00d4ff)
- ✨ Animación shimmer en el título
- 🌟 Efectos glow en tarjetas y botones
- 💫 Partículas flotantes de fondo
- 🎭 Hover effects suaves
- 🔮 Glass morphism en componentes

### **2. Datos Reales del CSV ⭐**
- ✅ Lee `data/datos_historicos.csv`
- ✅ Filtra por ruta específica
- ✅ Calcula promedios históricos
- ✅ Ajusta por factores:
  - 👥 Número de pasajeros
  - ⏱️ Duración del vuelo
  - 🎩 Composición de clases (business/económica)
- ✅ Muestra número de vuelos históricos analizados

### **3. Pruebas Extremas Validadas ⭐**
- 🧪 50 pasajeros
- 🚀 1000 pasajeros
- 🛫 1500 pasajeros
- ⏱️ 1 hora - 16 horas
- 🎩 0% - 100% business class
- 🌍 Rutas con/sin datos históricos

---

## 📊 CÓMO VERIFICAR QUE FUNCIONA

### **1. Abrir el dashboard**
Deberían ver:
- 🎨 Fondo oscuro (negro/azul)
- 💙 Título "NEXUS" con efecto brillante animado
- 🔵 Sidebar con borde azul neón
- 📊 4 métricas con efectos hover

### **2. Generar una predicción**
```
Tab: Nueva Predicción
Vuelo: LH123
Ruta: FRA-JFK
Pasajeros: 245
Business: 45
Duración: 8h
Click: "GENERAR PREDICCIÓN"
```

### **3. Verificar que usa datos reales**
Expandir: **"💡 ¿Por qué estos números?"**

Deberían ver:
```
📊 Vuelos históricos analizados: 10
```
✅ Si dice 10+ → **Usa datos del CSV correctamente**

### **4. Ver el impacto calculado**
Deberían ver:
- 💵 Ahorro de costo
- ⚖️ Peso reducido
- ✈️ Combustible ahorrado
- ♻️ Waste evitado
- 🌍 CO2 evitado
- 🌳 Árboles equivalentes

---

## 🧪 PRUEBAS EXTREMAS (Para demostración)

### **Caso 1: JUMBO (1000 pasajeros)**
```
Vuelo: JUMBO-1000
Ruta: FRA-JFK
Pasajeros: 1000
Business: 200
Duración: 8h
```
**Resultado esperado:**
- Predicciones ~4x más grandes
- Ahorro: ~$3,425
- CO2 evitado: ~18 kg

### **Caso 2: MICRO (50 pasajeros)**
```
Vuelo: MICRO-50
Ruta: FRA-JFK
Pasajeros: 50
Business: 5
Duración: 2h
```
**Resultado esperado:**
- Predicciones pequeñas
- Factor duración: -35%
- Ahorro proporcional

### **Caso 3: ULTRA-LARGO (16 horas)**
```
Vuelo: ULTRA-SIN
Ruta: FRA-SIN
Pasajeros: 350
Business: 80
Duración: 16h
```
**Resultado esperado:**
- ⚠️ Deltas POSITIVOS (necesita MÁS comida)
- Factor duración: +40%
- Muestra que el método estándar falla

---

## 📖 DOCUMENTACIÓN PARA LEER

### **PRIORIDAD ALTA:**
1. **`ACTUALIZACION_DATOS_REALES.md`** ⭐
   - Cómo se procesaron los 615K registros
   - Qué cambió en el código
   - Cómo funcionan las predicciones ahora
   
2. **`COMO_FUNCIONA_NEXUS.md`** 
   - Explicación completa del sistema
   - Análisis del output
   - Algoritmo paso a paso
   
3. **`PRUEBAS_EXTREMAS.md`**
   - 8 casos de prueba listos
   - Inputs y outputs esperados

### **PRIORIDAD MEDIA:**
4. **`INSTRUCCIONES_EQUIPO.md`** - Este archivo (setup y demo)
5. **`README.md`** - Documentación completa

---

## 🎤 PARA LA PRESENTACIÓN

### **Estructura sugerida (5 min):**

**1. Intro (30 seg)**
- Problema: 50%+ de desperdicio en catering aeronáutico
- Solución: NEXUS - Predicción inteligente con ML

**2. Demo Dashboard (2 min)**
- Mostrar tema futurista
- Input de vuelo normal (245 pax)
- Generar predicción
- Explicar tabla (AI vs Standard)
- Mostrar impacto ($$, CO2, waste)

**3. Caso Extremo (1 min)**
- Demo con JUMBO-1000 (1000 pasajeros)
- Mostrar cómo escala
- Destacar ahorro masivo ($3,425)

**4. Tecnología (1 min)**
- Usa datos históricos REALES
- Factores de ajuste (pasajeros, duración, business)
- Closed-loop learning (mejora automática)

**5. Cierre (30 seg)**
- ROI: $$$ + CO2 + waste
- Escalabilidad probada (50 - 1500 pax)
- Gamificación para captura de datos

---

## 🐛 TROUBLESHOOTING

### **Problema: Streamlit no se reconoce**
```powershell
# Solución: Usar ruta completa
C:\ruta\a\HackMTY\.venv\Scripts\streamlit.exe run app.py
```

### **Problema: No encuentra el CSV**
```powershell
# Verificar que existe
dir data\datos_historicos.csv

# Debe mostrar: 86.6 MB (615K registros)
# Si no existe, necesitas el archivo result_hack_oficial.csv
```

### **Problema: Errores de importación**
```powershell
# Reinstalar dependencias
pip install -r requirements.txt
```

### **Problema: Puerto ocupado**
El dashboard intentará puertos: 8501, 8502, 8503
Prueba en tu navegador cada uno hasta que funcione

---

## ✅ CHECKLIST PRE-PRESENTACIÓN

- [ ] Git pull ejecutado
- [ ] Dependencias instaladas
- [ ] Dashboard corriendo (http://localhost:850X)
- [ ] Tema futurista visible (fondo negro/azul)
- [ ] Predicción normal funciona (245 pax)
- [ ] Predicción JUMBO funciona (1000 pax)
- [ ] Muestra "Vuelos históricos: 10+" 
- [ ] Impacto se calcula correctamente
- [ ] Documentación leída (`COMO_FUNCIONA_NEXUS.md`)
- [ ] Roles asignados (quién presenta qué)
- [ ] Pitch ensayado (timing 5 min)

---

## 🎯 DIVISIÓN DE ROLES SUGERIDA

### **Persona 1: Tech Lead**
- Explicar arquitectura
- Mostrar código (opcional)
- Hablar de factores de ajuste

### **Persona 2: Demo**
- Manejar el dashboard
- Ejecutar predicciones
- Mostrar casos extremos

### **Persona 3: Business**
- Explicar problema
- Destacar impacto ($$$, CO2)
- Hablar de ROI y escalabilidad

### **Persona 4: Product**
- Mostrar gamificación
- Hablar de closed-loop learning
- Visión futura

---

## 📞 CONTACTO

Si tienen dudas:
1. Lean `COMO_FUNCIONA_NEXUS.md`
2. Lean `RESUMEN_CAMBIOS.md`
3. Ejecuten las pruebas de `PRUEBAS_EXTREMAS.md`

---

## 🏆 TODO ESTÁ LISTO

✅ Código completo y funcional
✅ Tema futurista aplicado
✅ Datos reales del CSV integrados
✅ Pruebas extremas validadas
✅ Documentación completa
✅ Todo subido a GitHub

**¡Solo hagan `git pull` y ya tienen TODO!** 🚀

---

**Repositorio:** https://github.com/ismamx3/HackMTY.git
**Branch:** main
**Última actualización:** Ahora mismo ✅

**¡ÉXITO EN EL HACKATHON! 🏆**
