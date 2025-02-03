-- The inside query returns the maximum budget value on the Film table
-- Since Film table only contains IDs called Director and Genre, all these tables are inner joined in order to be able to access the Director_Name and GenreType attributes
-- Then all rows of this new bigger table is checked if their budget equals the maximum budget returned by the inside query, and a table of the ones qualify is returned
-- Returned table contains only Director_Name and GenreType attributes 

SELECT Director.Director_Name, Genre.Type
FROM Film
INNER JOIN Director ON Film.Director = Director.Director_ID
INNER JOIN Genre ON Film.Genre = Genre.Genre_ID
WHERE Budget = (SELECT MAX(Budget) FROM Film);
