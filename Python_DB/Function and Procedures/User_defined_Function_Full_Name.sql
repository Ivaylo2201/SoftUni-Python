CREATE FUNCTION fn_full_name(
    first_name VARCHAR,
    last_name VARCHAR
) RETURNS VARCHAR AS
$$
    BEGIN
        IF first_name IS NULL AND last_name IS NULL THEN
            RETURN NULL;
        ELSEIF first_name IS NOT NULL AND last_name IS NULL THEN
            RETURN INITCAP(first_name);
        ELSEIF first_name IS NULL AND last_name IS NOT NULL THEN
            RETURN INITCAP(last_name);
        ELSE
            RETURN CONCAT(INITCAP(first_name), ' ', INITCAP(last_name));
        END IF;
    END;
$$
LANGUAGE plpgsql;