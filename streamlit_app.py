
import os
import shutil
import subprocess
import os
import streamlit as st

# Configuração da página
welcome = st.Page(
    "view/welcome.py",
    title="Welcome",
    icon="👋",
)

leads_funnel = st.Page(
    "view/leads_funnel.py",
    title="leads_funnel",
    icon="🧮",
)

funil_de_vendas = st.Page(
    "view/funil_de_vendas.py",
    title="jogo da funil_de_vendas",
    icon="💀",
)


# Configuração da navegação
pg = st.navigation(
    {
        "Boas Vindas 👋": [welcome],
        "Funil de Leads": [leads_funnel],
        "Funil de Vendas": [funil_de_vendas]
    }
)

pg.run()
