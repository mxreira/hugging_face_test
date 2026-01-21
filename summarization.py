from transformers import pipeline

modelo = pipeline("summarization", model="facebook/bart-large-cnn", device= 'cuda')


texto = """
Greeks or Hellenes are an ethnic group and nation native to Greece, 
Cyprus, southern Albania, Anatolia, parts of Italy and Egypt, and to a lesser extent, other countries surrounding the Eastern Mediterranean and Black Sea.
They also form a significant diaspora (omogenia), with many Greek communities established around the world.
"""

resposta = modelo(texto, max_length= 140, min_length=30)

print(resposta)