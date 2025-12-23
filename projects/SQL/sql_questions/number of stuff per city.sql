-- Find the average number of bathrooms and bedrooms for each city’s property types.
--  Output the result along with the city name and the property type.
 --my solution:

select city,property_type,avg(bathrooms),avg(bedrooms) from airbnb_search_details

group by 1,2;

-- other solution:
SELECT city, property_type, avg(bedrooms) as n_bedrooms_avg, avg(bathrooms) as n_bathrooms_avg
FROM airbnb_search_details
GROUP BY city, property_type
ORDER BY city