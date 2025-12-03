CREATE TABLE courses (
    course_id SERIAL PRIMARY KEY,
    course_name VARCHAR(60),
    course_author VARCHAR(40),
    course_status VARCHAR(9),
    course_published_dt DATE
);

INSERT INTO courses
    (course_name, course_author, course_status, course_published_dt)
VALUES
    ('Programming using Python', 'Bob Dillon', 'published', '2020-09-30'),
    ('Data Engineering using Python', 'Bob Dillon', 'published', '2020-07-15'),
    ('Data Engineering using Scala', 'Elvis Presley', 'draft', null),
    ('Programming using Scala' , 'Elvis Presley' , 'published' , '2020-05-12'),
    ('Programming using Java' , 'Mike Jack' , 'inactive' , '2020-08-10'),
    ('Web Applications - Python Flask' , 'Bob Dillon' , 'inactive' , '2020-07-20'),
    ('Web Applications - Java Spring' , 'Bob Dillon' , 'draft' , null),
    ('Pipeline Orchestration - Python' , 'Bob Dillon' , 'draft' , null),
    ('Streaming Pipelines - Python' , 'Bob Dillon' , 'published' , '2020-10-05'),
    ('Web Applications - Scala Play' , 'Elvis Presley' , 'inactive' , '2020-09-30'),
    ('Web Applications - Python Django' , 'Bob Dillon' , 'published' , '2020-06-23'),
    ('Server Automation - Ansible' , 'Uncle Sam' , 'published' , '2020-07-05');

SELECT * FROM courses ORDER BY course_id;


select * from courses where course_status in('inactive','draft');
select * from courses where course_name like '%Python%' or course_name like '%Scala%';
select count(*) ,course_status from courses group by course_status;
select count(*), course_author from courses where course_status='published' group by course_author ;
select * from courses where (course_name like '%Python%' or course_name like '%Scala%') and course_status='draft';
select count(course_status) as xdf, course_author from courses where course_status='published'
group by course_author
	having count(*)>1;

SELECT * FROM departments;
SELECT * FROM categories;
SELECT * FROM products;
SELECT * FROM orders;
SELECT * FROM order_items;
SELECT * FROM customers;

select
count(*) as customer_order_count,
c.customer_id,
c.customer_fname,
c.customer_lname
from 
	orders as o
	join customers as c on o.order_customer_id=c.customer_id
	where (to_char(o.order_date,'YYYY-MM')) ='2014-01'
	group by c.customer_id
	order by 1 desc, 2 asc;



SELECT c.*
FROM customers AS c
WHERE c.customer_id NOT IN (
    SELECT o.order_customer_id
    FROM orders AS o
    WHERE o.order_customer_id = c.customer_id
        AND to_char(order_date, 'yyyy-MM') = '2014-01'
)
ORDER BY 1
LIMIT 10;

select * from order_items;
select * from orders;
select * from customers;




select
sum(oi.order_item_subtotal) as customer_revenue,
c.customer_id,
c.customer_fname,
c.customer_lname
FROM orders as o
	left outer join customers as c on o.order_customer_id = c.customer_id
	left outer join order_items as oi on o.order_id=oi.order_item_order_id
	where order_status in ('CLOSED','COMPLETE') and (to_char(o.order_date,'YYYY-MM')) ='2014-01'
	group by 2 ,3,4
	order by 1 desc, 2 asc;



-- Get the revenue generated for each category for the month of 2014 January
-- * Tables - `orders`, `order_items`, `products` and `categories`
-- * Data should be sorted in ascending order by `category_id`.
-- * Output should contain all the fields from `categories` along with the revenue as `category_revenue`.
-- * Consider only `COMPLETE` and `CLOSED` orders

select * from orders;
select * from order_items;
select * from products;
select * from categories;

select 
c.category_id,
c.category_department_id,
c.category_name,
sum(oi.order_item_subtotal) as category_revenue
from orders as o
	join order_items as oi on o.order_id=oi.order_item_order_id
	join products as p on oi.order_item_product_id =p.product_id
	join categories as c on p.product_category_id=c.category_id
	where order_status in ('CLOSED','COMPLETE') and (to_char(o.order_date,'YYYY-MM')) ='2014-01'
	group by 1,2,3
	order by 1
;


-- ### Exercise 5 - Product Count Per Department

-- Get the count of products for each department.
-- * Tables - `departments`, `categories`, `products`
-- * Data should be sorted in ascending order by `department_id`
-- * Output should contain all the fields from `departments` and the product count as `product_count`

select* from departments;
select * from categories;
select * from products;

select
d.department_id,
d.department_name,
count(*) as product_count
from categories as c 
	join departments as d on d.department_id=c.category_department_id
	join products as p on p.product_category_id=c.category_id
	group by d.department_id
	order by 1;

SELECT d.department_id,
    d.department_name,
    count(*) AS department_count
FROM departments AS d
    JOIN categories AS c
        ON d.department_id = c.category_department_id
    JOIN products AS p
        ON c.category_id = p.product_category_id
GROUP BY 1, 2
ORDER BY 1;
	