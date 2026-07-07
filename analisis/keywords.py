from nltk.corpus import stopwords
from collections import Counter
from wordcloud import WordCloud

def obtener_keywords(texto):
    # Obtener las stopwords en español
    stop_words = stopwords.words('spanish')

    # Obtener palabras (eliminar stop words)
    palabras = texto.lower().split()
    palabras_filtradas = [
        palabra for palabra in palabras
        if palabra not in stop_words
    ]
    # Contar la frecuencia de cada palabra
    contador = Counter(palabras_filtradas)

    #Las 10 mas repetidas
    top10 = dict(contador.most_common(15))
    return top10


def generar_wordcloud(frecuencias):

    return WordCloud(
        width=800,
        height=400,
        background_color="white",
        colormap="viridis"
    ).generate_from_frequencies(frecuencias)