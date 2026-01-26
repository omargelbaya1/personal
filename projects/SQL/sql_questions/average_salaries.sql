--Compare each employee's salary with the average salary of the corresponding department.
--Output the department, first name, and salary of employees along with the average salary of that department.

select department,first_name,salary,avg(salary) over(partition by department) from employee
group by 1 ,2 ,3;


--or

select e.department, first_name, salary, avg_salary from employee e
join (
select department, avg(salary) as avg_salary from employee group by department) d
on e.department=d.department