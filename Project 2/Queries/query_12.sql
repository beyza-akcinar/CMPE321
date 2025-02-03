-- Firstly, Film and Director tables are joined in order to access to needed fields
-- The new table is grouped by Release_year since we want to find data for each year
-- Then, for each group, Director_Name, Release_Year, the maximum budget value of the films meeting the requirement(Budget = MAX(Budget) for the group) is returned

SELECT Director_Name, Release_Year, MAX(Budget) AS Max_Budget
FROM Film
INNER JOIN Director ON Director.Director_ID = Film.Director
GROUP BY Release_Year;
	