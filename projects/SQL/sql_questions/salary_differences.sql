--Calculates the difference between the highest salaries in the marketing and engineering departments.
--Output just the absolute difference in salaries.

--my solution:
select max(salary)-(select max(salary) from db_employee e
join db_dept d on e.department_id=d.id
where d.department='engineering') as difference from db_employee e
join db_dept d on e.department_id=d.id
where d.department='marketing'
;

--better solutions:
select abs(max(salary) filter (where department = 'marketing') - max(salary) filter (where department = 'engineering'))
from db_employee emp
LEFT JOIN db_dept dept on emp.department_id = dept.id


SELECT ABS(MAX(CASE
                   WHEN dept.department = 'marketing' THEN emp.salary
               END) - MAX(CASE
                              WHEN dept.department = 'engineering' THEN emp.salary
                          END)) AS salary_difference
FROM db_employee emp
JOIN db_dept dept ON emp.department_id = dept.id
WHERE dept.department IN ('marketing',
                          'engineering');


with cte as (
    select department_id, max(salary) as salary
    from db_employee as e
    join db_dept as d
    on d.id = e.department_id
    where d.department in ('marketing', 'engineering')
    group by department_id
)

select max(salary)-min(salary) as salary_diff from cte