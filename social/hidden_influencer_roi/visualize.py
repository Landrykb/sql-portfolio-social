"""
Hidden Influencer Roi — Social Domain
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

# Top Influencers by Activity
df0 = pd.read_sql_query("""SELECT u.user_name, COUNT(t.tweet_id) as tweets, ROUND(AVG(LENGTH(t.text)),1) as avg_len FROM users u JOIN tweets t ON u.user_id = t.user_id GROUP BY u.user_name ORDER BY tweets DESC LIMIT 10""", conn)
print(f"Top Influencers by Activity: {len(df0)} rows")
print(df0.head())

conn.close()
print("\nDone! All queries executed successfully.")
