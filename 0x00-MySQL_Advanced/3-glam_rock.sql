-- Selecting all the bands with Glam rock as thier style
SELECT band_name, IFNULL(split, 2022) - formed AS lifespan FROM metal_bands WHERE style LIKE '%Glam rock%';
