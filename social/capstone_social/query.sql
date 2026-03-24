-- Capstone Social
-- Domain: Social
-- Level: Master
-- BleepxQuery SwiftLink Training Program
--
-- Attempts: 6
-- Date: 3/13/2026

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


