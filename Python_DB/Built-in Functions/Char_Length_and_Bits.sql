SELECT
    concat(m.mountain_range, ' ', p.peak_name) AS "Mountain Information",
    char_length(concat(m.mountain_range, ' ', p.peak_name)) AS "Characters Length",
    bit_length(concat(m.mountain_range, ' ', p.peak_name)) AS "Bits of a String"
FROM
    mountains AS m,
    peaks AS p
WHERE
    m.id = p.mountain_id