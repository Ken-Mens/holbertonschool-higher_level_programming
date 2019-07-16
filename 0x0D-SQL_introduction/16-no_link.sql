-- lists only ones with name in second_table
SELECT score, name FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
