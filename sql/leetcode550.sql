WITH first_logged_in_players AS (SELECT player_id,
                                        MIN(event_date) as min_event_date
                                   FROM Activity
                                   GROUP BY player_id),
     logged_in_again_players AS (SELECT player_id
                                   FROM first_logged_in_players
                                  WHERE (player_id, ADDDATE(min_event_date, INTERVAL 1 DAY))
                                        IN (SELECT player_id, event_date FROM Activity)
                                )
SELECT ROUND((SELECT COUNT(DISTINCT player_id) FROM logged_in_again_players) / COUNT(DISTINCT player_id), 2) AS fraction
  FROM Activity