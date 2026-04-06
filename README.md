# Stock Market Anomaly Detection

Data Collection: Use yfinance to download historical adjusted close prices.
Model Training: Use sklearn.ensemble.IsolationForest. The contamination parameter defines the expected proportion of outliers in the data (e.g., 0.01 for 1%).
Detection: The model returns 1 for normal points and -1 for anomalies.


Objective 	            Typical Period	        Typical Interval

Flash Crash Detection	30–60 Minutes	        1–5 Seconds
Day Trading Setup	    1–5 Days	            5–15 Minutes
Swing Trading/Risk	    30–90 Days	            Daily (EOD)
Structural/Calendar	    1–5 Years	            Daily or Monthly


# Period 1 and 5 Days

Interval = 1 min , 2 min, 5 min, 15 min, 30 min, 60 min, 90 min, 1 hour, 1 Day

# Period 1 Month

Interval = 2 min, 5 min, 15 min, 30 min, 60 min, 90 min, 1 hour, 1 Day, 1 week, 1 month

# Period 3 Month

Interval = 60 min, 1 hour, 1 Day, 1 week, 1 month, 3 month

# Period 6 Month

Interval = 60 min, 1 hour, 1 Day, 1 week, 1 month, 3 month

# Period 1 Year

Interval = 60 min, 1 hour, 1 Day, 1 week, 1 month, 3 month

# Period 3 Year

Interval = 1 Day, 1 week, 1 month, 3 month

# Period 5 Year

Interval = 1 Day, 1 week, 1 month, 3 month

# Period 10 Year

Interval = 1 Day, 1 week, 1 month, 3 month