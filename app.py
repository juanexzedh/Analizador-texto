import streamlit as st
import matplotlib.pyplot as plt

from analisis.keywords import obtener_keywords, generar_wordcloud
from analisis.summarizer import resumir_texto
from analisis.sentiment import analizador_sentimiento

st.set_page_config(
    page_title="Analizador de Texto",
    page_icon="📄",
    layout="wide"
)
st.title("📄 Analizador de Texto")

texto = st.text_area(
    "Ingrese un texto",
    height=250,
    placeholder="Escriba o pegue aquí el texto..."
)

if st.button("Analizar"):

    # Validaciones
    if not texto.strip():
        st.warning("Debe ingresar un texto para realizar el análisis.")
        st.stop()

    palabras = texto.split()

    if len(palabras) < 30:
        st.warning(f"El texto tiene {len(palabras)} palabras. "
                   "Se requieren al menos 30 para realizar el análisis.")
        st.stop()

    # Resumen
    resumen = resumir_texto(texto)
    st.subheader("Resumen")
    st.write(resumen)

    #Sentimiento
    sentimiento = analizador_sentimiento(texto)
    st.subheader("Análisis de sentimiento")
    st.metric("Clasificación", sentimiento["clasificacion"])

    #Palabras clave
    top10 = obtener_keywords(texto)
    st.subheader("Top 10 palabras")
    st.write(top10)

    #Nube de palabras
    nube = generar_wordcloud(top10)
    fig, ax = plt.subplots(figsize=(10,5))
    ax.imshow(nube, interpolation="bilinear")
    ax.axis("off")
    st.pyplot(fig)

#Para correrlo: python -m streamlit run app.py

"""
TABS
tab1, tab2, tab3 = st.tabs([
    "📝 Resumen",
    "😊 Sentimiento",
    "☁️ Palabras clave"
])

with tab1:
    st.write(resumen)

with tab2:
    st.metric("Clasificación", sentimiento["clasificacion"])
    st.write(f"Polaridad: {sentimiento['score']:.2f}")
    st.write(f"Subjetividad: {sentimiento['sub']:.2f}")

with tab3:
    st.pyplot(fig)


EXPANDERS
with st.expander("📝 Ver resumen"):
    st.write(resumen)

with st.expander("😊 Ver análisis de sentimiento"):
    st.write(sentimiento)

with st.expander("☁️ Ver nube de palabras"):
    st.pyplot(fig)

COLUMNAS
col1, col2 = st.columns(2)

with col1:
    st.subheader("Resumen")
    st.write(resumen)

with col2:
    st.subheader("Sentimiento")
    st.metric("Clasificación", sentimiento["clasificacion"])

st.subheader("Nube de palabras")
st.pyplot(fig)

CONTAINERS
with st.container():
    st.subheader("Resumen")
    st.write(resumen)

with st.container():
    st.subheader("Sentimiento")
    ...

SIDEBARS
num_oraciones = st.sidebar.slider(
    "Oraciones del resumen",
    1,
    10,
    3
)

colormap = st.sidebar.selectbox(
    "Colores",
    ["viridis", "plasma", "magma"]
)

MIENTRAS LAS FUNCIONES HACEN LO SUYO...
with st.spinner("Analizando texto..."):
    resumen = resumir_texto(texto)
    sentimiento = analizador_sentimiento(texto)
    top10 = obtener_keywords(texto)
"""