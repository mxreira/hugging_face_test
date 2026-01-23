from transformers import pipeline


def summarization(prompt, max_length = 140, min_length = 30):

    modelo = pipeline("summarization", model="facebook/bart-large-cnn", device= 'cuda')

    resposta = modelo(prompt, max_length= max_length, min_length=min_length)

    print(resposta)

    return resposta[0]['summary_text']

