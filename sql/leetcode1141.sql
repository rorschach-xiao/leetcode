WITH thirdty_days_activity AS (SELECT user_id, activity_date
                                FROM Activity
                                WHERE activity_date <= DATE_FORMAT("2019-07-27", "%Y-%m-%d")
                                      AND activity_date > ADDDATE("2019-07-27", INTERVAL -30 DAY))
SELECT activity_date AS day, COUNT(DISTINCT user_id) AS active_users
  FROM thirdty_days_activity
 GROUP BY activity_date