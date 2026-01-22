from huggingface_hub import InferenceClient
from dotenv import load_dotenv

load_dotenv()



client = InferenceClient(model='meta-llama/Meta-Llama-3-8B-Instruct')


#Summarization
'''
texto = 'The Greek language holds a very important place in the history of the Western world. Beginning with the epic poetry of Homer, ancient Greek literature includes many works of lasting importance in the European canon. Greek is also the language in which many of the foundational texts in science and philosophy were originally composed. The New Testament of the Christian Bible was also originally written in Greek.[14][15] Together with the Latin texts and traditions of the Roman world, the Greek texts and Greek societies of antiquity constitute the objects of study of the discipline of Classics.'

resposta = client.summarization(texto)'''

#Text Generation / Chat Completion
 
messages = [{"role": "system",  #assistant ou ai se for a resposta do sistema / system para passar conteudo afim de ter respostas padronizadas
             "content": "Responda as perguntas com a didática de um professor universitário de contabiliade, apenas informações verdadeiras e validadas."}]

print('Eu sou seu assistente virtual para dúvidas relacionadas a contabilidade')
print('-----------------------------------------------------------------------\n')
while True:

    pergunta = input('Digite sua Pergunta ("exit" para sair): ')

    if pergunta == 'exit':
        break

    mensagem_usuario = {'role':'user',
                'content':pergunta}

    messages.append(mensagem_usuario)

    resposta = client.chat_completion(messages, max_tokens=600)

    content_resposta = resposta.choices[0]['message']['content']
    role = resposta.choices[0]['message']['role']

    dict_resposta_ia = {'role': role, 'content': content_resposta}
    messages.append(dict_resposta_ia)

    print(content_resposta)