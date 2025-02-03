-- The inside query 1 returns the Director_ID of "Martin Scorsese"
-- The inside query 2 returns Film_IDs of all films in the Awards table
-- Each row of Film table is checked, and the rows that meet the requirements(Director =/= Director_ID of "Martin Scorsese" and Film_ID is not among the ones returned from the query) are returned in a table
-- The returned table contains only the Title column

SELECT Film.Title
FROM Film
WHERE Director NOT IN (SELECT Director_ID FROM Director WHERE Director_Name = 'Martin Scorsese')
AND Film_ID NOT IN (SELECT Awarded_Film FROM Award);