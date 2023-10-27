SELECT p.product_id, IF(units IS NULL, 0, ROUND(SUM(price*units)/SUM(units), 2)) AS average_price
  FROM Prices p LEFT JOIN UnitsSold u ON u.product_id = p.product_id
 WHERE u.purchase_date IS NULL OR u.purchase_date <= p.end_date AND u.purchase_date >= p.start_date
GROUP BY p.product_id