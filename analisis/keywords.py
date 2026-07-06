import nltk
import streamlit as st
from nltk.corpus import stopwords
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def obtener_keywords(texto):
    # Obtener las stopwords en español
    stop_words = stopwords.words('spanish')

    # Obtener palabras (eliminar stop words)
    palabras = texto.lower().split()
    palabras_filtradas = [
        palabra for palabra in palabras
        if palabra not in stop_words
    ]
    print(palabras_filtradas)
    print("-" * 40)

    # Contar la frecuencia de cada palabra
    contador = Counter(palabras_filtradas)
    print(contador)
    print("-" * 40)

    #Las 10 mas repetidas
    top10 = contador.most_common(10)
    top10 = dict(top10)
    print(top10)

    # Crear la nube de palabras
    wordcloud = WordCloud(
        width=800,
        height=400,
        background_color="white",
        colormap="viridis"
    ).generate_from_frequencies(top10)

    # Mostrarla con matplotlib
    plt.figure(figsize=(10,5))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()

    """
    fig, ax = plt.subplots(figsize=(10,5))
    ax.imshow(wordcloud, interpolation="bilinear")
    ax.axis("off")

    st.pyplot(fig)
    """