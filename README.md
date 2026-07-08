# 📄 Analizador Inteligente de Texto

Aplicación web desarrollada con **Streamlit** que permite analizar textos en español mediante técnicas básicas de Procesamiento de Lenguaje Natural (NLP).

El usuario puede ingresar cualquier texto (artículos, reseñas, opiniones, comentarios, etc.) y obtener automáticamente:

- 😊 Análisis de sentimiento
- 📝 Resumen automático
- ☁️ Palabras clave más frecuentes
- 📊 Nube de palabras

---

## Vista previa

> *(Aquí puedes agregar una captura de pantalla cuando subas el proyecto.)*

---

## Características

- Análisis de sentimiento utilizando **TextBlob**
- Traducción automática español → inglés para mejorar la precisión del análisis
- Resumen automático mediante el algoritmo **LSA (Latent Semantic Analysis)**
- Extracción de palabras más frecuentes eliminando stopwords
- Generación de nube de palabras
- Interfaz web interactiva con Streamlit

---

## Tecnologías utilizadas

- Python 3
- Streamlit
- TextBlob
- Sumy
- NLTK
- WordCloud
- Pandas
- Matplotlib
- Deep Translator

---

## Estructura del proyecto

```
analizador-texto/
│
├── app.py
│
├── analisis/
│   ├── sentiment.py
│   ├── keywords.py
│   └── summarizer.py
│
├── requirements.txt
└── README.md
```

---

## Instalación

Clonar el repositorio

```bash
git clone https://github.com/usuario/analizador-texto.git

cd analizador-texto
```

Crear entorno virtual

```bash
python -m venv venv
```

Activarlo

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

Instalar dependencias

```bash
pip install -r requirements.txt
```

Descargar las stopwords de NLTK (solo la primera vez)

```python
import nltk
nltk.download("stopwords")
```

---

## Ejecución

```bash
streamlit run app.py
```

---

## Funcionamiento

1. El usuario introduce un texto.
2. La aplicación valida la entrada.
3. Se genera un resumen automático.
4. Se traduce el texto al inglés para realizar el análisis de sentimiento.
5. Se identifican las palabras más frecuentes.
6. Se genera una nube de palabras.

---

## Limitaciones

- El análisis de sentimiento depende de la traducción automática al inglés.
- Se requiere conexión a Internet para utilizar el traductor.
- El resumen utiliza el algoritmo LSA, por lo que puede no capturar completamente el contexto de textos muy complejos.
- No se realiza lematización ni eliminación de signos de puntuación.

---

## Posibles mejoras

- Selección del número de oraciones del resumen desde la interfaz.
- Soporte para múltiples idiomas.
- Exportar resultados a PDF.
- Historial de análisis.
- Gráficas de frecuencia de palabras.
- Cachear resultados utilizando `st.cache_data`.
- Mejor limpieza del texto mediante expresiones regulares.
- Incorporar modelos de Transformers (BERT, RoBERTa o DistilBERT) para mejorar el análisis de sentimiento.

---

## Aprendizajes

Este proyecto permitió poner en práctica:

- Desarrollo de aplicaciones web con Streamlit.
- Procesamiento básico de lenguaje natural (NLP).
- Modularización de proyectos en Python.
- Visualización de datos.
- Manejo de librerías externas.
- Organización de proyectos para portafolio.

---

## Autor

Desarrollado por **Tu Nombre**

Proyecto realizado con fines de aprendizaje y portafolio.