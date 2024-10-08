# Write your MySQL query statement below
SELECT
    country_name,
    CASE
        WHEN AVG(weather_state) <= 15 THEN 'Cold'
        WHEN AVG(weather_state) >= 25 THEN 'Hot'
    ELSE 'Warm' END AS weather_type
FROM Countries
JOIN Weather ON Countries.country_id = Weather.country_id
AND day LIKE '2019-11%'
GROUP BY country_name