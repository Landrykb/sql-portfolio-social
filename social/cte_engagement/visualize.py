"""
Cte Engagement — Social Domain
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

# Top Users by Tweet Count (CTE)
df0 = pd.read_sql_query("""WITH UserStats AS (SELECT user_id, COUNT(*) as tweet_count FROM tweets GROUP BY user_id) SELECT user_id, tweet_count FROM UserStats ORDER BY tweet_count DESC LIMIT 10""", conn)
print(f"Top Users by Tweet Count (CTE): {len(df0)} rows")
print(df0.head())

conn.close()
print("\nDone! All queries executed successfully.")
