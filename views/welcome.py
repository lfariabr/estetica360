
import os
import streamlit as st

base_dir = os.path.dirname(__file__)  # Directory of the current script
logo_path = os.path.join(base_dir, "logo.jpeg")
st.image(logo_path, width=300)

# Título e introdução
st.title("Método Marisa Peraro")
st.subheader("CLÍNICAS LUCRATIVAS")

# Detalhes do evento
# st.write("""
# Nos dias 02 e 03 de Novembro, na Av. Europa-SP,
# aprenda a faturar R$ 200k/mês na sua clínica 💰
# """)

# Texto adicional com motivação
st.write("""
Abrindo os segredos da estética para você faturar 200k/mês.
Domine a técnica e a metodologia para aumentar o lucro da sua clínica 🚀
""")

# Links de apoio
st.markdown("""
### Links de Apoio
- [Instagram](https://www.instagram.com/360estetica)
- [Site Oficial](https://www.360estetica.com.br/)
""")
