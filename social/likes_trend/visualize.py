"""
Likes Trend — Social Domain
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

# Cumulative Tweets Over Time
df0 = pd.read_sql_query("""SELECT created_at, COUNT(*) OVER (ORDER BY created_at) as cumulative_tweets FROM tweets""", conn)
print(f"Cumulative Tweets Over Time: {len(df0)} rows")
print(df0.head())

conn.close()
print("\nDone! All queries executed successfully.")
