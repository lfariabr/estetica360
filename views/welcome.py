
import os
import streamlit as st

base_dir = os.path.dirname(__file__)  # Directory of the current script
logo_path = os.path.join(base_dir, "logo_metodo.jpeg")
st.image(logo_path, width=500)

# Título e introdução
st.title("Bem-vindo ao Método Marisa Peraro")
st.subheader("Transformando Clínicas em Máquinas de Lucro")

# Apresentação especial para as clínicas
st.write("""
**Olá!** Hoje é um dia especial para as 13 clínicas que decidiram dar um passo à frente no mercado de estética. 
Juntas, vamos explorar como aplicar o **Método Marisa Peraro**, uma abordagem revolucionária que já transformou 
inúmeras clínicas em negócios altamente lucrativos.

Se você está aqui, é porque sabe que sua clínica tem potencial para mais. E nós estamos aqui para mostrar que faturar
**R$200.000/mês** não é um sonho distante, mas uma meta alcançável com as ferramentas certas.
""")

# Benefícios do Método
st.markdown("""
### Por que o Método Marisa Peraro é único?
- **Estratégias Comprovadas**: Com base em dados e resultados reais.
- **Gestão Inteligente**: Melhore a eficiência e elimine desperdícios.
- **Aumento de Faturamento**: Descubra como multiplicar seus lucros sem aumentar custos desnecessários.
- **Apoio Total**: Acompanhamento personalizado para garantir a aplicação do método em sua clínica.
""")

# Motivação
st.write("""
O mercado da estética é competitivo, mas quem tem um método sólido lidera. O **Método Marisa Peraro** combina estratégias
práticas e insights de mercado para transformar sua clínica em referência. Imagine fidelizar mais clientes, aumentar
os atendimentos e fazer sua equipe trabalhar em harmonia com objetivos claros.

Hoje, você está um passo à frente para revolucionar sua clínica. Vamos nessa? 🚀
""")

# Call-to-action e links
st.markdown("""
### Links de Apoio e Próximos Passos
- [Acompanhe no Instagram](https://www.instagram.com/360estetica)
- [Saiba Mais no Site Oficial](https://www.360estetica.com.br/)
- **Fale Conosco**: Estamos aqui para ajudar você a implementar o método e alcançar os resultados que sua clínica merece.
""")

st.success("Estamos animados para embarcar nessa jornada com vocês! Vamos começar?")
