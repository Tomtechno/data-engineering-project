{{ config(materialized = "view") }}

select * from {{ ref('us_accidents') }}
limit 50
