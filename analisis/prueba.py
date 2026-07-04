from textblob import TextBlob
from deep_translator import GoogleTranslator

#texto = "I love my mom, she always makes me happy. I am proud that I have her in my life"
# analisis = TextBlob(texto)

textos = [
    "Me encanta este celular. Es lo mejor que me ha pasado en la vida, lo amo.",
    "Odio hacer filas en el banco.",
    "Hoy está lloviendo.",
    "Detesto que me traten asi. Todos son malos conmigo, nadie me quiere, todos me odian.",
    "El examen fue difícil."
]

for texto in textos:
    traduccion = GoogleTranslator(source='es', target='en').translate(texto)
    analisis = TextBlob(traduccion)
    print(f"Texto: {traduccion}")
    print(f"Polaridad: {analisis.sentiment.polarity}")
    print(f"Subjetividad: {analisis.sentiment.subjectivity}")
    print("-" * 40)