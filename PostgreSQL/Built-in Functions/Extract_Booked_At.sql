SELECT
    extract(year FROM booked_at) AS "YEAR",
    extract(month FROM booked_at) AS "MONTH",
    extract(day FROM booked_at) AS "DAY",
    extract(hour FROM booked_at) AS "HOUR",
    extract(minute FROM booked_at) AS "MINUTE",
    ceil(extract(second FROM booked_at)) AS "SECOND"
FROM
    bookings