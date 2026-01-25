--Meta/Facebook has developed a new programing language called Hack.
--To measure the popularity of Hack they ran a survey with their employees.
--The survey included data on previous programing familiarity as well as the number of years of experience, age, gender and most importantly satisfaction with Hack.
--Due to an error location data was not collected, but your supervisor demands a report showing average popularity of Hack by office location.
--Luckily the user IDs of employees completing the surveys were stored.
--Based on the above, find the average popularity of the Hack per office location.
--Output the location along with the average popularity.

--My code:
select fe.location, avg(fhs.popularity)
from  facebook_employees  as fe
join facebook_hack_survey as fhs on fe.id=fhs.employee_id
group by 1;


--Other variations:
SELECT e.location,
       AVG(s.popularity) AS avg_popularity
FROM facebook_employees e
JOIN facebook_hack_survey s ON e.id = s.employee_id
GROUP BY e.location

--
select avg(popularity), location
from facebook_employees e
join facebook_hack_survey h
on e.id = h.employee_id
group by location;