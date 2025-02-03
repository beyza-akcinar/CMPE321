-- The inner queries return the Release_Year(i) and Budget(ii) for the movie called "The Godfather", respectively
-- All rows of Film are checked one by one and the rows that meet the conditions (Release_Year = (i) and Budget > (ii)) are returned in a table
-- The returned table contains the same type of colums as Film

SELECT *
FROM Film
WHERE Release_Year = (SELECT Release_Year FROM Film WHERE Title = 'The Godfather')
AND Budget > (SELECT Budget FROM Film WHERE Title = 'The Godfather');