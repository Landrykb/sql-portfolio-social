-- Hidden Viral Prediction
-- Domain: Social
-- Level: Master
-- BleepxQuery SwiftLink Training Program
--
-- Attempts: 4
-- Date: 3/24/2026

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
