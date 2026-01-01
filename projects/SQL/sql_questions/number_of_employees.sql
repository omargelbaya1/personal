--Find the number of employees working in the Admin department that joined in April or later, in any year.


select count(*) as n_admins 
from worker 
where lower(department) ='admin' and extract(month from joining_date) >= 4 ;


--OR


SELECT COUNT(*) AS n_admins
FROM worker
WHERE lower(department) LIKE 'admin'
  AND EXTRACT(MONTH
              FROM joining_date) >= 4