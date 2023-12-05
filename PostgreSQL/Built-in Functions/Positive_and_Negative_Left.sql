SELECT
    peak_name,
    left(peak_name, 4) AS "Positive Left",
    left(peak_name, -4) AS "Negative Left"
FROM
    peaks