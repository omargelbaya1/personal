--this one is quite difficult but i just need to start nesting queries within queries:

--Management wants to analyze only employees with official job titles.
--Find the job titles of the employees with the highest salary.
--If multiple employees have the same highest salary, include all their job titles.
SELECT b.worker_title AS best_paid_title
FROM worker a
JOIN title b ON a.worker_id = b.worker_ref_id
WHERE a.salary = (
    SELECT MAX(w.salary)
    FROM worker w
    JOIN title t ON w.worker_id = t.worker_ref_id
    WHERE t.worker_title IS NOT NULL
)
ORDER BY best_paid_title;

--variaton that no longer works but its quite simple, i think its because the title might be null in one
--of the tables
SELECT
    worker_title AS best_paid_title
FROM worker
JOIN title
ON worker_id = worker_ref_id
WHERE salary=(SELECT MAX(salary) FROM worker)
