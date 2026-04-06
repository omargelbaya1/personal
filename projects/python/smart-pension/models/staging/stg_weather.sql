with source as (

    select * from {{ source('public', 'raw_weather') }}

)

select * from source