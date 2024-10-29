
import streamlit as st
st.title("Estética 360!")
st.write("Welcome!")

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

    # Exibindo os resultados
    st.write(f"Agendamentos (30%): {agendamentos}")
    st.write(f"Comparecimentos (50%): {comparecimentos}")
    st.write(f"Ticket Médio: R$ {ticket_medio}")
    st.write(f"Faturamento estimado: R$ {faturamento:,.2f}")
