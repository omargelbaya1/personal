--We have a table with employees and their salaries, however, some of the records are old and contain outdated salary information.
--Find the current salary of each employee assuming that salaries increase each year.
--Output their id, first name, last name, department ID, and current salary.
--Order your list by employee ID in ascending order.

--now my solution should work but it doesnt take into account what if the user moves to a new department, so this method is the best:

SELECT id, first_name, last_name, department_id, salary
FROM (
    SELECT *,
           ROW_NUMBER() OVER(PARTITION BY id ORDER BY salary DESC) AS rn
    FROM ms_employee_salary
) AS t -- "t" is an alias for the subquery (required for SQL syntax)
WHERE t.rn = 1
ORDER BY id;


--my solution:

select id,first_name,last_name,department_id,max(salary) as current_salary from ms_employee_salary
group by 1,2,3,4
order by 1 asc;