-- Hidden Influencer Roi
-- Domain: Social
-- Level: Master
-- BleepxQuery SwiftLink Training Program
--
-- Attempts: 19
-- Date: 3/13/2026

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
