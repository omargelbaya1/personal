EXPLAIN
SELECT * FROM orders where order_id=2;

EXPLAIN
SELECT o.*,
	round(sum(oi.order_item_subtotal)::numeric,2) as revenue
FROM orders AS o
	JOIN order_items AS oi
		ON o.order_id = oi.order_item_order_id
where o.order_id=2
GROUP by o.order_id,
	o.order_date,
	o.order_customer_id,
	o.order_status;


DROP INDEX orders_order_date_idx;
DROP INDEX order_items_oid_idx;

ALTER TABLE order_items add 
	FOREIGN KEY (order_item_order_id) REFERENCES orders(order_id);



ALTER TABLE orders
	ADD FOREIGN KEY (order_customer_id)
		REFERENCES customers(customer_id);

CREATE INDEX order_order_customer_id_idx
ON orders(order_customer_id);

CREATE INDEX order_items_order_item_order_id_idx
ON order_items (order_item_order_id);




commit;


