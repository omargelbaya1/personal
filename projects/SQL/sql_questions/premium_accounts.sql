--You have a dataset that records daily active users for each premium account. A premium account appears in the data every day as long as it remains premium. However, some premium accounts may be temporarily discounted, meaning they are not actively paying — this is indicated by a final_price of 0.
--
--
--For each date, count the number of premium accounts that were actively paying on that day. Then, track how many of those same accounts are still premium and actively paying exactly 7 days later, if that later date exists in the dataset. Return results for the first 7 dates in the dataset.
--
--
--Output three columns:
--•   The date of initial calculation.
--•   The number of premium accounts that were actively paying on that day.
--•   The number of those accounts that remain premium and are still paying after 7 days.

--final solution:

select a.entry_date, count(a.account_id),count(b.account_id) from premium_accounts_by_day a
left join premium_accounts_by_day b
on a.account_id = b.account_id
and b.final_price>0
and (b.entry_date - a.entry_date) = 7

where a.final_price>0
group by 1
order by 1 asc
limit 7

--other solution:
WITH premium_accounts AS (
    SELECT
        entry_date,
        account_id,
        final_price
    FROM premium_accounts_by_day
    WHERE final_price > 0
)
SELECT
    a.entry_date,
    COUNT(DISTINCT a.account_id) AS premium_paid_accounts,
    COUNT(DISTINCT b.account_id) AS premium_paid_accounts_after_7d
FROM premium_accounts a
LEFT JOIN premium_accounts b
    ON a.account_id = b.account_id
   AND (b.entry_date - a.entry_date) = 7
GROUP BY a.entry_date
ORDER BY a.entry_date
LIMIT 7;


--other:
with valid_dates as (
select distinct(entry_date) as entry_date
from premium_accounts_by_day
order by entry_date asc
limit 7
)

select p.entry_date, SUM(CASE WHEN p.account_id is not null and p.final_price > 0 THEN 1 ELSE 0 END) as premium_paid_accounts,
       SUM(CASE WHEN (p.account_id is not null and p.final_price > 0) and
                    (s.account_id is not null and s.final_price > 0) THEN 1 ELSE 0 END) as premium_paid_accounts_after_7d
from premium_accounts_by_day p
left join premium_accounts_by_day s
on p.entry_date + 7= s.entry_date
and p.account_id = s.account_id
where p.entry_date in (select entry_date from valid_dates)
group by 1
order by p.entry_date asc

o