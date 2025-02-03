-- Firstly, the tables are joined in order to be able to access the Director_Name field
-- Then the new table is grouped by Director_Name, and the count of rows is returned for each group(the count of directed films) 
-- After these the table is ordered by FilmCount in descending order, meaning that the first row is our answer
-- So we limit the return value to one row to be able to get it

SELECT Director.Director_Name, COUNT(*) AS Film_Count
FROM Director 
JOIN Film ON Director.Director_ID = Film.Director
GROUP BY Director.Director_Name
ORDER BY Film_Count DESC
LIMIT 1;