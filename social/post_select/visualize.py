"""
Post Select — Social Domain
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

# Tweet Distribution by User (Top 10)
df0 = pd.read_sql_query("""SELECT user_id, COUNT(*) as cnt FROM tweets GROUP BY user_id ORDER BY cnt DESC LIMIT 10""", conn)
print(f"Tweet Distribution by User (Top 10): {len(df0)} rows")
print(df0.head())

conn.close()
print("\nDone! All queries executed successfully.")
