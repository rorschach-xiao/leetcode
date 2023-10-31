WITH teacher_subject AS (SELECT DISTINCT teacher_id, subject_id FROM Teacher)
SELECT teacher_id, COUNT(*) AS cnt
  FROM teacher_subject
 GROUP BY teacher_id