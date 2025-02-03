-- This query returns the sum of all budget values on the Film table
-- The column is renamed ad Total_Price

SELECT SUM(Budget) AS Total_Price FROM Film;