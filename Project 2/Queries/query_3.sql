-- The inside query returns the minimum budget value in the Film table
-- The outside query checks each row of Film table, and returns the row if the budget value of the row equals the minimum value found by inside query

SELECT *
FROM Film
WHERE Budget = (SELECT MIN(Budget) FROM Film);

