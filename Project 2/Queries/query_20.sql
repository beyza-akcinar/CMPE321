-- Firstly, the tables are joined, this is a left join because wee need all the director rows
-- The new table is grouped by Director_ID
-- For each group, if the count of Award_IDs is more than 0 "TRUE", else "FALSE" is returned under new column called "Awarded"

SELECT Director.Director_ID,
    CASE WHEN COUNT(Award.Award_ID) > 0 THEN 'TRUE' ELSE 'FALSE' END AS Awarded
FROM Director
LEFT JOIN Film ON Director.Director_ID = Film.Director
LEFT JOIN Award ON Film.Film_ID = Award.Awarded_Film
GROUP BY Director.Director_ID;