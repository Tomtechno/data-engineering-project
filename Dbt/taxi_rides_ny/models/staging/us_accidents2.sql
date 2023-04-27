{{ config(materialized = "view") }}

select * from {{ ref('us_accidents_external_table') }}
limit 50
