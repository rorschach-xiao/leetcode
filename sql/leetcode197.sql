WITH sorted_weather AS (SELECT * FROM Weather ORDER BY recordDate)
SELECT w2.id
  FROM sorted_weather w1 RIGHT JOIN sorted_weather w2
                                 ON w2.recordDate = ADDDATE(w1.recordDate, INTERVAL 1 DAY)
  WHERE w2.temperature > w1.temperature