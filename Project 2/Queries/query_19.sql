-- Firstly the Film and Director tables are joined
-- All rows are checked, and the ones meeting the requirement (Favorite_Genre of Director = Film Genre) are returned in a new table
-- The returned table includes all the columns of Film and Director tables

SELECT *
FROM Film
JOIN Director ON Film.Director = Director.Director_ID
WHERE Director.Favorite_Genre = Film.Genre;