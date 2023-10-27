WITH new_employee AS (SELECT e1.id, e1.name, e1.managerId, COUNT(e1.id) as reports
                        FROM Employee e1 LEFT JOIN Employee e2 ON e1.id = e2.managerId
                       WHERE e2.id IS NOT NULL
                    GROUP BY e1.id)
SELECT name FROM new_employee WHERE reports >= 5