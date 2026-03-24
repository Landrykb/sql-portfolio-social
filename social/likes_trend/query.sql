-- Likes Trend
-- Domain: Social
-- Level: Advanced
-- BleepxQuery SwiftLink Training Program
--
-- Attempts: 5
-- Solve Time: 52m 53s
-- Date: 3/5/2026

SELECT strftime('%Y-%m', created_at) AS month, COUNT(*) AS tweet_count
FROM tweets
GROUP BY month 
ORDER BY month DESC;


