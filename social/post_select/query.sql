-- Post Select
-- Domain: Social
-- Level: Beginner
-- BleepxQuery SwiftLink Training Program
--
-- Attempts: 3
-- Solve Time: 53m 38s
-- Date: 3/5/2026

SELECT tweet_id, created_at, text
FROM tweets
WHERE text LIKE '%#SQL%'
ORDER BY created_at DESC
LiMIT 5

