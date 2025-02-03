-- This statement adds a new row to the Awards table
-- Since the table creates the Award_ID by autoincrement, providing only the other two values is enough
-- However, this query works fine because there exists a film with the Title "After Sun"
-- If there is no movie with the given Title, this query still adds the row with Awarded_Film as NULL

INSERT INTO Award(Award_Title, Awarded_Film)
VALUES ("BU-Best Actor", (SELECT Film_ID FROM Film WHERE Title = "After Sun"));