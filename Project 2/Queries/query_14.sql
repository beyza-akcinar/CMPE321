-- Firstly, Film and Director tables are joined in order to able to access Director_Name field
-- The inside query returns all the Film_IDs appearing in the Award table
-- All rows of the Film table are checked and the ones meeting the requirements(Release_Year > 2015 and Film_ID is not among the ones returned from the inside query) are returned in a new table
-- The returned table has Title, Director_Name, and Release_Year fields

SELECT Title, Director_Name, Release_Year
FROM Film 
JOIN Director ON Film.Director = Director.Director_ID
WHERE Release_Year > '2015' 
  AND Film_ID NOT IN (SELECT Awarded_Film FROM Award);