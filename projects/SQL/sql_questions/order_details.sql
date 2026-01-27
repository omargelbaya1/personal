--Find order details made by Jill and Eva.
--Consider the Jill and Eva as first names of customers.
--Output the order date, details and cost along with the first name.
--Order records based on the customer id in ascending order.

--my solution:

select c.first_name,o.order_date,o.order_details,o.total_order_cost from customers c
join orders o on c.id=o.cust_id
where c.first_name in ('Jill','Eva')
order by c.id asc


