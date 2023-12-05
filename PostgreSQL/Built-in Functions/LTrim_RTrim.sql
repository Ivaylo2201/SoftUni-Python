SELECT
    ltrim(peak_name, 'M') AS "Left Trim",
    rtrim(peak_name, 'm') AS "Right Trim"
FROM
    peaks