"""
Engagement By Type — Social Domain
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

# Engagement: Tweets per User
df0 = pd.read_sql_query("""SELECT user_id, COUNT(*) as tweet_count, ROUND(AVG(LENGTH(text)),1) as avg_length FROM tweets GROUP BY user_id ORDER BY tweet_count DESC LIMIT 15""", conn)
print(f"Engagement: Tweets per User: {len(df0)} rows")
print(df0.head())

conn.close()
print("\nDone! All queries executed successfully.")
