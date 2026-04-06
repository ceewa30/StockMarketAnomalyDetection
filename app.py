import pandas as pd
import yfinance as yf
from flask import Flask, render_template, request
from sklearn.ensemble import IsolationForest
import plotly.graph_objects as go
import json
import numpy as np
import plotly.utils

app = Flask(__name__)

def get_anomaly_data(ticker, period, interval):
    # 1. Fetch data
    data = yf.download(ticker, period=period, interval=interval, progress=False)

    if data.empty:
        return json.dumps({"data": [], "layout": {"title": "No data"}}), 0, 0, 0

    data.columns = data.columns.get_level_values(0) # Keep only price types (Open, Close, etc.)
    df = data.reset_index().dropna(subset=['Close'])

    time_col = df.columns[0]
    df['Date'] = pd.to_datetime(df[time_col])

    close_values = df['Close'].values.reshape(-1, 1)

    # 2. Detect Anomalies (using Close price)
    model = IsolationForest(contamination=0.01, random_state=42)
    df['anomaly'] = model.fit_predict(close_values)

    df['anomaly'] = df['anomaly'].map({1: '0', -1: '1'})

    counts = df['anomaly'].value_counts().to_dict()

    # Map counts to friendly names (handling cases where one might be missing)
    normal_count = counts.get('0', 0)
    anomaly_count = counts.get('1', 0)
    total_count = len(data)


    # 3. Create Plotly Figure
    fig = go.Figure()

    anomalies = df[df['anomaly'] == '1']
    # Use .ravel() to guarantee 1D arrays for Plotly
    y_main = df['Close'].iloc[:, 0].to_numpy().ravel() if df['Close'].ndim > 1 else df['Close'].to_numpy().ravel()
    y_anomaly = anomalies['Close'].iloc[:, 0].to_numpy().ravel() if anomalies['Close'].ndim > 1 else anomalies['Close'].to_numpy().ravel()

    x_main = df.iloc[:, 0].dt.strftime('%Y-%m-%d %H:%M:%S').tolist()
    x_anomaly = anomalies.iloc[:, 0].dt.strftime('%Y-%m-%d %H:%M:%S').tolist()

    # Plot Main Line
    fig.add_trace(go.Scatter(x=x_main, y=y_main.tolist(), name='Close Price', line=dict(color='blue')))

    # Plot Anomalies (Markers will now sit ON the line)
    fig.add_trace(go.Scatter(
        x=x_anomaly, y=y_anomaly.tolist(),
        mode='markers', name='Anomaly',
        marker=dict(color='red', size=10, symbol='x')
    ))

    fig.update_layout(title=f"Anomaly Detection for {ticker}", xaxis_title="Date", yaxis_title="Price")

    graphJSON = fig.to_json()

    return graphJSON, total_count, normal_count, anomaly_count

@app.route('/', methods=['GET', 'POST'])
def index():
    ticker = "AAPL"
    period="1mo"
    interval="30m"
    if request.method == 'POST':
        ticker = request.form.get('ticker', 'AAPL').upper()
        period = request.form.get('period', '1mo')
        interval = request.form.get('interval', '30m')

    graphJSON, total_count, normal_count, anomaly_count = get_anomaly_data(ticker, period, interval)
    return render_template('index.html', graphJSON=graphJSON, ticker=ticker, period=period, interval=interval, total_count=total_count, normal_count=normal_count, anomaly_count=anomaly_count)

if __name__ == '__main__':
    app.run(debug=True)
