
import streamlit as st

# Título e introdução
st.title("Estética 360 - Funil de Vendas")
st.write("Bem-vindo ao Funil de Vendas!")

# Input para o faturamento desejado
faturamento_desejado = st.number_input("Quanto quero faturar? R$", format="%i", step=50000)

# Botão para calcular o funil
if st.button("Calcular Funil de Vendas"):
    # Valores fixos
    investimento_mensal = 8000  # Investimento fixo
    cpa_meta = 11  # Custo por aquisição (fixo)
    agendamento_pct = 0.30  # Conversão para agendamentos (30%)
    comparecimento_pct = 0.50  # Comparecimento (50%)
    ticket_medio = 1820  # Ticket médio fixo (R$ 1.820)

    # Cálculos
    leads_necessarios = int(investimento_mensal / cpa_meta)
    agendamentos = int(leads_necessarios * agendamento_pct)
    comparecimentos = int(agendamentos * comparecimento_pct)
    faturamento_estimado = comparecimentos * ticket_medio

    # Exibindo os resultados
    st.success("Seu funil de vendas foi gerado com sucesso!")

    # Exibição dos resultados
    st.write("### Resultados do Funil de Vendas:")
    st.metric(label="Investimento Mensal", value=f"R$ {investimento_mensal:,.2f}")
    st.metric(label="Leads Gerados", value=f"{leads_necessarios}")
    st.metric(label="CPA Meta (R$)", value=f"R$ {cpa_meta:,.2f}")
    st.metric(label="Agendamentos (30%)", value=f"{agendamentos}")
    st.metric(label="Comparecimentos (50%)", value=f"{comparecimentos}")
    st.metric(label="Ticket Médio (R$)", value=f"R$ {ticket_medio:,.2f}")
    st.metric(label="Faturamento Estimado (R$)", value=f"R$ {faturamento_estimado:,.2f}")
    
    # Balões para dar um toque especial
    st.balloons()
