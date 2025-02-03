-- Firstly, the tables are joined in order to able to access the fields Director_Name and Award_Title
-- Then, rows are grouped in terms of Film_ID since we want to find the "Films" having awards in at least 3 categories
-- For all groups, distinct Award_Title values are counted, and checked if the group has more than 2 different award types 
-- The Director_Name fields of the groups meeting the requirement are returned in a new table

SELECT DISTINCT Director.Director_Name
FROM Film
INNER JOIN Director ON Film.Director = Director.Director_ID
INNER JOIN Award ON Film.Film_ID = Award.Awarded_Film
GROUP BY Film_ID
HAVING COUNT(DISTINCT Award_Title) > 2;