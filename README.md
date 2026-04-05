# Stock Market Anomaly Detection

Data Collection: Use yfinance to download historical adjusted close prices.
Model Training: Use sklearn.ensemble.IsolationForest. The contamination parameter defines the expected proportion of outliers in the data (e.g., 0.01 for 1%).
Detection: The model returns 1 for normal points and -1 for anomalies.
