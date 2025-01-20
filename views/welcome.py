
import os
import streamlit as st

base_dir = os.path.dirname(__file__)  # Directory of the current script
logo_path = os.path.join(base_dir, "logo_metodo.jpeg")
st.image(logo_path, width=500)

# Título e introdução
# st.title("Bem-vindo ao Método Marisa Peraro")
st.subheader("Bem-vindo! Vamos transformar sua clínica hoje 🚀")

# Apresentação especial para as clínicas
st.write("""
Se você está aqui, é porque sabe que sua clínica tem potencial para mais! 
Faturar **R$200.000/mês** não é um sonho distante, 
mas uma meta alcançável com as ferramentas certas.
""")

# Benefícios do Método
st.markdown("""
### Por que o Método Marisa Peraro é único?
- **Estratégias Comprovadas**: Com base em dados e resultados reais.
- **Gestão Inteligente**: Melhore a eficiência e elimine desperdícios.
- **Aumento de Vendas**: Multiplique seus lucros com mudanças simples.
- **Apoio Total**: Acompanhamento personalizado para garantir a aplicação do método em sua clínica.
""")

# Motivação
st.write("""
O mercado da estética é competitivo, mas quem tem um método sólido lidera. O **Método Marisa Peraro** combina estratégias
práticas e insights de mercado para transformar sua clínica em referência. Imagine fidelizar mais clientes, aumentar
os atendimentos e fazer sua equipe trabalhar em harmonia com objetivos claros.

Hoje, você está um passo à frente para revolucionar sua clínica.
""")

# Call-to-action e links
st.markdown("""
### Links de Apoio e Próximos Passos
- [Acompanhe no Instagram](https://www.instagram.com/360estetica)
- [Saiba Mais no Site Oficial](https://www.360estetica.com.br/)
- **Fale Conosco**: Estamos aqui para ajudar você a implementar o método e alcançar os resultados que sua clínica merece.
""")

# Interactive Buttons
col1, col2 = st.columns(2)

with col1:
    if st.button("Funil de Vendas 🤑"):
        st.session_state["page"] = "sales_funnel"

with col2:
    if st.button("Quiz de Vendas 💰"):
        st.session_state["page"] = "how_much_did_you_sell"

# Navigation logic
if "page" in st.session_state:
    if st.session_state["page"] == "sales_funnel":
        st.write("Você será redirecionado para o Funil de Vendas...")
        # Replace this with code to load the sales_funnel.py
    elif st.session_state["page"] == "how_much_did_you_sell":
        st.write("Você será redirecionado para o Quiz de Vendas...")
        # Replace this with code to load the how_much_did_you_sell.py
