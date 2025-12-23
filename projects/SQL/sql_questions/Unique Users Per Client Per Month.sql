-- Write a query that returns the number of unique users per client for each month. 
--Assume all events occur within the same year, s
--so only month needs to be be in the output as a number from 1 to 12.

-- Table
-- fact_events

--my solution:
select client_id,date_part('month',time_id) as month,count( distinct user_id) as users_num from fact_events
group by 1,2
order by 1 asc;


-- another example of solution:
SELECT client_id, EXTRACT(month from time_id) as month, COUNT(DISTINCT user_id) as users_per_month
FROM fact_events
GROUP BY client_id, month;

-- can you extract function, its faster than date_part