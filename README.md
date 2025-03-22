# 📈 Investment Risk & Simulation Dashboard  

## **Overview**  
The **Investment Risk & Simulation Dashboard** is a **Streamlit-powered web app** that fetches **real-time stock data**, allows users to **edit their portfolio dynamically**, runs **Monte Carlo simulations** to forecast investment growth, and provides a **detailed risk analysis** based on the simulations.

---

## **🚀 Features**  

### **📊 Real-Time Data Fetching**
- Retrieves **live stock data** from **Yahoo Finance** (updated every 60 seconds).  
- Allows selection from **popular stock tickers** like **Apple (AAPL), Tesla (TSLA), Amazon (AMZN), Microsoft (MSFT), etc.**  
- User can **manually refresh data** at any time.  

### **📋 Editable Portfolio**
- Users can **modify the portfolio** (investment amounts, returns, etc.) within the **dashboard**.  
- Edits are **saved persistently** and **don’t disappear** after modification.  

### **🔄 Monte Carlo Investment Simulation**
- Runs **up to 500 simulations** for stock price movements.  
- Uses **historical daily returns** to predict **future investment growth** over a selected time horizon (30 to 252 days).  
- Allows customization of **drift (expected return bias)** to simulate different market conditions.  

### **⚠️ Simplified Risk Analysis**
- Provides **essential risk metrics** based on simulation results:  
  ✅ **Mean Return**  
  ✅ **Minimum & Maximum Return**  
  ✅ **Median Return**  
  ✅ **Worst Case (5th Percentile)**  
  ✅ **Best Case (95th Percentile)**  
  ✅ **Average Return**  

### **📊 Data Visualization**
- **Line charts** for investment growth over time.  
- **Heatmaps** for simulation results (future stock value trends).  

### **📥 Export Data**
- **Downloadable** simulation data and historical stock data as **CSV files**.  

---

## **💻 How to Run the App**  

### **1️⃣ Install Dependencies**
Make sure you have **Python 3.8+** installed. Then install required libraries:
```bash
pip install -r requirements.txt
```

### **2️⃣ Run the Streamlit App**
```bash
streamlit run streamlit_app.py
```

### **3️⃣ Interact with the Dashboard**
- Select a **stock** from the **dropdown list**.  
- **Edit portfolio data** (investment amounts, returns, etc.).  
- **Run Monte Carlo simulations** to see potential future outcomes.  
- View **risk metrics** and **download results** as CSV.  

---

## **🛠️ Tech Stack**
- **Python** (for data processing and modeling).  
- **Streamlit** (for interactive UI and data visualization).  
- **Yahoo Finance API** (for fetching live stock data).  
- **NumPy & Pandas** (for data handling and Monte Carlo simulation).  
- **Matplotlib & Seaborn** (for advanced visualizations).  

---

## **🔮 Future Improvements**
- 🟢 Add **custom portfolio tracking** for multiple stocks.  
- 🟢 Integrate **machine learning models** for stock return predictions.  
- 🟢 Expand **risk analysis** to include **Sharpe Ratio & Beta Calculation**.  

---

## **📝 License**
This project is **open-source** under the **Apache License**. Feel free to contribute! 🚀  