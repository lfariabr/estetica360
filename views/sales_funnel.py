
import streamlit as st

# Título e introdução
st.title("Funil de Vendas")
st.write("Método Estética360 by Marisa Peraro!")
st.markdown("---")

# Inputs para o faturamento desejado e ticket médio
faturamento_desejado = st.number_input("Quanto quero faturar? R$", format="%i", step=50000)
ticket_medio = st.number_input("Qual o ticket médio? R$", format="%i", step=500)

# Botão para calcular o funil
if st.button("Calcular Funil de Vendas"):
    # Valores fixos
    cpa_meta = 11  # Custo por aquisição (fixo)
    agendamento_pct = 0.30  # Conversão para agendamentos (30%)
    comparecimento_pct = 0.50  # Comparecimento (50%)

    # Cálculos
    compradores_necessarios = faturamento_desejado / ticket_medio
    comparecimentos_necessarios = int(compradores_necessarios)  # Assume 100% dos comparecimentos compram
    agendamentos_necessarios = int(comparecimentos_necessarios / comparecimento_pct)
    leads_necessarios = int(agendamentos_necessarios / agendamento_pct)
    investimento_necessario = leads_necessarios * cpa_meta

    # Exibindo os resultados
    st.success("Seu funil de vendas foi gerado com sucesso!")

    # Exibição dos resultados
    st.write("### Resultados do Funil de Vendas:")
    st.metric(label="Faturamento Desejado", value=f"R$ {faturamento_desejado:,.0f}")
    st.metric(label="Ticket Médio (R$)", value=f"R$ {ticket_medio:,.0f}")
    st.metric(label="CPA Meta (R$)", value=f"R$ {cpa_meta:,.2f}")
    st.metric(label="Leads Necessários", value=f"{leads_necessarios}")
    st.metric(label="Agendamentos Necessários (30%)", value=f"{agendamentos_necessarios}")
    st.metric(label="Comparecimentos Necessários (50%)", value=f"{comparecimentos_necessarios}")
    # st.metric(label="Compradores Necessários", value=f"{int(compradores_necessarios)}")
    st.metric(label="Investimento Necessário (R$)", value=f"R$ {investimento_necessario:,.0f}")

    # Balões para dar um toque especial
    st.balloons()
