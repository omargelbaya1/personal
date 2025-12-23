-- Find the last time each bike was in use. Output both the bike 
-- number and the date-timestamp of the bike's last use (i.e., the date-time the bike was returned). Order the results by bikes that were most recently used.

-- Table
-- dc_bikeshare_q1_2012

--my solution:
select bike_number,max(end_time) as last_used from dc_bikeshare_q1_2012
group by 1
order by 2 desc;


--another exmaple of solution:
SELECT BIKE_NUMBER, END_TIME FROM (
select *,
      DENSE_RANK() OVER ( PARTITION BY BIKE_NUMBER ORDER BY END_TIME DESC) AS RNK
from dc_bikeshare_q1_2012 ) X
WHERE RNK=1
ORDER BY BIKE_NUMBER