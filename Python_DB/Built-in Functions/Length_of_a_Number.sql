SELECT
    population,
    length(cast(population AS TEXT))
FROM
    countries