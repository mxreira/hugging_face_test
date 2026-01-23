from transformers import pipeline


def text_generation(prompt):
    modelo = pipeline("text-generation", model="Qwen/Qwen2.5-0.5B", device= 'cuda')
    
    resposta = modelo(prompt)

    texto_gerado = resposta[0]['generated_text'][len(prompt):]

    return texto_gerado
