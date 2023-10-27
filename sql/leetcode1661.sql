WITH activity_start AS (SELECT * FROM Activity WHERE activity_type='start'),
activity_end AS (SELECT * FROM Activity WHERE activity_type='end')
SELECT a1.machine_id, ROUND(AVG(a2.timestamp - a1.timestamp),3) AS processing_time
  FROM activity_start a1 JOIN activity_end a2
                         ON (a1.machine_id=a2.machine_id AND a1.process_id=a2.process_id)
 GROUP BY a1.machine_id
