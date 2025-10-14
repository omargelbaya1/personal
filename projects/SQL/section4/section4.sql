select * from information_schema.tables;


CREATE DATABASE itversity_retail_db;
CREATE USER itversity_retail_user with ENCRYPTED PASSWORD 'r3k957b8';


GRANT ALL ON DATABASE itversity_retail_db TO itversity_retail_user;

ALTER DATABASE itversity_retail_db OWNER TO itversity_retail_user;

select count(*)from departments;
select count(*)from categories;
select count(*)from customers;
select count(*)from order_items;
select count(*)from orders;
select count(*)from products;

select * from orders LIMIT 10;