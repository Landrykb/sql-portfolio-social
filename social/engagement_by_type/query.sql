-- Engagement By Type
-- Domain: Social
-- Level: Intermediate
-- BleepxQuery SwiftLink Training Program
--
-- Attempts: 6
-- Solve Time: 54m 20s
-- Date: 3/5/2026

SELECT 
  t.tweet_id,
  t.created_at, u.user_name
  FROM tweets t
LEFT JOIN users u ON t.user_id = u.user_id
  ORDER BY created_at DESC
  LIMIT 5;

