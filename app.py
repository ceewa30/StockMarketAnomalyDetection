import pandas as pd
import yfinance as yf
from flask import Flask, render_template, request
from sklearn.ensemble import IsolationForest
import plotly.graph_objects as go
import json
import plotly.utils

app = Flask(__name__)

def get_anomaly_data(ticker):
    # 1. Fetch data
    df = yf.download(ticker, start="2023-01-01", progress=False)
    df.reset_index(inplace=True)
    # 2. Detect Anomalies (using Close price)
    model = IsolationForest(contamination=0.01, random_state=42)
    df['anomaly'] = model.fit_predict(df[['Close']].values)

    # 3. Create Plotly Figure
    fig = go.Figure()
    # Main price line
    fig.add_trace(go.Scatter(x=df['Date'], y=df['Close'], name='Close Price', line=dict(color='blue')))

    # Highlight anomalies
    anomalies = df[df['anomaly'] == -1]
    fig.add_trace(go.Scatter(x=anomalies['Date'], y=anomalies['Close'], mode='markers',
                             name='Anomaly', marker=dict(color='red', size=10, symbol='x')))

    fig.update_layout(title=f"Anomaly Detection for {ticker}", xaxis_title="Date", yaxis_title="Price")

    graphJSON = fig.to_json()

    return graphJSON

@app.route('/', methods=['GET', 'POST'])
def index():
    ticker = "AAPL"
    if request.method == 'POST':
        ticker = request.form.get('ticker', 'AAPL').upper()

    graphJSON = get_anomaly_data(ticker)
    return render_template('index.html', graphJSON=graphJSON, ticker=ticker)

if __name__ == '__main__':
    app.run(debug=True)
