import streamlit as st

# Configuração do layout e estilo da página
st.set_page_config(page_title="Boas Vindas", page_icon="💎", layout="wide")

# Estilo customizado com CSS
st.markdown(
    """
    <style>
    .welcome-title {
        font-size: 3em;
        color: #FF5F6D;  /* Cor similar ao branding da 360 Estética */
        font-weight: bold;
        text-align: center;
        margin-bottom: 20px;
    }
    .welcome-text {
        font-size: 1.5em;
        text-align: center;
        margin-bottom: 30px;
        color: #FFC371;
    }
    .welcome-button {
        display: flex;
        justify-content: center;
    }
    .footer {
        position: fixed;
        bottom: 0;
        width: 100%;
        text-align: center;
        color: #888;
        padding: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Título estilizado
st.markdown('<div class="welcome-title">Bem-vindo à Estética 360!</div>', unsafe_allow_html=True)

# Texto de boas-vindas estilizado
st.markdown('<div class="welcome-text">Seu ponto de partida para beleza, bem-estar e tecnologia.</div>', unsafe_allow_html=True)

# Botão centralizado
st.markdown('<div class="welcome-button">', unsafe_allow_html=True)
if st.button('Explorar Serviços'):
    st.write("Aqui você pode explorar todos os nossos serviços de estética.")
st.markdown('</div>', unsafe_allow_html=True)

# Footer estilizado
st.markdown(
    """
    <div class="footer">
        <p>Estética360 © 2024 | <a href="https://www.360estetica.com.br/" target="_blank">Visite nosso site</a></p>
    </div>
    """,
    unsafe_allow_html=True
)
