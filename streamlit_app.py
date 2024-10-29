
import os
import streamlit as st

# Configuração da página e navegação
st.set_page_config(
    page_title="Estética 360",
    page_icon="💎",  # Ícone global da página (diamante)
    layout="wide",
    initial_sidebar_state="expanded",
)

# Definição das páginas do app com ícones personalizados
pages = {
    "💎 Boas Vindas": "views/welcome.py",  # Ícone de diamante
    "⭐ Funil de Leads": "views/leads_funnel.py",  # Ícone de estrela
    "💰 Funil de Vendas": "views/sales_funnel.py",  # Ícone de dinheiro
}

# Sidebar com seleção de páginas
st.sidebar.title("Menu Estética360")
selected_page = st.sidebar.radio("Navegação", options=pages.keys())

# Função para carregar e executar o código da página selecionada
def load_page(page):
    with open(page, "r") as file:
        exec(file.read(), globals())

# Carregar a página selecionada
page_path = pages[selected_page]
load_page(page_path)

# Footer estilizado
st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        bottom: 0;
        width: 100%;
        text-align: center;
        color: #888;
        padding: 10px;
    }
    </style>
    <div class="footer">
        <p>Estética360 © 2024 | Desenvolvido por Luis</p>
    </div>
    """,
    unsafe_allow_html=True
)
