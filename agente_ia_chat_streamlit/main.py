import streamlit as st
from summarization import summarization
from text_generation import text_generation
from chat_completion import chat_completion
def gerador_texto(prompt):
    st.write('Gerador de texto selecionado')

    resposta = text_generation(prompt)

    if resposta:
        st.success('Texto gerado com sucesso!')
        st.write(resposta)
    else:
        st.error('Erro ao gerar texto')
    


def resumidor_texto(prompt):

    st.markdown('##### Resumidor de texto selecionado')

    resposta = summarization(prompt)
    if resposta:
        st.success('Resumo gerado com sucesso!')
        st.write(resposta)
    else:
        st.error('Erro ao gerar resumo')


def abrir_chat(prompt):
    
    st.markdown('##### Converse com a IA')


    #armazenar lista de mensagens -> session_state
    if 'mensagens' not in st.session_state:
        mensagens = [{"role": "system",  #assistant ou ai se for a resposta do sistema / system para passar conteudo afim de ter respostas padronizadas
             "content": "Responda as perguntas apenas informações verdadeiras e validadas."}]
    
        st.session_state['mensagens'] = mensagens

    else:
        mensagens = st.session_state['mensagens']

    if prompt:

        
        mensagem_usuario = {'role': 'user',
                            'content': prompt}

        mensagens.append(mensagem_usuario)

        mensagens = chat_completion(mensagens)

        for dic_mensagem in mensagens:

            role = dic_mensagem['role']
            content = dic_mensagem['content']

            with st.chat_message(role):
                st.write(content)

def main_app():
    
    #titulo -> HashIAs

    st.header('HashIAs', divider= True)

    #subtitulo -> Selecione a IA quie mais te ajuda, envie seu prompt

    st.markdown('#### Selecione a IA que mais te ajuda, envie seu prompt')

    #selectbox -> gerar texto, resumir texto, abrir chat
    
    opcoes = ['Gerar Texto', 'Resumir Texto', 'Abrir Chat']

    ferramenta_selecionada = st.selectbox('Selecione a ferramenta de IA desejada', options= opcoes)

    #campo de prompt -> digite aqui seu prompt

    prompt = st.chat_input('Digite aqui seu prompt')

    if ferramenta_selecionada:
        
        if ferramenta_selecionada == opcoes[0]:
            if prompt:
                gerador_texto(prompt)

        elif ferramenta_selecionada == opcoes[1]:
            if prompt:
                resumidor_texto(prompt)

        elif ferramenta_selecionada == opcoes[2]:

            abrir_chat(prompt)
        else:
            print('Opção inválida')
        


main_app()