from transformers import pipeline

analizador = pipeline(
    "sentiment-analysis",
    model="pysentimiento/robertuito-sentiment-analysis"
)
texto = "Me encanta este celular, funciona de maravilla."

resultado = analizador(texto)
print(texto)
print(resultado)