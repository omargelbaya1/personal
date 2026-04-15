with stg as (

    select * from {{ ref('stg_weather') }}

),

summary as (

    select
        city,
        round(avg(temp_max_c)::numeric, 2)          as avg_temp_max_c,
        round(avg(temp_min_c)::numeric, 2)          as avg_temp_min_c,
        round(sum(precipitation_mm)::numeric, 2)    as total_precipitation_mm,
        count(case when precipitation_mm > 1 then 1 end) as rainy_days,
        max(date) filter (
            where temp_max_c = max(temp_max_c) over (partition by city)
        )                                            as hottest_day
    from stg
    group by city

)

select * from summary