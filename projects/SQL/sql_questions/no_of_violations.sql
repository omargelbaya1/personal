-- You are given a dataset of health inspections that includes details about violations. Each row represents an inspection, and if an inspection resulted in a violation, the violation_id column will contain a value.
-- Count the total number of violations that occurred at 'Roxanne Cafe' for each year, based on the inspection date. Output the year and the corresponding number of violations in ascending order of the year.

--my solution:
select extract(year from inspection_date :: DATE) as inspection_year, count(*) as violations from sf_restaurant_health_violations where business_name='Roxanne Cafe'
group by 1 
order by 1 asc;

--can also use date_part as below:
SELECT EXTRACT (YEAR FROM inspection_date :: DATE) AS inspection_year,
       COUNT(violation_id) AS n_violations
FROM sf_restaurant_health_violations
WHERE business_name = 'Roxanne Cafe'
GROUP BY inspection_year
ORDER BY inspection_year ASC;