-- Firstly, the Film table is inner joined with Genre in order to able to access the Genre.Type attribute
-- The new table is grouped by Genre.Type, and the count of rows is returned for each group as Film_Count
-- The returned table contains Type and Film_Count as columns
-- The rows of the returned table are sorted by Film_Count in the descending order

SELECT Genre.Type, COUNT(*) AS Film_Count
FROM Film
INNER JOIN Genre ON Film.Genre = Genre.Genre_ID
GROUP BY Genre.Type
ORDER BY Film_Count DESC;