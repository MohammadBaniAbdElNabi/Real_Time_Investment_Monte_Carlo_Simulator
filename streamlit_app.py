import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import altair as alt
import yfinance as yf

# Function to fetch real-time investment data
def fetch_data(ticker="AAPL"):
    try:
        df = yf.download(ticker, period="1y", interval="1d")
        df = df[["Close"]].reset_index()
        df.columns = ["Date", "Investment Amount"]
        df["Daily Returns"] = df["Investment Amount"].pct_change().fillna(0)
        df["Cumulative Returns"] = (1 + df["Daily Returns"]).cumprod()
        return df
    except Exception as e:
        st.error(f"Error fetching data: {e}")
        return pd.DataFrame()

# Function to run Monte Carlo investment simulation
def run_monte_carlo_simulation(data, num_simulations, num_days, drift=0):
    daily_returns_mean = data["Daily Returns"].mean()
    daily_returns_std = data["Daily Returns"].std()

    simulated_daily_returns = np.random.normal(daily_returns_mean, daily_returns_std, (num_days, num_simulations)) + drift
    cumulative_returns = np.cumprod(1 + simulated_daily_returns, axis=0)

    initial_investment = data["Investment Amount"].iloc[-1]  # Latest Investment Value
    simulated_portfolio_value = initial_investment * cumulative_returns
    
    return pd.DataFrame(simulated_portfolio_value)

# Function to calculate risk metrics
def calculate_risk_metrics(df):
    daily_returns = df["Daily Returns"].dropna()

    # Sharpe Ratio
    sharpe_ratio = daily_returns.mean() / daily_returns.std() * np.sqrt(252)

    # Sortino Ratio (using only downside deviation)
    downside_returns = daily_returns[daily_returns < 0]
    sortino_ratio = daily_returns.mean() / downside_returns.std() * np.sqrt(252)

    # Maximum Drawdown
    cumulative_max = df["Cumulative Returns"].cummax()
    drawdown = df["Cumulative Returns"] / cumulative_max - 1
    max_drawdown = drawdown.min()

    return sharpe_ratio, sortino_ratio, max_drawdown

# Streamlit UI
st.title("📊 Live Investment Dashboard & Risk Analysis")

# Stock Ticker Selection
ticker = st.text_input("Enter Stock Ticker (e.g., AAPL, TSLA, AMZN):", "AAPL")

# Fetch live data
df = fetch_data(ticker)

if df.empty:
    st.error("❌ No data found! Check the ticker symbol.")
else:
    st.success(f"✅ Live Data Loaded for {ticker} at {pd.Timestamp.now()}")

    # Editable Data Table
    st.subheader("💼 Edit Your Investment Data")
    edited_df = st.data_editor(df, num_rows="dynamic")

    # Investment Growth Chart
    st.subheader("📈 Investment Growth Over Time")
    line_chart = alt.Chart(edited_df).mark_line().encode(
        x='Date:T',
        y='Investment Amount:Q',
        tooltip=['Date:T', 'Investment Amount:Q']
    ).interactive()
    st.altair_chart(line_chart, use_container_width=True)

    # Pre-Simulation Risk Analysis
    st.subheader("📉 Risk Analysis (Before Simulation)")
    sharpe, sortino, max_dd = calculate_risk_metrics(edited_df)
    
    col1, col2, col3 = st.columns(3)
    col1.metric("📊 Sharpe Ratio", f"{sharpe:.2f}")
    col2.metric("📊 Sortino Ratio", f"{sortino:.2f}")
    col3.metric("📊 Max Drawdown", f"{max_dd:.2%}")

    # Monte Carlo Simulation Settings
    st.subheader("🎛️ Monte Carlo Simulation Settings")
    num_simulations = st.slider("Number of Simulations", min_value=50, max_value=500, value=100, step=50)
    num_days = st.slider("Investment Horizon (Days)", min_value=30, max_value=252, value=252, step=30)
    drift = st.slider("Expected Drift", min_value=-0.05, max_value=0.05, value=0.0, step=0.01)

    # Run Simulation
    if st.button("🚀 Run Simulation"):
        st.subheader(f"📊 Running {num_simulations} Simulations Over {num_days} Days")

        # Run Simulation
        simulation_results = run_monte_carlo_simulation(edited_df, num_simulations, num_days, drift)

        # Display Simulation Results
        st.subheader("📊 Simulated Portfolio Growth Over Time")
        st.line_chart(simulation_results)

        # Heatmap of Simulations
        st.subheader("📊 Simulation Results Heatmap")
        fig, ax = plt.subplots(figsize=(12, 8))
        sns.heatmap(simulation_results, cmap="coolwarm", cbar=True, ax=ax)
        ax.set_title("Heatmap of Simulated Portfolio Values Over Time")
        ax.set_xlabel("Simulations")
        ax.set_ylabel("Days")
        st.pyplot(fig)

        # Post-Simulation Risk Analysis
        st.subheader("📉 Risk Analysis (After Simulation)")

        final_returns = simulation_results.iloc[-1]  # Get final returns of simulations
        simulated_df = pd.DataFrame({"Daily Returns": final_returns.pct_change().fillna(0), "Cumulative Returns": (1 + final_returns.pct_change()).cumprod()})

        sim_sharpe, sim_sortino, sim_max_dd = calculate_risk_metrics(simulated_df)

        col1, col2, col3 = st.columns(3)
        col1.metric("📊 Sharpe Ratio (After)", f"{sim_sharpe:.2f}", delta=f"{sim_sharpe - sharpe:.2f}")
        col2.metric("📊 Sortino Ratio (After)", f"{sim_sortino:.2f}", delta=f"{sim_sortino - sortino:.2f}")
        col3.metric("📊 Max Drawdown (After)", f"{sim_max_dd:.2%}", delta=f"{sim_max_dd - max_dd:.2%}")

        # Download Simulated Portfolio Data
        st.download_button(
            label="📥 Download Simulated Portfolio Data",
            data=simulation_results.to_csv(index=False),
            file_name="simulated_portfolio_values.csv",
            mime="text/csv"
        )

    # Download Historical Data
    st.download_button(
        label="📥 Download Live Investment Data",
        data=df.to_csv(index=False),
        file_name="live_investment_data.csv",
        mime="text/csv"
    )

# Help Section
with st.expander("❓ Help"):
    st.write("This dashboard allows you to analyze live stock investments, run Monte Carlo simulations, and assess risk metrics.")