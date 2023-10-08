SELECT
    peak_name,
    right(peak_name, 4) AS "Positive Right",
    right(peak_name, -4) AS "Negative Right"
FROM
    peaks