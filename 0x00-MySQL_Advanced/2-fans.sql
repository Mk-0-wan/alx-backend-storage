-- Selecting bands based on thier number of fnas
-- Group by will help you in grouping all the common row values in a particular column together
SELECT origin, SUM(fans) AS nb_fans FROM metal_bands GROUP BY origin ORDER BY nb_fans DESC;
