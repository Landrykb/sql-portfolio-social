-- Cte Engagement
-- Domain: Social
-- Level: Expert
-- BleepxQuery SwiftLink Training Program
--
-- Attempts: 4
-- Solve Time: 50m 43s
-- Date: 3/5/2026

WITH TweetLengths AS (
  SELECT t.user_id, LENGTH(t.text) AS text_length
  FROM tweets t
)
SELECT u.user_name, AVG(tl.text_length) AS avg_text_length
FROM TweetLengths tl
JOIN users u ON tl.user_id = u.user_id
GROUP BY u.user_name
ORDER BY avg_text_length DESC;
