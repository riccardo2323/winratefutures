import streamlit as st
import numpy as np
import pandas as pd

# Configurazione della pagina
st.title("Simulatore di Trading basato sui Contratti")

# Input dell'utente
contracts = st.sidebar.selectbox("Numero di Contratti", [1, 2, 3, 4])
ticks_profit = st.sidebar.number_input("Ticks di Profitto", min_value=1, max_value=10, value=5)
ticks_loss = st.sidebar.number_input("Ticks di Perdita", min_value=1, max_value=10, value=5)
num_trades = st.sidebar.number_input("Numero di Operazioni", min_value=1, max_value=1000, value=200)
zero_trade_rate = st.sidebar.slider("Percentuale di Chiusura a 0 (%)", min_value=0, max_value=100, value=20) / 100
win_rate = st.sidebar.slider("Percentuale di Vincita (%)", min_value=0, max_value=100, value=60) / 100

# Calcolo delle percentuali effettive
effective_win_rate = win_rate * (1 - zero_trade_rate)

num_variations = st.sidebar.number_input("Numero di Variazioni", min_value=1, max_value=20, value=10)

# Simulazione
profit_per_tick = 12.5  # Profitto per Tick in dollari
simulation_results = {}

for variation in range(1, num_variations + 1):
    profits = []
    for _ in range(num_trades):
        random_value = np.random.rand()
        if random_value <= zero_trade_rate:
            profit = 0  # Trade chiuso a 0
        elif random_value <= zero_trade_rate + effective_win_rate:
            profit = (ticks_profit * profit_per_tick * contracts)  # Trade vincente
        else:
            profit = -(ticks_loss * profit_per_tick * contracts)  # Trade perdente
        profits.append(profit)
    cumulative_profit = np.cumsum(profits)
    simulation_results[f'Variation {variation}'] = cumulative_profit

# Creazione del DataFrame per visualizzare i risultati
df_simulation = pd.DataFrame(simulation_results)

# Visualizzazione dei risultati
st.subheader("Risultati della Simulazione")
st.line_chart(df_simulation)

# Visualizzazione della tabella dei profitti cumulativi
st.subheader("Tabella dei P
