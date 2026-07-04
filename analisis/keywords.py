import nltk
# Solo es necesario la primera vez
nltk.download('stopwords')
from nltk.corpus import stopwords

# Obtener las stopwords en español
stop_words = stopwords.words('spanish')

print(stop_words[:20])# las primeras 20