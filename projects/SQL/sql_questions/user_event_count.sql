-- -- Count the number of user events performed by MacBookPro users.
-- Output the result along with the event name.
-- Sort the result based on the event count in the descending order.

select 
event_name , count(*) as event_count 
from 
playbook_events
where device in ('macbook pro')
group by 1
order by 2 desc;
