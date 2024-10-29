
import streamlit as st
st.title("Funil de Leads!")
st.write("Método Estética360 by Marisa Peraro!")
st.markdown("---")

# Input para o funil em formato R$
leads_input = st.number_input("Quantos leads", format="%i", step=1000)

# Botão para calcular
if st.button("Calcular Funil"):
    # Definindo as porcentagens
    agendamentos_pct = 0.30  # 30%
    comparecimentos_pct = 0.50  # 50%
    ticket_medio = 1300  # Valor em R$

    # Calculando os valores
    agendamentos = int(leads_input * agendamentos_pct)
    comparecimentos = int(agendamentos * comparecimentos_pct)
    faturamento = comparecimentos * ticket_medio

    # Exibindo os resultados com formatação mais amigável
    st.success("Seu funil foi gerado com sucesso!")
    
    # Exibição mais bonita dos resultados
    st.write("### Resultados do Funil:")
    
    st.metric(label="Agendamentos (30%)", value=f"{agendamentos}")
    st.metric(label="Comparecimentos (50%)", value=f"{comparecimentos}")
    st.metric(label="Ticket Médio", value=f"R$ {ticket_medio:,.2f}")
    st.metric(label="Faturamento Estimado", value=f"R$ {faturamento:,.2f}")
    
    # Balões para dar um toque especial
    st.balloons()
