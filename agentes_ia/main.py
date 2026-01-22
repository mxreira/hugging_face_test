from huggingface_hub import InferenceClient
from dotenv import load_dotenv

load_dotenv()


client = InferenceClient()

texto = 'The Greek language holds a very important place in the history of the Western world. Beginning with the epic poetry of Homer, ancient Greek literature includes many works of lasting importance in the European canon. Greek is also the language in which many of the foundational texts in science and philosophy were originally composed. The New Testament of the Christian Bible was also originally written in Greek.[14][15] Together with the Latin texts and traditions of the Roman world, the Greek texts and Greek societies of antiquity constitute the objects of study of the discipline of Classics.'

resposta = client.summarization(texto)

print(resposta)