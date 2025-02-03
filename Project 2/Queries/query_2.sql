-- Firstly, Film and Director tables are inner joined in order to access the Director_Name field
-- Then, each row of this new table is checked, and returned itf they meet the requirements(Release_Year < 2020)
-- Lastly, the rows are ordered in terms of their Release_Year in ascending order

SELECT Film.Title, Director.Director_Name, Film.Release_Year
FROM Film
INNER JOIN Director ON Film.Director = Director.Director_ID
WHERE Film.Release_Year < 2020
ORDER BY Film.Release_Year ASC;
