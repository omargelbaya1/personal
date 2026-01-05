-- Find the number of workers by department who joined on or after April 1, 2014.


-- Output the department name along with the corresponding number of workers.


-- Sort the results based on the number of workers in descending order.



select department , count(*) as number_of_employees from worker 
where joining_date  >='2014-04-01'

group by 1
order by 2 desc




--or
select 
    department,
    count(*)
from worker
where date_part('month',joining_date)>=4
group by department;

--or

select department, count(1) 
from worker
where EXTRACT(month from joining_date) >= 4
group by department