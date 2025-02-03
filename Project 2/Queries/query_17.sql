-- All the tables are joined in order to access required fields. We left joined only for Award table, since we want to count films without awards as well
-- The new table is grouped by both Genre_ID and Director_ID since we want to count a director's films based on one specific genre
-- Temp   : |Genre|Director_Name|Film_Count|
-- Temp table contains the total number of films of a specific genre a director has directed, also without any awards
-- Temp2  : |Genre|Director_Name|Film_Count|
-- Temp2 table is the same
-- Temp2 table is grouped by Genre again to find the maximum the Film_Count value based on genre
-- After finding the maximum Film_Count value for each genre, (genre,value) based comparison with Temp table is performed

-- This complicated process was required because when more than one director have the maximum number of films, just by doing GROUP BY returning all of them is not possible

SELECT Temp.Genre AS Genre_Type, Temp.Director_Name, Temp.Film_Count
FROM
    (SELECT Genre.Type AS Genre, Director_Name, COUNT(Film_ID) AS Film_Count
    FROM Film
    JOIN Genre ON Film.Genre = Genre.Genre_ID
    JOIN Director ON Director.Director_ID = Film.Director
    LEFT JOIN Award ON Award.Awarded_Film = Film.Film_ID
    GROUP BY Genre_ID, Director_ID
	HAVING COUNT(Award_ID) = 0) AS Temp
WHERE (Temp.Genre, Temp.Film_Count) IN 
    (SELECT T.Genre, MAX(T.Film_Count)
    FROM (SELECT Genre.Type AS Genre, Director_Name, COUNT(Film_ID) AS Film_Count
    FROM Film
    JOIN Genre ON Film.Genre = Genre.Genre_ID
    JOIN Director ON Director.Director_ID = Film.Director
    LEFT JOIN Award ON Award.Awarded_Film = Film.Film_ID
    GROUP BY Genre_ID, Director_ID
	HAVING COUNT(Award_ID) = 0) AS T
    GROUP BY Genre);
	

