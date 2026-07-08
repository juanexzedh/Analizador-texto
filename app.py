import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

from analisis.keywords import obtener_keywords, generar_wordcloud
from analisis.summarizer import resumir_texto
from analisis.sentiment import analizador_sentimiento

st.set_page_config(
    page_title="Analizador de Texto",
    page_icon="📄",
    layout="wide"
)
st.title("📄 Analizador de Texto")
st.write("Analiza cualquier texto para obtener su sentimiento, un resumen automático y las palabras más relevantes.")
st.write("-"*50)

texto = st.text_area(
    "Ingrese un texto",
    height=250,
    placeholder="Escriba o pegue aquí el texto..."
)

if st.button("Analizar"):

    with st.spinner("Analizando texto..."):
        # Validaciones
        if not texto.strip():
            st.warning("Debe ingresar un texto para realizar el análisis.")
            st.stop()
        palabras = texto.split()

        if len(palabras) < 30:
            st.warning(f"El texto tiene {len(palabras)} palabras. "
                    "Se requieren al menos 30 para realizar el análisis.")
            st.stop()

        tab1, tab2, tab3 = st.tabs([
            "📝 Resumen",
            "😊 Sentimiento",
            "☁️ Palabras clave"
        ])

        #Resumen
        with st.container():
            resumen = resumir_texto(texto)
            with tab1:
                st.subheader("Resumen")
                st.write(resumen)

        #Sentimiento
        sentimiento = analizador_sentimiento(texto)
        with tab2:
            st.subheader("Análisis de sentimiento")
            st.metric("Clasificación", sentimiento["clasificacion"])
            st.write(f"Polaridad: {sentimiento['score']:.2f}")
            st.progress(sentimiento['score'])
            st.write(f"Subjetividad: {sentimiento['sub']:.2f}")
            st.progress(sentimiento['sub'])

        #Palabras Clave
        top10 = obtener_keywords(texto)
        col1, col2 = st.columns(2)

        with tab3:
            col1, col2 = st.columns(2)
            with col1:
                st.subheader("Top 10 palabras")
                df = pd.DataFrame(top10.items(), columns=["Palabra", "Frecuencia"])
                st.table(df)
        
            with col2:
                #Nube de palabras
                nube = generar_wordcloud(top10)
                fig, ax = plt.subplots(figsize=(10,5))
                ax.imshow(nube, interpolation="bilinear")
                ax.axis("off")
                st.pyplot(fig)

#Para correrlo: python -m streamlit run app.py