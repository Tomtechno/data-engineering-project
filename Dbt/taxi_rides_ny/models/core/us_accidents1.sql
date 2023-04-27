{{ config(
        materialized = "table",
        cluster_by = "severity"
    )
}}

select
    cast(severity as integer) as severity_id,
    cast(ID as string) as accident_id,
    cast(start_time as date) as start_time,
    cast(end_time as date) as end_time,
    cast(description as string) as description,
    cast(state as string) as state,
    cast(weather_condition as string) as weather_condition

from {{ source("staging", "us_accidents") }}
group by severity