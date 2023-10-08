SELECT
    last_name,
    count(notes) AS "Notes with Dumbledore"
FROM
    wizard_deposits
WHERE
    notes ILIKE '%Dumbledore%'
GROUP BY
    last_name