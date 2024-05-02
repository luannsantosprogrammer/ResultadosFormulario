import streamlit as st
import pandas as pd
import asyncio


import streamlit as st
import pandas as pd
import asyncio

# Função para ler os dados de forma assíncrona
async def ler_dados():
    await asyncio.sleep(3)  # Espera 3 segundos para simular uma operação assíncrona
    pd.set_option('display.max_columns', 500)
    producao = pd.read_csv('https://docs.google.com/spreadsheets/d/1glWuwTvqPXxnyKMX5LabRYg00koKdRRVaAK8bUGhSR0/export?format=csv')
    quantidade = producao['NOME'].value_counts()
    return quantidade

# Função para mostrar os dados no Streamlit
def mostrar_dados():
    
    with st.empty():  # Cria uma área vazia na interface
        while True:
            quantidade = asyncio.run(ler_dados())  # Executa a leitura assíncrona dos dados
            st.write(quantidade)  # Atualiza os dados na área vazia
            asyncio.sleep(5)  # Espera 5 segundos antes de atualizar novamente

# Interface do Streamlit
st.title('Dados Assíncronos')

mostrar_dados()  # Chama a função para mostrar os dados
