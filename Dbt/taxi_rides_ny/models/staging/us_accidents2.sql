{{ config(materialized = "view") }}

select * from {{ source("staging", "us_accidents") }}
limit 50