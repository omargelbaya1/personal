-- Write a query that will calculate the number of shipments per month. 
-- The unique key for one shipment is a combination of shipment_id and sub_id. Output the year_month in 
-- format YYYY-MM and the number of shipments in that month.


--my solution
select to_char(shipment_date, 'YYYY-MM'),count(shipment_id) from amazon_shipment
group by 1;

--another solution:
SELECT
    TO_CHAR(shipment_date, 'YYYY-MM') AS yyyy_mm,
    COUNT(CONCAT(shipment_id, sub_id)) AS uniq_key
FROM amazon_shipment
GROUP BY
    yyyy_mm