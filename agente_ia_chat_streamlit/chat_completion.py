from huggingface_hub import InferenceClient
from dotenv import load_dotenv

load_dotenv()

def chat_completion(mensagens: list, max_tokens = 600):
    
    client = InferenceClient(model='meta-llama/Meta-Llama-3-8B-Instruct')

    resposta = client.chat_completion(mensagens, max_tokens=max_tokens)

    content_resposta = resposta.choices[0]['message']['content']
    role = resposta.choices[0]['message']['role']

    dict_resposta_ia = {'role': role, 'content': content_resposta}
    mensagens.append(dict_resposta_ia)

    return mensagens



