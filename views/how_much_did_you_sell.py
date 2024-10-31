
import streamlit as st
import gspread
from google.oauth2 import service_account
import json
import io
import datetime

# Configuração da API do Google Sheets usando variável de ambiente
def connect_to_gsheet():
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    
    # Carrega as credenciais do JSON armazenado na variável de ambiente
    credentials_info = st.secrets["google_credentials"]
    creds = service_account.Credentials.from_service_account_info(credentials_info, scopes=scope)
    
    # Conecta ao Google Sheets
    client = gspread.authorize(creds)
    sheet = client.open_by_key("1uuU05wNcFLwaGWR8KbWaBiWjsO_eCmF5v4PUsaKFQV8").sheet1
    return sheet

# Função para salvar o valor na planilha
def save_to_gsheet(faturamento):
    sheet = connect_to_gsheet()
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sheet.append_row([timestamp, faturamento])  # Armazena data/hora e valor

# Título e introdução
st.title("Quiz de Vendas")
st.write("Método Estética360 by Marisa Peraro!")
st.markdown("---")

# Input para o faturamento do ano
# faturamento_do_ano = st.number_input("Quanto você vendeu este ano? R$", format="%i", step=50000)

# Instrução para o usuário
st.markdown("##### Insira o quanto você vendeu em 2024.")
st.markdown("####### Use apenas números.")
faturamento_do_ano = st.number_input("Vendas do ano:", format="%d", step=1000)

if st.button("Enviar"):
    save_to_gsheet(faturamento_do_ano)
    st.write("Valor enviado:", f"R$ {faturamento_do_ano:,.0f}")
    st.success("Faturamento enviado com sucesso!")
