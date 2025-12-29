--Find the most profitable company from the financial sector. Output the result along with the continent.

--my solution:
select company,continent from 
forbes_global_2010_2014 where 
profits=
(select max(profits) from forbes_global_2010_2014 where sector='Financials')

--other solutions:
WITH max_profits AS
  (SELECT MAX(profits) AS max_profit
   FROM forbes_global_2010_2014
   WHERE sector = 'Financials')
SELECT company,
       continent
FROM forbes_global_2010_2014
JOIN max_profits ON forbes_global_2010_2014.profits = max_profits.max_profit
WHERE sector = 'Financials';

select company,continent,profits as most_profitble
from forbes_global_2010_2014
where sector='Financials'
order by profits desc
limit 1

select company,continent from forbes_global_2010_2014 where sector = 'Financials'
and profits = (select max(profits) from forbes_global_2010_2014);
