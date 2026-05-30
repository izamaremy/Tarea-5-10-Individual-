import streamlit as st

# Configuración inicial de la portada de la app
st.set_page_config(page_title="Crisol Operational Synergy", layout="wide")

st.title("📚 Crisol Synergy: Omnichannel & Quality Auditor")
st.write("Herramienta interactiva de Business Hacking para solucionar el motor operativo interno.")

# Barra lateral de navegación
st.sidebar.header("🛠️ Panel de Control Operativo")
opcion = st.sidebar.selectbox(
    "Selecciona la Dimensión a Auditar", 
    ["Sincronización Omnicanal", "Control Biológico (Hongos)", "ROI Emocional (Reembolsos)"]
)

# CASO 1: Sincronización de Inventarios
if opcion == "Sincronización Omnicanal":
    st.subheader("🔄 Optimizador de Stock en Tiempo Real")
    st.markdown("Monitorea la brecha de datos entre el stock virtual de la web y el inventario real de las tiendas.")
    
    frecuencia = st.slider("Frecuencia de actualización del inventario (en horas)", 1, 24, 24)
    
    # Lógica de impacto operativo
    if frecuencia == 24:
        ofr_fail = 15.0
        status = "🔴 Alerta: Stock Fantasma Crítico (Actualización por Lotes)"
    elif frecuencia > 12:
        ofr_fail = 10.5
        status = "⚠️ Riesgo Moderado de desincronización cruzada"
    elif frecuencia > 2:
        ofr_fail = 4.0
        status = "🟡 Sincronización optimizada en camino"
    else:
        ofr_fail = 1.2
        status = "🟢 Estado Óptimo: Sincronización Ágil en Tiempo Real"
        
    st.metric(label="Tasa de Cancelación de Pedidos Web (OFR)", value=f"{ofr_fail}%", delta=f"{ofr_fail - 15.0}% vs Baseline")
    st.write(f"**Estado del Ecosistema:** {status}")

# CASO 2: Control de Calidad e Insumos
elif opcion == "Control Biológico (Hongos)":
    st.subheader("🍄 Auditor de Humedad y Calidad del Almacén")
    st.markdown("**Principio GI GO (Garbage In, Garbage Out):** Si entran insumos dañados al almacén, el resultado final será una UX desastrosa.")
    
    humedad = st.slider("Nivel de humedad relativa en el depósito (%)", 30, 95, 85)
    dias = st.slider("Días de almacenamiento prolongado sin rotación de stock", 1, 180, 90)
    
    # Lógica de cálculo de riesgo de moho
    riesgo = (humedad * 0.6) + (dias * 0.4)
    
    if riesgo > 70:
        st.error("🚨 ESTADO CRÍTICO: Alta probabilidad de proliferación de hongos, hojas humedecidas y filos magullados.")
    elif riesgo > 45:
        st.warning("⚠️ ADVERTENCIA MODERADA: Humedad elevada. Se requiere inspección y acondicionamiento ambiental inmediato.")
    else:
        st.success("✅ AMBIENTE SEGURO: Estándar 'Almacén Sano' optimizado. Producto en óptimas condiciones físicas.")

# CASO 3: Gestión Financiera Postventa
elif opcion == "ROI Emocional (Reembolsos)":
    st.subheader("💸 Calculadora de Retención y Capital Emocional")
    st.markdown("Evalúa cómo afecta el tiempo de devolución de dinero a la lealtad de tu comunidad.")
    
    dias_reembolso = st.slider("Días calendario para procesar la devolución del dinero", 1, 30, 30)
    
    # Mapeo del impacto en la satisfacción del usuario
    satisfaccion = max(5, 100 - (dias_reembolso * 3.2))
    
    st.metric(label="Puntaje de Confianza del Cliente (UX Index)", value=f"{int(satisfaccion)}/100")
    
    if dias_reembolso > 15:
        st.error("🔴 Bucle de Fricción Operativa: Clientes migrando a Amazon o Buscalibre. Quejas masivas activas en Reddit.")
    elif dias_reembolso > 5:
        st.warning("🟡 Fricción tolerable, pero el retraso burocrático deteriora gradualmente el posicionamiento de marca.")
    else:
        st.success("🟢 Quick Win Logrado: Flujo financiero ágil. Retención del cliente asegurada para futuras campañas.")
