SELECT
    c.country
    ,c.year
    ,MAX(e.horse_power) AS max_horse_power
FROM public.cars c
JOIN public.engines e
    ON c.engine_name = e.name
WHERE c.country != 'USA'
GROUP BY
    c.country
    ,c.year
HAVING MAX(e.horse_power) > 200
ORDER BY max_horse_power DESC