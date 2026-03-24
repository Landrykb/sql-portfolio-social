"""
Hidden Viral Prediction — Social Domain
BleepxQuery SwiftLink Training Program
"""
import sqlite3
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Load datasets
conn = sqlite3.connect(':memory:')
pd.read_csv('../../datasets/tweets.csv').to_sql('tweets', conn, index=False, if_exists='replace')
pd.read_csv('../../datasets/users.csv').to_sql('users', conn, index=False, if_exists='replace')

# Tweet Volume Trend
df0 = pd.read_sql_query("""SELECT strftime('%Y-%m', created_at) as month, COUNT(*) as tweet_count FROM tweets GROUP BY month ORDER BY month""", conn)
print(f"Tweet Volume Trend: {len(df0)} rows")
print(df0.head())

conn.close()
print("\nDone! All queries executed successfully.")
