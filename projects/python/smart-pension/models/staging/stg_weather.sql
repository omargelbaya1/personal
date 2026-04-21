with source as (

    select * from {{ source('public', 'raw_weather') }}

),

latest_dayas (
    row_number() on city
)

stg as (

    select distinct on (city,date)
        city::text                 as city,
        date::date                 as date,
        temp_max_c::float          as temp_max_c,
        temp_min_c::float          as temp_min_c,
        precipitation_mm::float    as precipitation_mm,
        ingested_at::timestamp     as ingested_at
    from source
    where date is not null

)

select * from stg