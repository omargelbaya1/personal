--EXERCISE 1

%sql
--can do year(created_ts) instead
select distinct date_format(created_ts,'yyyy') as created_year , count(*) as user_count from users
group by 1
order by 1 asc


%sql
--EXERICSE2
-- can do month(user_dob) or dayofweek(user_dob) for the order clause instead

select
user_id,
user_dob, 
user_email_id,
date_format(user_dob,'EEEE') as user_day_of_birth
from users
WHERE date_format(user_dob,'MM')=="05"
order by date_format(user_dob,'dd')



%sql
--EXERCISE 3
-- again, better to use year,month functions instead of date_format
select user_id, 
concat_ws(' ',upper(user_first_name),upper(user_last_name)) as user_name, 
user_email_id, 
created_ts, 
date_format(created_ts,'yyyy') as created_year from users
where date_format(created_ts,'yyyy') =='2019'
order by 2 asc



%sql
--EXERCISE 4
select
CASE when user_gender = 'M' then 'Male'
when user_gender = 'F' then 'Female'
else 'Not Specified' end as gender,
count(*) as user_count
from users
group by 1


%sql
--EXERCISE 5
select 
user_id,
user_unique_id, 
case when len(replace(user_unique_id,'-','')) < 9 then 'Invalid Unique ID'
else nvl(substr(replace(user_unique_id,'-',''),-4),'Not Specified') end as user_unique_id_last4
from users
order by 1 asc


%sql
--EXERCISE 6
select 
int(replace(split(user_phone_no,' ')[0],'+')) as country_code,
count(*) as user_count
from 
users
where user_phone_no is not null
group by 1
order by 1 asc
