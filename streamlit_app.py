
import os
import shutil
import subprocess
import os
import streamlit as st

# Configuração da página
welcome = st.Page(
    "views/welcome.py",
    title="Welcome",
    icon="👋",
)

leads_funnel = st.Page(
    "views/leads_funnel.py",
    title="leads_funnel",
    icon="🧮",
)

sales_funnel = st.Page(
    "views/sales_funnel.py",
    title="jogo da sales_funnel",
    icon="💀",
)


# Configuração da navegação
pg = st.navigation(
    {
        "Menu Estética360": [welcome, leads_funnel, sales_funnel],
        # "Funil de Leads": [leads_funnel],
        # "Funil de Vendas": [sales_funnel]
    }
)

pg.run()
