from textblob import TextBlob
from deep_translator import GoogleTranslator

def analizador_sentimiento(texto):
    traduccion = GoogleTranslator(source='es', target='en').translate(texto)
    analisis = TextBlob(traduccion)

    pol = analisis.sentiment.polarity
    sub = analisis.sentiment.subjectivity
    if pol >= 0.2:
        clasificacion = "Positivo"
    elif pol <= -0.2:
        clasificacion = "Negativo"
    else:
        clasificacion = "Neutro"

    resultados = {"score": pol, "clasificacion": clasificacion, "sub": sub}

    print(f"Texto: {traduccion}")
    print(f"Polaridad: {pol}")
    print(f"Subjetividad: {sub}")
    print(f"Clasificacion: {clasificacion}")

    return resultados
    