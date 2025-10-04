import streamlit as st
import dados

st.title('Jogos')

jogo = st.text_input('Nome do jogo: ')
ano = st.number_input('Ano do jogo: ' , min_value=1950, max_value=2025)
empresa = st.text_input('Empresa criadora do jogo: ')

if st.button('Adicionar'):
    dados.adicionar_dados(jogo, ano , empresa)
    st.success('Jogo adicionado com sucesso!')

jogos = dados.obter_jogos()
st.header('Lista de jogos')
st.table(jogos)