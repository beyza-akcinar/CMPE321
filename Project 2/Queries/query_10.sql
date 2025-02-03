-- The inside query returns the Genre_ID for the "Comedy" genre
-- In order to able to access the Favorite_Genre attribute of Director, Film and Director tables are inner joined
-- Each row of the new table is checked, and the ones meeting the requirements (Favourite_Genre = Genre_ID of "Comedy" genre and 2000 < Release_Year < 2010) are returned in a table
-- The returned table contains Title and Release_Year columns

SELECT Film.Title, Film.Release_Year
FROM Film
INNER JOIN Director ON Film.Director = Director.Director_ID
WHERE Director.Favorite_Genre = (SELECT Genre_ID FROM Genre WHERE Type = 'Comedy')
AND Release_Year BETWEEN '2000-01-01' AND '2010-12-31';