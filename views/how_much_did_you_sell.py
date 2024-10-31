
import streamlit as st

# Título e introdução
st.title("Funil de Vendas")
st.write("Método Estética360 by Marisa Peraro!")
st.markdown("---")

# Inputs para o faturamento desejado e ticket médio
faturamento_do_ano = st.number_input("Quanto você vendeu este ano? R$", format="%i", step=50000)
