-- All the tables are joined in order to access required fields. We left joined only for Award table, since we want to count films without awards as well
-- The new table is grouped by both Genre_ID and Director_ID since we want to count a director's films based on one specific genre
-- Temp   : |Genre|Director_Name|Award_Count|
-- Temp table contains the total number of awards a director's films of a specific genre have
-- Temp2  : |Genre|Award_Count|
-- Temp2 table is the same just without the Director_Name row
-- Temp2 table is grouped by Genre again to find the maximum the Award_Count value based on genre
-- After finding the maximum Award_Count value for each genre, (genre,value) based comparison with Temp table is performed

-- This complicated process was required because when more than one director have the maximum number of awards, just by doing GROUP BY returning all of them is not possible 

SELECT Temp.Genre, Temp.Director_Name, Temp.Award_Count
FROM
    (SELECT Genre.Type AS Genre, Director_Name, COUNT(Award_ID) AS Award_Count
    FROM Film
    JOIN Genre ON Film.Genre = Genre.Genre_ID
    JOIN Director ON Director.Director_ID = Film.Director
    LEFT JOIN Award ON Award.Awarded_Film = Film.Film_ID
    GROUP BY Genre_ID, Director_ID) AS Temp
WHERE (Temp.Genre, Temp.Award_Count) IN 
    (SELECT Temp2.Genre, MAX(Temp2.Award_Count)
    FROM (SELECT Genre.Type AS Genre, COUNT(Award_ID) AS Award_Count
    FROM Film
    JOIN Genre ON Film.Genre = Genre.Genre_ID
    JOIN Director ON Director.Director_ID = Film.Director
    LEFT JOIN Award ON Award.Awarded_Film = Film.Film_ID
    GROUP BY Genre_ID, Director_ID) AS Temp2
    GROUP BY Genre);


