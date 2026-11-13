import streamlit as st
from teste_prova import obter_dados_meteorologicos

st.set_page_config(
    page_title="Dashboard Meteorológico",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Dashboard Meteorológico")
st.write("Painel de monitoramento — Jaraguá do Sul/SC")

if st.button("🔄 Consultar novamente"):
    st.rerun()

try:
    with st.spinner("Atualizando painel..."):
        dados = obter_dados_meteorologicos()
    
    st.success("Painel atualizado.")
    st.subheader("Indicadores principais")
    
    col1, col2, col3, col4 = st.columns(4)
    
    col1.metric(
        "🌡️ Temperatura",
        f"{dados['current']['temperature_2m']:.1f} °C"
    )
    col2.metric(
        "💧 Umidade",
        f"{dados['current']['relative_humidity_2m']} %"
    )
    col3.metric(
        "💨 Velocidade do Vento",
        f"{dados['current']['wind_speed_10m']:.1f} km/h"
    )
    col4.metric(
        "⛰️ Elevação",
        f"{dados['elevation']} m"
    )

except Exception as e:
    st.error(f"Erro ao obter os dados meteorológicos: {e}")
