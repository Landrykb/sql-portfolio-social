-- User Joins
-- Domain: Social
-- Level: Advanced
-- BleepxQuery SwiftLink Training Program
--
-- Attempts: 8
-- Solve Time: 49m 15s
-- Date: 3/5/2026

SELECT u.user_name, COUNT(t.tweet_id) AS tweet_count
  FROM tweets t
  JOIN users u ON t.user_id = u.user_id
  GROUP BY u.user_name
  ORDER BY tweet_count DESC
LIMIT 5;

  
