select distinct order_status from orders
order by 1;


select * from orders where order_status ='COMPLETE';
select * from orders where order_status ='CLOSED';

select * from orders where order_status ='COMPLETE'
OR ORDER_STATUS='CLOSED';

select * from orders where order_status in ('COMPLETE','CLOSED');

select count(*) from orders;
select count(*) from order_items;
select count(distinct order_status) from orders;
select count(distinct order_date) from orders;
select * from order_items;

select sum(order_item_subtotal)
from order_items
where order_item_order_id=2;

select * from orders;

select order_status, count(*) as order_count
from orders
group by 1
order by 2 desc;


select order_date, count(*) as order_count
from orders
group by 1
order by 2 desc;

select to_char(order_date,'yyyy-MM') AS order_month, count(*) as order_count
from orders
group by 1
order by 2 desc;


select * from order_items;


select order_item_order_id, round(sum(order_item_subtotal)::numeric,2) as order_revenue
from order_items
group by 1
order by 1;

SELECT order_date, count(*) as order_count
FROM orders
WHERE order_status in ('COMPLETE','CLOSED')
GROUP BY 1
	 HAVING count(*) >= 120
ORDER BY 2 desc;

--ORDER OF EXECUTION:
--FROM
--WHERE
--GROUP BY
--SELECT 
--ORDER BY


select order_item_order_id,
	round(sum(order_item_subtotal)::numeric,2) as order_revenue
	from order_items
	group by 1
		having round(sum(order_item_subtotal)::numeric,2) >= 2000
	order by 2 desc;

SELECT  * 
FROM orders as o
	join order_items as oi
		on o.order_id = oi.order_item_order_id;

SELECT count(distinct order_id) from orders;
SELECT count(distinct order_item_order_id) from orders_items;


select o.order_date,
	oi.order_item_product_id,
	round(sum(oi.order_item_subtotal)::numeric,2) as order_revenue
from orders as o
	join order_items as oi
	on o.order_id = oi.order_item_order_id
where o.order_status in ('COMPLETE','CLOSED')
group by 1,2
order by 1,3 desc;

CREATE OR REPLACE VIEW order_details_v
as
select o.*,
	oi.order_item_product_id,
	oi.order_item_subtotal,
	oi.order_item_id
from orders as o
	join order_items as oi
		on o.order_id = oi.order_item_order_id;

select * from order_details_v where order_id=2;


with order_details_cte AS
(select o.*,
	oi.order_item_product_id,
	oi.order_item_subtotal,
	oi.order_item_id
from orders as o
	join order_items as oi
		on o.order_id = oi.order_item_order_id)
select * from order_details_cte;

select * from order_items;


select * from order_details_v;
select * from products;


select *
from products as p
	left outer join order_details_v as odv
    on p.product_id = odv.order_item_product_id
	where to_char(odv.order_date::timestamp, 'yyyy-MM') = '2014-01'
		and odv.order_item_product_id is NULL;

select *
from products as p
	left outer join order_details_v as odv
    on p.product_id = odv.order_item_product_id
		and to_char(odv.order_date::timestamp, 'yyyy-MM') = '2014-01'
	where odv.order_item_product_id is NULL;