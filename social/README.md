# Social SQL Analytics Portfolio

## About
SQL data analysis projects completed through the **BleepxQuery SwiftLink Training Program**.

| Metric | Value |
|--------|-------|
| Domain | **Social** |
| Challenges Solved | **8/8** (100%) |
| Avg Solve Time | **52m 10s** |
| Best Solve Time | **49m 15s** |
| First-Try Solves | **0/8** |
| Visualizations | **8** charts |

## Skills Demonstrated
- **Core SQL:** SELECT, WHERE, ORDER BY, LIMIT, DISTINCT
- **Aggregation:** GROUP BY, HAVING, COUNT, SUM, AVG, MAX, MIN
- **Joins:** INNER JOIN, LEFT JOIN, multi-table joins
- **Advanced:** Window Functions (RANK, LAG, LEAD), CTEs, Subqueries
- **Analysis:** CASE expressions, date functions, percentage calculations
- **Real-world:** Social industry data analysis & problem solving

## Datasets
### tweets
- **Rows:** 10,000
- **Columns:** 4
- **Schema:** `tweet_id`, `user_id`, `created_at`, `text`
- **Preview:**

| tweet_id | user_id | created_at | text |
| --- | --- | --- | --- |
| TW1 | U1 | 2023-09-04 | Sample tweet #SQL |
| TW2 | U2 | 2023-11-25 | Sample tweet #AgriTech |
| TW3 | U3 | 2023-10-01 | Sample tweet #Analytics |

### users
- **Rows:** 10,000
- **Columns:** 3
- **Schema:** `user_id`, `user_name`, `signup_date`
- **Preview:**

| user_id | user_name | signup_date |
| --- | --- | --- |
| U1 | User_1 | 2022-10-23 |
| U2 | User_2 | 2022-06-11 |
| U3 | User_3 | 2022-04-29 |


## Projects

### 1. [Post Select](./post_select/query.sql) 📊
- **Level:** Beginner ⭐
- **Attempts:** 3
- **Solve Time:** 53m 38s

```sql
SELECT tweet_id, created_at, text
FROM tweets
WHERE text LIKE '%#SQL%'
ORDER BY created_at DESC
LiMIT 5

```

### 2. [Engagement By Type](./engagement_by_type/query.sql) 📊
- **Level:** Intermediate ⭐⭐
- **Attempts:** 6
- **Solve Time:** 54m 20s

```sql
SELECT 
  t.tweet_id,
  t.created_at, u.user_name
  FROM tweets t
LEFT JOIN users u ON t.user_id = u.user_id
  ORDER BY created_at DESC
  LIMIT 5;

```

### 3. [User Joins](./user_joins/query.sql) 📊
- **Level:** Advanced ⭐⭐⭐
- **Attempts:** 8
- **Solve Time:** 49m 15s

```sql
SELECT u.user_name, COUNT(t.tweet_id) AS tweet_count
  FROM tweets t
  JOIN users u ON t.user_id = u.user_id
  GROUP BY u.user_name
  ORDER BY tweet_count DESC
LIMIT 5;

  
```

### 4. [Likes Trend](./likes_trend/query.sql) 📊
- **Level:** Advanced ⭐⭐⭐
- **Attempts:** 5
- **Solve Time:** 52m 53s

```sql
SELECT strftime('%Y-%m', created_at) AS month, COUNT(*) AS tweet_count
FROM tweets
GROUP BY month 
ORDER BY month DESC;


```

### 5. [Cte Engagement](./cte_engagement/query.sql) 📊
- **Level:** Expert ⭐⭐⭐⭐
- **Attempts:** 4
- **Solve Time:** 50m 43s

```sql
WITH TweetLengths AS (
  SELECT t.user_id, LENGTH(t.text) AS text_length
  FROM tweets t
)
SELECT u.user_name, AVG(tl.text_length) AS avg_text_length
FROM TweetLengths tl
JOIN users u ON tl.user_id = u.user_id
GROUP BY u.user_name
ORDER BY avg_text_length DESC;
```

### 6. [Capstone Social](./capstone_social/query.sql) 📊
- **Level:** Master ⭐⭐⭐⭐⭐
- **Attempts:** 6


```sql
WITH TweetStats AS (
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


```

### 7. [Hidden Influencer Roi](./hidden_influencer_roi/query.sql) 📊
- **Level:** Master ⭐⭐⭐⭐⭐
- **Attempts:** 19


```sql
 WITH UserActivity AS (
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
   LIMIT 15
```

### 8. [Hidden Viral Prediction](./hidden_viral_prediction/query.sql) 📊
- **Level:** Master ⭐⭐⭐⭐⭐
- **Attempts:** 4


```sql
WITH UserMetrics AS (
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
ORDER BY speed_rank;
```


## How to Run
1. Load the CSV datasets into any SQL database (SQLite, PostgreSQL, etc.)
2. Run each query against the loaded tables
3. Each challenge folder contains: `query.sql`, `README.md`, and visualization code
4. Run `python run_all.py` to execute all queries (requires Python + SQLite)

---
*Generated by [BleepxQuery](https://bleepxacademy.vercel.app) — SwiftLink Training Program*
