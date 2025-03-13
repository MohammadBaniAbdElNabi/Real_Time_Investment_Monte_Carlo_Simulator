import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import yfinance as yf
from scipy.stats import norm
import time

# Streamlit UI Title
st.title("📈 Real-Time Investment Monte Carlo Simulator")

# User Inputs for Ticker Symbol
ticker = st.text_input("Enter Stock Ticker (e.g., AAPL, TSLA, BTC-USD):", "AAPL")
days = st.slider("Investment Horizon (Days):", 30, 365, 252)
simulations = st.slider("Number of Simulations:", 100, 1000, 500)
drift = st.slider("Expected Drift:", -0.05, 0.05, 0.0, step=0.01)

# Fetch Real-Time Stock Data
@st.cache_data(ttl=300)
def fetch_stock_data(ticker):
    try:
        stock = yf.Ticker(ticker)
        df = stock.history(period="1y")
        df['Daily Returns'] = df['Close'].pct_change()
        return df.dropna()
    except Exception as e:
        st.error(f"Error fetching data: {e}")
        return pd.DataFrame()

df = fetch_stock_data(ticker)

if df.empty:
    st.error("❌ No data found! Check the ticker symbol.")
else:
    st.success("✅ Real-Time Data Loaded!")

    # Display Historical Data
    st.subheader("📊 Stock Price History")
    fig = px.line(df, x=df.index, y='Close', title=f'{ticker} Closing Price')
    st.plotly_chart(fig, use_container_width=True)

    # Monte Carlo Simulation using Geometric Brownian Motion (GBM)
    def monte_carlo_simulation(df, num_simulations, num_days, drift):
        mu = df['Daily Returns'].mean()
        sigma = df['Daily Returns'].std()
        last_price = df['Close'].iloc[-1]
        
        simulations = np.zeros((num_days, num_simulations))
        simulations[0] = last_price
        
        for t in range(1, num_days):
            z = np.random.standard_normal(num_simulations)
            simulations[t] = simulations[t-1] * np.exp((mu - 0.5 * sigma**2 + drift) + sigma * z)
        
        return simulations

    # Run Simulation with Progress Bar
    if st.button("🚀 Run Simulation"):
        with st.spinner('Running Monte Carlo Simulations...'):
            time.sleep(1)
            simulations = monte_carlo_simulation(df, simulations, days, drift)
            st.success("✅ Simulation Completed!")

        # Plot Simulation Results
        st.subheader("📈 Simulated Portfolio Growth")
        fig_sim = px.line(pd.DataFrame(simulations), title="Monte Carlo Simulations")
        st.plotly_chart(fig_sim, use_container_width=True)

        # Risk Analysis: Value at Risk (VaR) & Conditional VaR (CVaR)
        final_returns = simulations[-1, :]
        VaR_95 = np.percentile(final_returns, 5)
        CVaR_95 = final_returns[final_returns <= VaR_95].mean()

        st.subheader("⚠️ Risk Analysis")
        st.metric("📉 Value at Risk (VaR 95%)", f"${VaR_95:,.2f}")
        st.metric("📉 Conditional Value at Risk (CVaR 95%)", f"${CVaR_95:,.2f}")
        
        # Download Simulated Data
        st.download_button("📥 Download Simulated Data", 
                           data=pd.DataFrame(simulations).to_csv(index=False),
                           file_name="monte_carlo_simulation.csv", 
                           mime="text/csv")

# Help Section
with st.expander("❓ Help"):
    st.write("This simulator fetches real-time stock data and runs Monte Carlo simulations to predict investment growth.")