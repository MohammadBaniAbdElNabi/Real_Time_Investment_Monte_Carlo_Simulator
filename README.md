# 📊 Real-Time Investment Monte Carlo Simulator

## 🚀 Overview
This project is a **Streamlit-based web application** that provides real-time investment analysis using **Monte Carlo simulations**. The app fetches live stock data via **Yahoo Finance (yfinance)**, performs **statistical analysis**, and generates **visualizations** to assess portfolio performance and risk.

## ✨ Features
- 📡 **Real-Time Investment Data**: Fetches current stock prices and historical data.
- 📈 **Monte Carlo Simulation**: Models future portfolio values based on historical returns.
- 📊 **Interactive Visualizations**: Charts, heatmaps, and risk metrics.
- ⚡ **Customizable Parameters**: Users can adjust simulations, investment horizon, and drift.
- 📝 **Data Editing**: Modify investment data dynamically.
- 📥 **Download Reports**: Export historical and simulated data as CSV.

## 🛠️ Setup & Installation
### 1️⃣ Install Dependencies
Run the following command to install required libraries:
```bash
pip install streamlit pandas numpy seaborn matplotlib altair yfinance
```

### 2️⃣ Run the App
```bash
streamlit run streamlit_app.py
```

## 📂 Project Structure
```
├── streamlit_app.py       # Main application script
├── requirements.txt       # List of dependencies
├── README.md              # Project documentation
```

## 🔧 How It Works
1. **Fetch Data**: Retrieves stock data from Yahoo Finance.
2. **Validate & Process Data**: Ensures correct formatting and data integrity.
3. **Run Monte Carlo Simulation**: Generates future investment scenarios.
4. **Visualize Results**: Displays line charts, heatmaps, and risk assessments.

## 🎨 User Interface
- **Editable Portfolio Table**
- **Dynamic Charts (Altair, Matplotlib, Seaborn)**
- **Simulation Controls (Sliders, Buttons)**

## 📌 Future Enhancements
- 🌍 **Multi-Asset Portfolio Support**
- 🔥 **Machine Learning-Based Forecasting**
- 📊 **Advanced Risk Metrics (Sharpe, Sortino Ratios)**

## 🤝 Contributing
Feel free to **fork** this repository, **submit issues**, or **propose new features**! 😊
