from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

def resumir_texto(texto, num_oraciones=3):
    if not texto.strip():
        return ""

    parser = PlaintextParser.from_string(texto, Tokenizer("spanish"))
    summarizer = LsaSummarizer()
    resumen = summarizer(parser.document, num_oraciones)

    return " ".join(str(oracion) for oracion in resumen)
