with source as (

    select * from {{ source('public', 'raw_weather') }}

),

deduplicated as (

    select *,
        row_number() over (
            partition by city, date
            order by ingested_at desc
        ) as row_num
    from source
    where date is not null

),

staged as (

    select
        city::text                 as city,
        date::date                 as date,
        temp_max_c::float          as temp_max_c,
        temp_min_c::float          as temp_min_c,
        precipitation_mm::float    as precipitation_mm,
        ingested_at::timestamp     as ingested_at
    from deduplicated
    where row_num = 1

)

select * from staged