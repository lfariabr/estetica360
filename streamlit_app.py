
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

# Footer estilizado e centralizado
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
        background-color: #f1f1f1; /* Adicionando um fundo suave para destacar */
        font-size: 14px; /* Ajuste do tamanho da fonte */
    }
    .footer p {
        margin: 0; /* Remove a margem para centralizar melhor */
    }
    </style>
    <div class="footer">
        <p>360estetic©2024 | Pró-Corpo Labs</p>
    </div>
    """,
    unsafe_allow_html=True
)
