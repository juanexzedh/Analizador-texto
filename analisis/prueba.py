import nltk
from nltk.corpus import stopwords
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import streamlit as st

# Obtener las stopwords en español
stop_words = stopwords.words('spanish')

texto = "En una pequeña ciudad había una biblioteca muy antigua. La biblioteca era conocida por sus libros de historia, ciencia, literatura y arte. Cada mañana, muchas personas visitaban la biblioteca para leer, estudiar o simplemente disfrutar del silencio. Algunos estudiantes buscaban información para sus proyectos, mientras que otros leían novelas por entretenimiento. El bibliotecario saludaba a cada visitante con una sonrisa y recomendaba libros según sus intereses. Con el paso del tiempo, la biblioteca se convirtió en un punto de encuentro para la comunidad. Muchas personas regresaban cada semana porque encontraban un ambiente tranquilo y agradable. Además de prestar libros, la biblioteca organizaba talleres de lectura, escritura y ciencia. Los niños disfrutaban especialmente de las actividades, mientras los adultos participaban en clubes de lectura. Gracias a estos eventos, la biblioteca seguía creciendo en popularidad y cada vez más personas descubrían el valor de la lectura y el conocimiento."

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

wordcloud = WordCloud(
    width=800,
    height=400,
    background_color="white",
    colormap="viridis"
).generate_from_frequencies(top10)

# Mostrarla con matplotlib
fig, ax = plt.subplots(figsize=(10,5))
ax.imshow(wordcloud, interpolation="bilinear")
ax.axis("off")
st.pyplot(fig)