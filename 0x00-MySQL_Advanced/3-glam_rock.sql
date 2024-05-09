-- Define the query to select bands with Glam rock as their main style
-- Calculate their lifespan
SELECT
    name AS band_name,
    IF(split = '0000', 2022 - formed, split - formed) AS lifespan
FROM
    metal_bands
WHERE
    style = 'Glam rock'
ORDER BY
    lifespan DESC;
