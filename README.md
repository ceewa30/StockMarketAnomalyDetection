# Stock Market Anomaly Detection Dashboard

A real-time financial data visualization tool that uses Machine Learning to identify price outliers and market anomalies. Built with Flask, Scikit-Learn, and Plotly.

# 🚀 Overview

Financial markets move fast, and manual analysis often misses sudden, irregular price movements. This project automates the detection of "black swan" events or potential market manipulations by training an Isolation Forest model on live ticker data.
Key Features
Live Data Fetching: Integration with yfinance for up-to-the-minute stock data.
ML-Powered Detection: Uses an Unsupervised Learning approach (Isolation Forest) to label anomalies without needing historical labels.
Dynamic Controls: Users can toggle between 1-minute to 1-month intervals and 1-day to 10-year periods.
Interactive UI: Fully responsive Plotly charts with hover-tooltips for precise price analysis.
Smart Validation: Built-in JavaScript logic to prevent API errors based on Yahoo Finance data availability limits.

# 🛠️ Tech Stack

Backend: Python, Flask
Machine Learning: Scikit-Learn (Isolation Forest)
Data Science: Pandas, NumPy
API: yfinance (Yahoo Finance)
Frontend: HTML5, CSS3, JavaScript, Plotly.js

# 📦 Installation & Setup

Clone the repository:
bash
git clone https://github.com
cd StockMarketAnomalyDetection
Use code with caution.

# Create a Virtual Environment:

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Use code with caution.

# Install Dependencies:

pip install flask pandas yfinance scikit-learn plotly numpy
Use code with caution.

# Run the Application:

python app.py
Use code with caution.

Open your browser and navigate to http://127.0.0.1:5000.

# 🔍 How it Works

The application follows a 3-step pipeline:
Data Ingestion: Standardizes the complex MultiIndex DataFrames returned by the Yahoo Finance API.
Anomaly Scoring: The IsolationForest algorithm isolates observations by randomly selecting a feature and then randomly selecting a split value between the maximum and minimum values of the selected feature.
Visualization: Data is flattened into 1D NumPy arrays and injected into a Plotly.js template for high-performance rendering.

# 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

Author: Sivakumar
LinkedIn: [Your LinkedIn Link]
