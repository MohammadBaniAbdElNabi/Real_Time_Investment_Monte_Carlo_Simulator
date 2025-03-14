### 📘 **README: Live Investment Dashboard & Risk Analysis**  

---

## 🚀 **Overview**  
This **Streamlit-powered dashboard** provides **real-time investment tracking, Monte Carlo simulations, and advanced risk analysis** for stock market investments. The app **fetches live stock prices** from Yahoo Finance, allows **interactive data editing**, and enables **investment risk evaluation before and after simulation**.  

---

## 📌 **Key Features**  
### 🔹 **Real-Time Data Fetching**
- Retrieves **live stock data** from Yahoo Finance (**1-year historical data**).  
- Updates automatically at **the time of app execution** for accuracy.  
- Allows **dynamic data editing** for portfolio customization.  

### 🔹 **Investment Growth Visualization**
- **Interactive charts** for investment trends over time.  
- Supports **custom stock ticker inputs** (e.g., AAPL, TSLA, AMZN).  

### 🔹 **Monte Carlo Simulation**
- Simulates **future portfolio performance** based on **historical data trends**.  
- Parameters:  
  - **Number of simulations:** 50 to 500  
  - **Investment horizon:** 30 to 252 days  
  - **Expected drift:** -5% to +5%  
- Outputs:  
  - **Simulated portfolio growth** chart  
  - **Heatmap visualization** of all simulations  

### 🔹 **Comprehensive Risk Analysis**  
#### **📉 Before Running the Simulation**  
- **Sharpe Ratio** → Measures risk-adjusted returns.  
- **Sortino Ratio** → Similar to Sharpe but penalizes downside risk only.  
- **Maximum Drawdown (Max DD)** → Shows the largest portfolio loss from peak to bottom.  

#### **📉 After Running the Simulation**  
- **Post-simulation Sharpe Ratio** → Evaluates the risk-return balance of the simulated portfolio.  
- **Post-simulation Sortino Ratio** → Assesses downside risk after simulation.  
- **Post-simulation Max Drawdown** → Identifies worst-case loss scenarios in simulated investments.  
- **Delta Metrics** → Shows the **change** in risk metrics before vs. after simulation.  

### 🔹 **Downloadable Reports**
- **Download Historical Investment Data** as CSV.  
- **Download Simulated Portfolio Data** for further analysis.  

---

## 🎛 **How to Use the App**
1️⃣ **Enter a Stock Ticker** (e.g., AAPL, TSLA, AMZN).  
2️⃣ **Review Live Data** → Data table is editable.  
3️⃣ **Analyze Pre-Simulation Risk Metrics** (Sharpe, Sortino, Max DD).  
4️⃣ **Adjust Monte Carlo Simulation Settings** (simulations, horizon, drift).  
5️⃣ **Run the Simulation** and view **updated risk metrics**.  
6️⃣ **Download Reports** for deeper insights.  

---

## 📦 **Installation & Running Locally**
### 1️⃣ **Install Dependencies**
Ensure you have **Python 3.8+** and install required packages:  
```sh
pip install streamlit pandas numpy seaborn matplotlib altair yfinance
```

### 2️⃣ **Run the App**
```sh
streamlit run streamlit_app.py
```

---

## 🔧 **Future Enhancements**
🔹 **Portfolio Diversification Simulation** (multiple stocks at once)  
🔹 **Custom Risk Tolerance Settings**  
🔹 **Machine Learning-Based Forecasting**  

---

## 🤝 **Contributing**
Feel free to fork the repository and submit pull requests for improvements.  

📩 **Contact:** Let me know if you have any feature suggestions! 🚀