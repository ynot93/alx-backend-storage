-- Define the query to select bands with Glam rock as their main style
-- Calculate their lifespan
SELECT
    band_name,
    (IFNULL(split, '2022') - formed) AS lifespan
FROM
    metal_bands
WHERE
    style LIKE '%Glam rock%'
ORDER BY
    lifespan DESC;
