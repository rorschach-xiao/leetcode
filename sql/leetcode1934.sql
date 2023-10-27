# WITH new_confirmations AS (SELECT s.user_id, c.time_stamp, c.action
#                              FROM Signups s LEFT JOIN Confirmations c
#                                             ON s.user_id = c.user_id),
# total_request_table AS (SELECT user_id, COUNT(*) as count
#                       FROM new_confirmations
#                       GROUP BY user_id),
# confirmed_table AS (SELECT user_id, COUNT(*) as count
#                       FROM new_confirmations
#                      WHERE action IS NOT NULL AND action='confirmed'
#                       GROUP BY user_id)
#
# SELECT t.user_id, ROUND(COALESCE(c.count, 0)/t.count, 2) AS confirmation_rate
#   FROM total_request_table t LEFT JOIN confirmed_table c ON t.user_id = c.user_id
WITH new_confirmations AS (SELECT s.user_id, c.time_stamp, IF(c.action='confirmed',1,0)status
                             FROM Signups s LEFT JOIN Confirmations c
                                            ON s.user_id = c.user_id)
SELECT user_id, ROUND(AVG(status), 2) AS confirmation_rate
  FROM new_confirmations
 GROUP BY user_id