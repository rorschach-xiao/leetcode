WITH first_delivery AS (SELECT * FROM Delivery d1
                        WHERE order_date = (SELECT MIN(order_date)
                                              FROM Delivery d2
                                              WHERE d2.customer_id = d1.customer_id
                                              GROUP BY d2.customer_id )
)
SELECT ROUND(SUM(IF(order_date=customer_pref_delivery_date,1,0))/COUNT(*) * 100, 2) AS immediate_percentage
  FROM first_delivery