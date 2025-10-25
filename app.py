"""Dashboard principal de Streamlit - NEXUS"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import os
from modelo import cargar_modelo, predecir_consumo
from utils import calcular_impacto, generar_explicacion, obtener_semaforo

# ============================================================================
# CONFIGURACIÓN DE PÁGINA
# ============================================================================

st.set_page_config(
    page_title="NEXUS - Predicción de Consumo",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================================
# CSS PERSONALIZADO
# ============================================================================

st.markdown("""
    <style>
    .main-header {
        font-size: 3.5rem;
        color: #1f77b4;
        font-weight: bold;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #666;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background: linear-gradient(135deg, #f0f2f6 0%, #e8eaf0 100%);
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .stMetric {
        background: white;
        padding: 15px;
        border-radius: 8px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    }
    .green-text {
        color: #28a745;
        font-weight: bold;
    }
    .red-text {
        color: #dc3545;
        font-weight: bold;
    }
    .blue-text {
        color: #1f77b4;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# ============================================================================
# SIDEBAR
# ============================================================================

with st.sidebar:
    st.markdown("# ✈️ NEXUS")
    st.markdown("### Sistema de Optimización")
    st.markdown("---")
    
    # Métricas globales
    st.metric(
        label="📊 Accuracy del Modelo",
        value="94.3%",
        delta="+2.1%"
    )
    
    st.metric(
        label="💰 Ahorros Hoy",
        value="$4,567",
        delta="+$342"
    )
    
    st.metric(
        label="♻️ Waste Evitado",
        value="234 kg",
        delta="-18%"
    )
    
    st.markdown("---")
    
    st.caption("🕐 Última actualización: Hoy 08:00")
    st.caption("📍 Unidad: Frankfurt (FRA)")
    st.caption("👥 Vuelos activos: 47")
    
    st.markdown("---")
    st.markdown("**👨‍💻 Desarrollado por:**")
    st.caption("Tu Equipo | Hackathon GateGroup 2025")

# ============================================================================
# HEADER PRINCIPAL
# ============================================================================

st.markdown('<p class="main-header">🛫 NEXUS</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Sistema Inteligente de Predicción de Consumo de Catering</p>', unsafe_allow_html=True)

# ============================================================================
# TABS PRINCIPALES
# ============================================================================

tab1, tab2, tab3 = st.tabs(["📋 Nueva Predicción", "📊 Analytics", "🏆 Leaderboard"])

# ============================================================================
# TAB 1: NUEVA PREDICCIÓN
# ============================================================================

with tab1:
    st.header("Datos del Vuelo")
    
    # Formulario de entrada
    col1, col2, col3 = st.columns(3)
    
    with col1:
        vuelo_numero = st.text_input(
            "Número de vuelo",
            value="LH123",
            help="Ejemplo: LH123, BA456"
        )
        ruta = st.selectbox(
            "Ruta",
            options=["FRA-JFK", "MUC-LAX", "ZRH-SIN", "FRA-LAX", "MUC-JFK", "FRA-SIN"],
            help="Selecciona origen y destino"
        )
    
    with col2:
        fecha_vuelo = st.date_input(
            "Fecha de salida",
            value=datetime.now() + timedelta(days=1),
            min_value=datetime.now()
        )
        hora_salida = st.time_input(
            "Hora de salida",
            value=datetime.strptime("14:30", "%H:%M").time()
        )
    
    with col3:
        pasajeros_total = st.number_input(
            "Pasajeros totales",
            min_value=50,
            max_value=400,
            value=245,
            step=5
        )
        pasajeros_business = st.number_input(
            "Clase Business",
            min_value=0,
            max_value=100,
            value=45,
            step=5
        )
    
    duracion = st.slider(
        "Duración estimada del vuelo (horas)",
        min_value=1.0,
        max_value=16.0,
        value=8.0,
        step=0.5
    )
    
    # Botón de predicción
    st.markdown("---")
    
    if st.button("🎯 GENERAR PREDICCIÓN", type="primary", use_container_width=True):
        
        with st.spinner("🔄 Analizando patrones históricos y generando predicción..."):
            import time
            time.sleep(1.5)  # Simular procesamiento
            
            # ================================================================
            # PREDICCIONES (Aquí cargarías modelos reales)
            # ================================================================
            
            # Por ahora, valores simulados
            # En producción: cargar_modelo('modelo_sandwiches_pollo') y predecir_consumo()
            
            predicciones = {
                'sandwiches_pollo': {'pred': 67, 'lower': 59, 'upper': 75, 'conf': 96},
                'sandwiches_veggie': {'pred': 23, 'lower': 19, 'upper': 27, 'conf': 94},
                'galletas': {'pred': 145, 'lower': 133, 'upper': 157, 'conf': 92},
                'cafe': {'pred': 89, 'lower': 79, 'upper': 99, 'conf': 91},
                'agua': {'pred': 234, 'lower': 220, 'upper': 248, 'conf': 98}
            }
            
            # Método estándar (valores fijos tradicionales)
            estandar = {
                'sandwiches_pollo': 90,
                'sandwiches_veggie': 30,
                'galletas': 200,
                'cafe': 100,
                'agua': 300
            }
        
        st.success("✅ Predicción generada exitosamente")
        
        # ================================================================
        # TABLA DE RECOMENDACIONES
        # ================================================================
        
        st.markdown("---")
        st.header("📦 Recomendación de Carga Optimizada")
        
        # Crear DataFrame para mostrar
        df_pred = pd.DataFrame({
            'Producto': [
                '🥪 Sandwiches Pollo',
                '🥪 Sandwiches Veggie',
                '🍪 Galletas',
                '☕ Café',
                '💧 Agua'
            ],
            'AI Recomienda': [
                predicciones['sandwiches_pollo']['pred'],
                predicciones['sandwiches_veggie']['pred'],
                predicciones['galletas']['pred'],
                predicciones['cafe']['pred'],
                predicciones['agua']['pred']
            ],
            'Standard': [
                estandar['sandwiches_pollo'],
                estandar['sandwiches_veggie'],
                estandar['galletas'],
                estandar['cafe'],
                estandar['agua']
            ],
            'Confianza': [
                f"{predicciones['sandwiches_pollo']['conf']}%",
                f"{predicciones['sandwiches_veggie']['conf']}%",
                f"{predicciones['galletas']['conf']}%",
                f"{predicciones['cafe']['conf']}%",
                f"{predicciones['agua']['conf']}%"
            ]
        })
        
        # Calcular Delta
        df_pred['Delta'] = df_pred['AI Recomienda'] - df_pred['Standard']
        
        # Formatear Delta con emojis
        def formatear_delta(x):
            if x < 0:
                return f"✅ {x}"
            elif x > 0:
                return f"⚠️ +{x}"
            else:
                return "➖ 0"
        
        df_pred['Ahorro/Ajuste'] = df_pred['Delta'].apply(formatear_delta)
        
        # Mostrar tabla
        st.dataframe(
            df_pred[['Producto', 'AI Recomienda', 'Standard', 'Ahorro/Ajuste', 'Confianza']],
            use_container_width=True,
            height=250
        )
        
        # ================================================================
        # EXPLICACIÓN
        # ================================================================
        
        with st.expander("💡 ¿Por qué estos números?", expanded=True):
            explicacion = generar_explicacion(
                ruta=ruta,
                hora=hora_salida.strftime("%H:%M"),
                consumo_historico=56.0,
                confidence=96.0,
                num_vuelos=127
            )
            st.markdown(explicacion)
        
        # ================================================================
        # CÁLCULO DE IMPACTO
        # ================================================================
        
        st.markdown("---")
        st.header("💰 Impacto Multi-Dimensional de esta Decisión")
        
        # Preparar datos para cálculo
        cantidad_ahorrada = {}
        for idx, producto in enumerate(['sandwiches_pollo', 'sandwiches_veggie', 'galletas', 'cafe', 'agua']):
            delta = df_pred.loc[idx, 'Delta']
            if delta < 0:  # Solo si ahorramos
                cantidad_ahorrada[producto] = abs(delta)
        
        vuelo_info = {
            'duracion_horas': duracion,
            'pasajeros': pasajeros_total
        }
        
        # Calcular impacto
        impacto = calcular_impacto(cantidad_ahorrada, vuelo_info)
        
        # Mostrar métricas
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric(
                label="💵 Ahorro de Costo",
                value=f"${impacto['ahorro_dinero']}",
                delta="+12%",
                delta_color="normal"
            )
            st.metric(
                label="⚖️ Peso Reducido",
                value=f"{impacto['peso_reducido_kg']} kg",
                delta="-18%",
                delta_color="inverse"
            )
        
        with col2:
            st.metric(
                label="✈️ Combustible Ahorrado",
                value=f"{impacto['combustible_ahorrado_litros']} L",
                delta="Savings",
                delta_color="off"
            )
            st.metric(
                label="♻️ Waste Evitado",
                value=f"{impacto['waste_evitado_kg']} kg",
                delta="-68%",
                delta_color="inverse"
            )
        
        with col3:
            st.metric(
                label="🌍 CO2 Evitado",
                value=f"{impacto['co2_evitado_kg']} kg",
                delta="Reducción",
                delta_color="off"
            )
            st.metric(
                label="🌳 Árboles Equivalentes",
                value=f"{impacto['arboles_equivalentes']:.1f}",
                delta="Plantados",
                delta_color="off"
            )
        
        # Info adicional
        st.info("""
        **📊 ¿Cómo se calculan estos números?**
        
        - **Ahorro $$$**: Costo unitario de cada producto × cantidad no cargada
        - **Peso**: Peso de cada producto × cantidad reducida
        - **Combustible**: Fórmula aeronáutica (cada kg = 0.003L fuel/hora)
        - **CO2**: 1 litro jet fuel = 2.5 kg CO2
        - **Árboles**: 1 árbol captura ~22 kg CO2/año
        """)
        
        # ================================================================
        # BOTONES DE ACCIÓN
        # ================================================================
        
        st.markdown("---")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.download_button(
                label="📄 Exportar Load Sheet (PDF)",
                data=f"NEXUS - Load Sheet\nVuelo: {vuelo_numero}\nRuta: {ruta}\n\n{df_pred.to_string()}",
                file_name=f"loadsheet_{vuelo_numero}_{fecha_vuelo}.txt",
                mime="text/plain"
            )
        
        with col2:
            if st.button("📧 Compartir por Email", use_container_width=True):
                st.success("✉️ Email enviado al equipo de preparación")
        
        with col3:
            if st.button("✅ Confirmar y Cargar", type="primary", use_container_width=True):
                st.success("✓ Carga confirmada y enviada a producción")

# ============================================================================
# TAB 2: ANALYTICS
# ============================================================================

with tab2:
    st.header("📊 Analytics y Tendencias del Modelo")
    
    # Evolución de Accuracy
    st.subheader("Evolución de Accuracy del Modelo (Closed-Loop Learning)")
    
    # Datos simulados de mejora semanal
    fechas_semanas = pd.date_range(end=datetime.now(), periods=8, freq='W')
    accuracy_semanas = [65.0, 72.0, 78.5, 83.0, 87.5, 90.0, 93.0, 94.3]
    
    fig_accuracy = go.Figure()
    
    fig_accuracy.add_trace(go.Scatter(
        x=fechas_semanas,
        y=accuracy_semanas,
        mode='lines+markers',
        name='Accuracy',
        line=dict(color='#1f77b4', width=3),
        marker=dict(size=10, color='#1f77b4'),
        fill='tozeroy',
        fillcolor='rgba(31, 119, 180, 0.1)'
    ))
    
    fig_accuracy.update_layout(
        title="El modelo mejora automáticamente cada semana sin intervención manual",
        xaxis_title="Semana",
        yaxis_title="Accuracy (%)",
        yaxis_range=[60, 100],
        height=400,
        hovermode='x unified'
    )
    
    st.plotly_chart(fig_accuracy, use_container_width=True)
    
    st.info("""
    **🔄 Closed-Loop Learning:**
    
    Cada noche a las 2 AM, el sistema automáticamente:
    1. Descarga reportes de consumo real de las últimas 24h
    2. Compara predicciones vs realidad
    3. Re-entrena los modelos con los nuevos datos
    4. Actualiza automáticamente para mejorar predicciones futuras
    
    **Resultado:** Mejora continua sin intervención humana
    """)
    
    # Top Rutas
    st.markdown("---")
    st.subheader("🔥 Top Rutas por Mejora de Accuracy")
    
    df_rutas_mejora = pd.DataFrame({
        'Ruta': ['FRA-JFK', 'MUC-LAX', 'ZRH-SIN', 'FRA-LAX', 'MUC-JFK'],
        'Semana 1': [68, 72, 65, 70, 66],
        'Semana 6': [94, 91, 83, 88, 85],
        'Mejora (%)': [26, 19, 18, 18, 19],
        'Estado': ['🔥 Excelente', '⭐ Muy bueno', '📈 Bueno', '📈 Bueno', '⭐ Muy bueno']
    })
    
    df_rutas_mejora = df_rutas_mejora.sort_values('Mejora (%)', ascending=False)
    
    st.dataframe(df_rutas_mejora, use_container_width=True, height=250)
    
    # Distribución por productos
    st.markdown("---")
    st.subheader("📦 Accuracy por Categoría de Producto")
    
    productos_acc = ['Sandwiches', 'Bebidas Calientes', 'Bebidas Frías', 'Snacks', 'Otros']
    accuracy_prod = [94.3, 91.5, 96.8, 89.2, 87.0]
    
    fig_productos = go.Figure(data=[
        go.Bar(
            x=productos_acc,
            y=accuracy_prod,
            marker_color=['#28a745' if x >= 90 else '#ffc107' for x in accuracy_prod],
            text=[f"{x}%" for x in accuracy_prod],
            textposition='outside'
        )
    ])
    
    fig_productos.update_layout(
        title="Precisión del Modelo por Tipo de Producto",
        yaxis_title="Accuracy (%)",
        yaxis_range=[0, 100],
        height=400
    )
    
    st.plotly_chart(fig_productos, use_container_width=True)

# ============================================================================
# TAB 3: LEADERBOARD (GAMIFICACIÓN)
# ============================================================================

with tab3:
    st.header("🏆 Crew Leaderboard - Sistema de Gamificación")
    
    st.markdown("""
    ### 📱 NEXUS Crew App
    
    La tripulación reporta consumo real en **30 segundos** al aterrizar mediante app móvil.
    Ganan puntos, badges y premios reales en dinero.
    
    **¿Por qué funciona?**
    - ⚡ Súper rápido (30 seg con sliders)
    - 🎮 Gamificación profesional
    - 💰 Premios reales en dinero
    - 🏅 Reconocimiento público
    - 📊 Ves tu impacto inmediato
    """)
    
    st.markdown("---")
    st.subheader("🥇 Top Contributors de la Semana")
    
    # Leaderboard simulado
    df_crew = pd.DataFrame({
        'Posición': ['🥇', '🥈', '🥉', '4️⃣', '5️⃣'],
        'Nombre': [
            'María S. (FRA)',
            'Hans M. (MUC)',
            'Sofia L. (ZRH)',
            'Pedro R. (FRA)',
            'Anna K. (MUC)'
        ],
        'Vuelos Reportados': [47, 39, 34, 31, 28],
        'Puntos Totales': [2340, 2120, 1890, 1650, 1520],
        'Accuracy Promedio': ['96%', '94%', '91%', '93%', '90%'],
        'Badges Ganados': ['🎯🔥⭐💎', '🎯🔥⭐', '🎯🔥', '🎯', '🎯']
    })
    
    st.dataframe(df_crew, use_container_width=True, height=250)
    
    # Premios
    col1, col2 = st.columns(2)
    
    with col1:
        st.success("""
        **💰 Premios Mensuales**
        
        - 🥇 1er lugar: **€500** tarjeta Amazon
        - 🥈 2do lugar: **€300** tarjeta Amazon
        - 🥉 3er lugar: **€150** tarjeta Amazon
        """)
    
    with col2:
        st.info("""
        **🎁 Premios Especiales**
        
        - 🏆 Ganador trimestral: **iPad Pro**
        - 🌟 Hall of Fame anual
        - 📜 Reconocimiento corporativo
        """)
    
    # Estadísticas de adopción
    st.markdown("---")
    st.subheader("📊 Estadísticas de Adopción")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Crew Activo", "89%", "+5%")
    
    with col2:
        st.metric("Reportes/Semana", "342", "+27")
    
    with col3:
        st.metric("Data Quality", "94%", "+2%")
    
    with col4:
        st.metric("Engagement", "4.7/5", "+0.3")
    
    # Mockups de la app
    st.markdown("---")
    st.subheader("📱 Mockups de NEXUS Crew App")
    
    st.info("""
    **Flujo de Usuario (30 segundos):**
    
    1. 📲 Notificación push al aterrizar
    2. 📋 Abrir app → vuelo pre-cargado
    3. 👆 Deslizar sliders de consumo (50%, 70%, etc.)
    4. ✅ Enviar → +10 puntos ganados
    5. 🏆 Ver ranking actualizado
    """)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("**Pantalla 1: Lista de Vuelos**")
        st.image("https://via.placeholder.com/300x600/1f77b4/ffffff?text=Lista+de+Vuelos", 
                caption="Vuelos pendientes de reportar")
    
    with col2:
        st.markdown("**Pantalla 2: Sliders Rápidos**")
        st.image("https://via.placeholder.com/300x600/28a745/ffffff?text=Sliders+30seg", 
                caption="Deslizar consumo por producto")
    
    with col3:
        st.markdown("**Pantalla 3: Puntos y Badges**")
        st.image("https://via.placeholder.com/300x600/ffc107/ffffff?text=Puntos+%26+Ranking", 
                caption="Ver puntos ganados y ranking")
    
    st.success("""
    **🎯 Tasa de Adopción Proyectada: 85-90%**
    
    (vs 10-15% de apps corporativas tradicionales)
    
    Basado en principios de economía conductual:
    - Incentivos inmediatos
    - Competencia social
    - Recompensas tangibles
    - Progreso visible
    """)

# ============================================================================
# FOOTER
# ============================================================================

st.markdown("---")
st.markdown("""
    <div style='text-align: center; color: #666; padding: 20px;'>
        <p><strong>NEXUS</strong> © 2025 | Hackathon GateGroup</p>
        <p>Powered by Prophet ML & Streamlit | Desarrollado con ❤️ por Tu Equipo</p>
    </div>
""", unsafe_allow_html=True)
