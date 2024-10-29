import streamlit as st

# Estilo customizado com CSS
st.markdown(
    """
    <style>
    .welcome-title {
        font-size: 3em;
        color: #FF5F6D;  /* Cor principal */
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
    .event-details {
        font-size: 1.2em;
        text-align: center;
        margin-bottom: 30px;
        color: #FF5F6D;
    }
    .footer {
        position: fixed;
        bottom: 0;
        width: 100%;
        text-align: center;
        color: #888;
        padding: 10px;
    }
    .logo {
        display: block;
        margin-left: auto;
        margin-right: auto;
        width: 200px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Logo da empresa
st.image("https://www.360estetica.com.br/images/logo-dark.png", width=300)

# Título estilizado
st.markdown('<div class="welcome-title">360 Estética by Marisa Peraro</div>', unsafe_allow_html=True)

# Texto de introdução
st.markdown('<div class="welcome-text">Gestão Estética Eficiente</div>', unsafe_allow_html=True)

# Detalhes do evento
st.markdown('<div class="event-details">Nos dias <strong>02 e 03 de Novembro</strong>, na <strong>Av. Europa-SP</strong>,<br> aprenda a faturar <strong>R$ 200k/mês</strong> na sua clínica 💰</div>', unsafe_allow_html=True)

# Texto adicional com motivação
st.markdown('<div class="welcome-text">Abrindo os segredos da estética para você faturar 200k/mês.<br>Domine a técnica e a metodologia para aumentar o lucro da sua clínica 🚀</div>', unsafe_allow_html=True)
