SELECT 
    customer_id,
    SUM(sale_amount) AS customer_sales,
    SUM(SUM(sale_amount)) OVER () AS total_sales,
    (SUM(sale_amount) * 100.0 / SUM(SUM(sale_amount)) OVER ()) AS percent_of_total
FROM sales
GROUP BY customer_id;
