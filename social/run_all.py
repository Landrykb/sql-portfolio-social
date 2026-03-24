"""
Social Domain — Run All Solved Queries
BleepxQuery SwiftLink Training Program
"""
import sqlite3
import pandas as pd
import os

# Load datasets
conn = sqlite3.connect(':memory:')
datasets_dir = os.path.join(os.path.dirname(__file__), 'datasets')
pd.read_csv(os.path.join(datasets_dir, 'tweets_sample.csv')).to_sql('tweets', conn, index=False, if_exists='replace')
pd.read_csv(os.path.join(datasets_dir, 'users_sample.csv')).to_sql('users', conn, index=False, if_exists='replace')

print("Datasets loaded. Running queries...\n")

queries = {
    'post_select': """SELECT tweet_id, created_at, text
FROM tweets
WHERE text LIKE '%#SQL%'
ORDER BY created_at DESC
LiMIT 5
""",
    'engagement_by_type': """SELECT 
  t.tweet_id,
  t.created_at, u.user_name
  FROM tweets t
LEFT JOIN users u ON t.user_id = u.user_id
  ORDER BY created_at DESC
  LIMIT 5;
""",
    'user_joins': """SELECT u.user_name, COUNT(t.tweet_id) AS tweet_count
  FROM tweets t
  JOIN users u ON t.user_id = u.user_id
  GROUP BY u.user_name
  ORDER BY tweet_count DESC
LIMIT 5;

  """,
    'likes_trend': """SELECT strftime('%Y-%m', created_at) AS month, COUNT(*) AS tweet_count
FROM tweets
GROUP BY month 
ORDER BY month DESC;

""",
    'cte_engagement': """WITH TweetLengths AS (
  SELECT t.user_id, LENGTH(t.text) AS text_length
  FROM tweets t
)
SELECT u.user_name, AVG(tl.text_length) AS avg_text_length
FROM TweetLengths tl
JOIN users u ON tl.user_id = u.user_id
GROUP BY u.user_name
ORDER BY avg_text_length DESC;""",
    'capstone_social': """WITH TweetStats AS (
  SELECT user_id, 
  COUNT(*) AS tweet_count 
  FROM tweets 
  GROUP BY user_id
),
UserStats AS (
  SELECT user_id, user_name FROM users
)
SELECT 
  us.user_name,
  ts.tweet_count
  FROM TweetStats ts 
  JOIN UserStats us ON ts.user_id = us.user_id
ORDER BY tweet_count DESC;

""",
    'hidden_influencer_roi': """ WITH UserActivity AS (
  SELECT u.user_id, u.user_name, u.signup_date,
  COUNT(t.tweet_id) AS total_posts,
  ROUND(AVG(LENGTH(t.text)), 1) AS avg_content_length, 
  MAX(LENGTH(t.text)) AS max_content_length,
  MIN(t.created_at) AS first_post_date
  FROM users u
  INNER JOIN tweets t ON u.user_id = t.user_id
  GROUP BY u.user_id, u.user_name, u.signup_date
)
SELECT user_name,
   total_posts,
   avg_content_length,
   max_content_length,
   signup_date,
   first_post_date,
   CAST(JUlIANDAY(first_post_date) - JUlIANDAY(signup_date) AS INTEGER) AS days_to_first_post,
   CASE 
     WHEN avg_content_length > 30 AND JULIANDAY(first_post_date) - JULIANDAY(signup_date) < 30 THEN "Tier 1 —  Top Creator"
     WHEN avg_content_length > 20  THEN "Tier 2 — Active Creator"
     WHEN total_posts >= 1 THEN "Tier 3 —  Casual"
     ELSE "Skip" 
   END AS campaign_tier
   FROM UserActivity
   ORDER BY avg_content_length DESC, days_to_first_post ASC 
   LIMIT 15""",
    'hidden_viral_prediction': """WITH UserMetrics AS (
  SELECT
    t.user_id,
    u.user_name,
    u.signup_date,
    t.created_at AS post_date,
    LENGTH(t.text) AS content_length,
    ROUND(JULIANDAY(t.created_at) - JULIANDAY(u.signup_date)) AS days_to_first_post
  FROM tweets t
  JOIN users u ON t.user_id = u.user_id
),
Ranked AS (
  SELECT
    user_id,
    user_name,
    signup_date,
    post_date,
    content_length,
    days_to_first_post,
    RANK() OVER (ORDER BY days_to_first_post ASC) AS speed_rank,
    CASE
      WHEN days_to_first_post <= 30 THEN 'Early Adopter'
      WHEN days_to_first_post <= 90 THEN 'Quick Starter'
      WHEN days_to_first_post <= 180 THEN 'Steady User'
      ELSE 'Late Bloomer'
    END AS engagement_tier,
    CASE
      WHEN content_length >= 40 THEN 'Long Form'
      WHEN content_length >= 20 THEN 'Standard'
      ELSE 'Short Form'
    END AS content_type
  FROM UserMetrics
  WHERE days_to_first_post >= 0
)
SELECT
  user_id,
  user_name,
  signup_date,
  post_date,
  content_length,
  days_to_first_post,
  speed_rank,
  engagement_tier,
  content_type
FROM Ranked
WHERE speed_rank <= 20
ORDER BY speed_rank;""",
}

for name, sql in queries.items():
    try:
        df = pd.read_sql_query(sql, conn)
        print(f"✓ {name}: {len(df)} rows")
    except Exception as e:
        print(f"✗ {name}: {e}")

conn.close()
print("\nDone!")
