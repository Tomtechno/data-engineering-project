{{ config(
        materialized = "view",  
        cluster_by = "state"
    )
}}

select
    cast(state as string) as state,
    cast(ID as string) as accident_id,
    cast(severity as integer) as severity_id,
    cast(start_time as date) as start_time,
    cast(end_time as date) as end_time,
    cast(description as string) as description,
    cast(weather_condition as string) as weather_condition
    avg(severity_id as float) as severity_average
from {{ source("staging", "us_accidents") }}
group by state