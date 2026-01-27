--Calculate the percentage of users who are both from the US and have an 'open' status, as indicated in the fb_active_users table.

--my solution:
select
(select count(*)
from fb_active_users
where country='USA'
and status='open') / count(*)::numeric*100
as percentage from fb_active_users;


--other better solutions:
--share= "open"/"total"

select 1.00*count(case when status = 'open' then 1 else NULL end)/count(*) as share
from fb_active_users
where country = 'USA'


select AVG(CASE WHEN status = 'open' THEN 1 ELSE 0 END) active_users_share from fb_active_users
WHERE country = 'USA';