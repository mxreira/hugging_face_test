from transformers import pipeline

modelo = pipeline("text-generation", model="Qwen/Qwen2.5-0.5B", device= 'cuda')

prompt = 'explain to me what is the programming language Python'

resposta = modelo(prompt)

#print(resposta)

texto_gerado = resposta[0]['generated_text'][len(prompt):]#.replace(prompt,'')

print(texto_gerado)