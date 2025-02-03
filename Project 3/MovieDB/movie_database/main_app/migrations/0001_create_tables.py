from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        # Add any dependencies if required
    ]

    operations = [
        migrations.RunSQL(
            """
            CREATE TABLE IF NOT EXISTS audience (
	            username VARCHAR(50) NOT NULL,
	            password VARCHAR(50) NOT NULL,
	            name VARCHAR(50) NOT NULL,
	            surname VARCHAR(50),
	            PRIMARY KEY(username)
            );
            """
        ),
        migrations.RunSQL(
            """
            CREATE TABLE IF NOT EXISTS director (
	            username VARCHAR(50) NOT NULL,
	            password VARCHAR(50) NOT NULL,
	            name VARCHAR(50) NOT NULL,
	            surname VARCHAR(50),
	            nation VARCHAR(50) NOT NULL,
	            platform_id INTEGER,
	            PRIMARY KEY(username)
            );
            """
        ),
        migrations.RunSQL(
            """
            CREATE TABLE IF NOT EXISTS database_manager (
	            username VARCHAR(50) NOT NULL,
	            password VARCHAR(50) NOT NULL,
	            PRIMARY KEY(username)
            );
            """
        ),
        migrations.RunSQL(
            """
            CREATE TABLE IF NOT EXISTS rating_platform (
	            platform_id INTEGER NOT NULL,
	            platform_name VARCHAR(50) NOT NULL UNIQUE,
	            PRIMARY KEY(platform_id)
            );
            """
        ),
        migrations.RunSQL(
            """
            CREATE TABLE IF NOT EXISTS theatre (
	            theatre_id INTEGER NOT NULL,
	            theatre_name VARCHAR(50),
	            theatre_capacity INTEGER,
	            district VARCHAR(50),
	            PRIMARY KEY(theatre_id)
            );
            """
        ),
        migrations.RunSQL(
            """
            CREATE TABLE IF NOT EXISTS movie (
	            movie_id INTEGER NOT NULL,
	            movie_name VARCHAR(50),
	            duration INTEGER,
	            average_rating FLOAT,
                director_username VARCHAR(50),
	            PRIMARY KEY(movie_id)
            );
            """
        ),
        migrations.RunSQL(
            """
            CREATE TABLE IF NOT EXISTS genre (
	            genre_id INTEGER NOT NULL,
	            genre_name VARCHAR(50) NOT NULL UNIQUE,
	            PRIMARY KEY(genre_id)
            );
            """
        ),
        migrations.RunSQL(
            """
            CREATE TABLE IF NOT EXISTS subscription (
	            username VARCHAR(50) NOT NULL,
	            platform_id INTEGER,
	            PRIMARY KEY(username, platform_id),
	            FOREIGN KEY(username) REFERENCES audience(username)
	            ON DELETE CASCADE,
	            FOREIGN KEY(platform_id) REFERENCES rating_platform(platform_id)
	            ON DELETE CASCADE
            );
            """
        ),
        migrations.RunSQL(
            """
            CREATE TABLE IF NOT EXISTS predecessor (
	            movie_id1 INTEGER NOT NULL,
	            movie_id2 INTEGER,
	            PRIMARY KEY(movie_id1, movie_id2),
	            FOREIGN KEY(movie_id1) REFERENCES movie(movie_id)
                ON DELETE CASCADE,
	            FOREIGN KEY(movie_id2) REFERENCES movie(movie_id)
                ON DELETE CASCADE
            );
            """
        ),
        migrations.RunSQL(
            """
            CREATE TABLE IF NOT EXISTS genre_list (
	            movie_id INTEGER NOT NULL,
	            genre_id INTEGER,
	            PRIMARY KEY(movie_id, genre_id),
	            FOREIGN KEY(movie_id) REFERENCES movie(movie_id)
	            ON DELETE CASCADE,
	            FOREIGN KEY(genre_id) REFERENCES genre(genre_id)
	            ON DELETE CASCADE
            );
            """
        ),
        migrations.RunSQL(
            """
            CREATE TABLE IF NOT EXISTS rating (
	            username VARCHAR(50) NOT NULL,
	            movie_id INTEGER,
	            rating FLOAT,
	            PRIMARY KEY(username, movie_id),
	            FOREIGN KEY(username) REFERENCES audience(username),
	            FOREIGN KEY(movie_id) REFERENCES movie(movie_id)
	            ON DELETE CASCADE,
                CHECK(rating>=0 AND rating<=5)
            );
            """
        ),
        migrations.RunSQL(
            """
                CREATE TABLE IF NOT EXISTS sessions (
	                session_id INTEGER UNIQUE,
	                movie_id INTEGER,
	                theatre_id INTEGER,
	                date DATE,
	                starting_slot INTEGER,
                    ending_slot INTEGER,
	                PRIMARY KEY(session_id),
	                FOREIGN KEY(movie_id) REFERENCES movie(movie_id),
	                FOREIGN KEY(theatre_id) REFERENCES theatre(theatre_id),
                    CHECK (starting_slot IN (1, 2, 3, 4)),
                    CHECK (ending_slot IN (1, 2, 3, 4))
                );
            """
        ),
        migrations.RunSQL(
            """
            CREATE TABLE IF NOT EXISTS ticket (
	            username VARCHAR(50),
	            session_id INTEGER,
	            PRIMARY KEY(username, session_id),
	            FOREIGN KEY(username) REFERENCES audience(username)
                ON DELETE CASCADE,
	            FOREIGN KEY(session_id) REFERENCES sessions(session_id)
            );
            """
        ),
        migrations.RunSQL(
            """
            CREATE TRIGGER IF NOT EXISTS enforce_max_rows
            BEFORE INSERT ON database_manager
            FOR EACH ROW
            BEGIN
                DECLARE row_count INT;
                SELECT COUNT(*) INTO row_count FROM database_manager;
                IF row_count >= 4 THEN
                SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Maximum number of rows reached';
                END IF;
            END;
            """
        ),
        migrations.RunSQL(
            """
            CREATE TRIGGER IF NOT EXISTS update_average_rating AFTER INSERT ON rating
            FOR EACH ROW
            BEGIN
                UPDATE movie
                SET average_rating = (
                    SELECT AVG(rating)
                    FROM rating
                    WHERE movie_id = NEW.movie_id
                )
                WHERE movie_id = NEW.movie_id;
            END;
            """
        ),



        




        

    ]