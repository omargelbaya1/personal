--Find the review_text that received the highest number of  cool votes.
--Output the business name along with the review text with the highest number of cool votes.



--MY SOLUTION:
select business_name,review_text from yelp_reviews
where cool = (select max(cool) from yelp_reviews);



-- could also do this but it seems like it might be a big hard coded:
-- NOT A GOOD SOLUTION:
select business_name, review_text
from yelp_reviews
order by cool desc, business_name
limit 2


--other solutions:
WITH cte AS (select business_name, review_text, DENSE_RANK()OVER(ORDER BY SUM(cool) DESC) as cool_rk from yelp_reviews GROUP BY 1,2)
SELECT business_name, review_text FROM cte
WHERE cool_rk = 1;