-- Firstly, the tables are joined in order to be able to access the Director_Name field
-- Then the new table is grouped by Director_Name, and the average of the Budget values is returned for each group
-- The results are returned in a table sorted by AverageBudget in descending order

SELECT Director.Director_Name, AVG(Film.Budget) AS AvgBudget
FROM Director JOIN Film ON Director.Director_ID = Film.Director
GROUP BY Director.Director_Name
ORDER BY AvgBudget DESC;