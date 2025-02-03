-- Since primary key values are unique and not null, they are not shown explicitly
-- Since the default for foreign keys is no action, they are also not shown explicitly

-- Password and name should not be null considering the real life situations
CREATE TABLE audience (
	username VARCHAR(50),
	password VARCHAR(50) NOT NULL,
	name VARCHAR(50) NOT NULL,
	surname VARCHAR(50),
	PRIMARY KEY(username)
);

CREATE TABLE database_manager (
	username VARCHAR(50),
	password VARCHAR(50) NOT NULL,
	PRIMARY KEY(username)
);

CREATE TABLE rating_platform (
	platform_id INTEGER NOT NULL,
	platform_name VARCHAR(50),
	PRIMARY KEY(platform_id)
);

CREATE TABLE theatre (
	theatre_id INTEGER NOT NULL,
	theatre_name VARCHAR(50),
	theatre_capacity INTEGER,
	district VARCHAR(50),
	PRIMARY KEY(theatre_id)
);

CREATE TABLE movie (
	movie_id INTEGER NOT NULL,
	movie_name VARCHAR(50),
	duration INTEGER,
	average_rating FLOAT,
	PRIMARY KEY(movie_id)
);

CREATE TABLE genre (
	genre_id INTEGER NOT NULL,
	genre_name VARCHAR(50),
	PRIMARY KEY(genre_id)
);

-- Every director should have only one nation -> nation cannot be null
CREATE TABLE director (
	username VARCHAR(50) NOT NULL,
	password VARCHAR(50) NOT NULL,
	name VARCHAR(50) NOT NULL,
	surname VARCHAR(50),
	nation VARCHAR(50) NOT NULL,
	platform_id INTEGER,
	PRIMARY KEY(username)
);

-- If a director is deleted, his/her movies are also deleted
-- If a movie is deleted, the directed_by entry fro that movie is deleted
CREATE TABLE directed_by (
	username VARCHAR(50) NOT NULL,
	movie_id INTEGER,
	PRIMARY KEY(username, movie_id),
	FOREIGN KEY(username) REFERENCES director
	ON DELETE CASCADE,
	FOREIGN KEY(movie_id) REFERENCES movie
	ON DELETE CASCADE
);

-- If an audience is deleted, his/her subscription is also deleted
-- If a rating platform is deleted, its subscribers are also deleted
CREATE TABLE subscription (
	username VARCHAR(50) NOT NULL,
	platform_id INTEGER,
	PRIMARY KEY(username, platform_id),
	FOREIGN KEY(username) REFERENCES audience
	ON DELETE CASCADE,
	FOREIGN KEY(platform_id) REFERENCES rating_platform
	ON DELETE CASCADE
);

CREATE TABLE predecessor (
	movie_id1 INTEGER NOT NULL,
	movie_id2 INTEGER,
	PRIMARY KEY(movie_id1, movie_id2),
	FOREIGN KEY(movie_id1) REFERENCES movie,
	FOREIGN KEY(movie_id2) REFERENCES movie
);

-- If a movie is deleted its genres are also deleted
-- If a genre is deleted, its occurences in this table are also deleted
CREATE TABLE genre_list (
	movie_id INTEGER NOT NULL,
	genre_id INTEGER,
	PRIMARY KEY(movie_id, genre_id),
	FOREIGN KEY(movie_id) REFERENCES movie
	ON DELETE CASCADE,
	FOREIGN KEY(genre_id) REFERENCES genre
	ON DELETE CASCADE
);

-- If a movie is deleted, its ratings are also deleted
-- If an audience is deleted, his/her rating is still kept
CREATE TABLE rating (
	username VARCHAR(50) NOT NULL,
	movie_id INTEGER,
	rating FLOAT,
	PRIMARY KEY(username),
	FOREIGN KEY(username) REFERENCES audience,
	FOREIGN KEY(movie_id) REFERENCES movie
	ON DELETE CASCADE
);

CREATE TABLE session (
	session_id INTEGER UNIQUE,
	movie_id INTEGER,
	theatre_id INTEGER,
	date DATE,
	time_slot INTEGER,
	PRIMARY KEY(theatre_id, date, time_slot),
	FOREIGN KEY(movie_id) REFERENCES movie,
	FOREIGN KEY(theatre_id) REFERENCES theatre
);

-- An audience can buy a ticket for his/her own name only
CREATE TABLE ticket (
	username VARCHAR(50),
	session_id INTEGER,
	PRIMARY KEY(username, session_id),
	FOREIGN KEY(username) REFERENCES audience,
	FOREIGN KEY(session_id) REFERENCES session(session_id)
);
