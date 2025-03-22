import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf
import seaborn as sns
import matplotlib.pyplot as plt

# ---- Configuration ----
st.set_page_config(page_title="Investment Risk & Simulation", layout="wide")

# ---- Stock Ticker Dropdown ----
st.sidebar.header("⚙️ Stock Selection")
stock_options = {
    "Apple (AAPL)": "AAPL",
    "Tesla (TSLA)": "TSLA",
    "Amazon (AMZN)": "AMZN",
    "Microsoft (MSFT)": "MSFT",
    "Google (GOOGL)": "GOOGL",
    "NVIDIA (NVDA)": "NVDA",
    "Meta (META)": "META",
    "Netflix (NFLX)": "NFLX",
    "Disney (DIS)": "DIS",
    "Visa (V)": "V"
}
selected_stock_name = st.sidebar.selectbox("Select a Stock", list(stock_options.keys()))
selected_ticker = stock_options[selected_stock_name]

# ---- Fetch Real-Time Stock Data ----
@st.cache_data(ttl=60)  # Refresh every 60 sec
def fetch_data(ticker):
    stock = yf.Ticker(ticker)
    hist = stock.history(period="1y")  
    df = hist[["Close"]].reset_index()
    df.columns = ["Date", "Investment Amount"]
    df["Daily Returns"] = df["Investment Amount"].pct_change()
    df["Cumulative Returns"] = (1 + df["Daily Returns"]).cumprod()
    return df.dropna()

# ---- Initialize Session State ----
if "df" not in st.session_state:
    st.session_state["df"] = fetch_data(selected_ticker)

# ---- Update Data Button ----
if st.sidebar.button("🔄 Update Data"):
    st.session_state["df"] = fetch_data(selected_ticker)
    st.success(f"Data updated for {selected_ticker}!")

# ---- Display & Edit Data ----
st.title("📈 Investment Risk & Simulation Dashboard")
st.subheader(f"💼 {selected_stock_name} Portfolio Data (Editable)")

edited_df = st.data_editor(st.session_state["df"], num_rows="dynamic")

# ---- Persist user edits ----
if not edited_df.equals(st.session_state["df"]):
    st.session_state["df"] = edited_df  # Save user modifications

# ---- Portfolio Summary ----
st.subheader("📊 Portfolio Summary")
total_investment = st.session_state["df"]["Investment Amount"].sum()
st.metric(label="💰 Total Investment", value=f"${total_investment:,.2f}")

# ---- Investment Growth Plot ----
st.subheader("📈 Investment Growth Over Time")
st.line_chart(st.session_state["df"].set_index("Date")["Investment Amount"])

# ---- Simulation Settings ----
st.subheader("🎛️ Monte Carlo Simulation Settings")
num_simulations = st.slider("Number of Simulations", 50, 500, 100, 50)
num_days = st.slider("Investment Horizon (Days)", 30, 252, 252, 30)
drift = st.slider("Expected Drift", -0.05, 0.05, 0.0, 0.01)

# ---- Monte Carlo Simulation Function ----
def run_simulation(data, num_simulations, num_days, drift=0):
    daily_mean = data["Daily Returns"].mean()
    daily_std = data["Daily Returns"].std()
    simulated_returns = np.random.normal(daily_mean, daily_std, (num_days, num_simulations)) + drift
    cumulative_returns = np.cumprod(1 + simulated_returns, axis=0)
    initial_investment = data["Investment Amount"].iloc[0]
    return initial_investment * cumulative_returns

# ---- Run Simulation ----
if st.button("🚀 Run Simulation"):
    st.subheader(f"📊 {num_simulations} Simulations Over {num_days} Days")
    simulation_results = run_simulation(st.session_state["df"], num_simulations, num_days, drift)
    st.session_state["simulation_results"] = simulation_results

    # ---- Display Simulation Results ----
    st.line_chart(pd.DataFrame(simulation_results))

    # ---- Risk Analysis ----
    st.subheader("⚠️ Risk Analysis Based on Simulation Results")
    final_returns = simulation_results[-1]
    
    mean_return = np.mean(final_returns)
    min_return = np.min(final_returns)
    median_return = np.median(final_returns)
    max_return = np.max(final_returns)
    
    worst_case = np.percentile(final_returns, 5)  # 5th percentile
    best_case = np.percentile(final_returns, 95)  # 95th percentile
    average_return = np.mean(final_returns)
    
    st.metric("📊 Mean Return", f"${mean_return:,.2f}")
    st.metric("📉 Minimum Return", f"${min_return:,.2f}")
    st.metric("📈 Median Return", f"${median_return:,.2f}")
    st.metric("📈 Maximum Return", f"${max_return:,.2f}")
    st.metric("📉 Worst Case (5th Percentile)", f"${worst_case:,.2f}")
    st.metric("📈 Best Case (95th Percentile)", f"${best_case:,.2f}")
    st.metric("📊 Average Return", f"${average_return:,.2f}")

    # ---- Download Simulation Data ----
    st.download_button("📥 Download Simulation Data", pd.DataFrame(simulation_results).to_csv(), "simulated_data.csv")

# ---- Help Section ----
with st.expander("❓ How It Works"):
    st.write("""
    This app fetches real-time stock data, allows users to edit their portfolio, 
    runs Monte Carlo simulations to forecast investment growth, and provides a detailed risk analysis.
    """)