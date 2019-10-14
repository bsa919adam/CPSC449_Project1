DROP TABLE IF EXISTS tracks;
CREATE TABLE tracks(
	title VARCHAR,
	artist VARCHAR,
	length VARCHAR,
	link VARCHAR primary key,
	artwork VARCHAR,
	UNIQUE(link),
	UNIQUE(title, artist, length)	
);

DROP TABLE IF EXISTS playlist;
CREATE TABLE playlist(
	title VARCHAR,
	link VARCHAR primary key,
	username VARCHAR,
	description VARCHAR,
	UNIQUE(link),
	UNIQUE(username),
);

DROP TABLE IF EXISTS user;
  CREATE TABLE user(
	username VARCHAR,
	password VARCHAR,
	displayname VARCHAR,
	email VARCHAR;
	homepage VARCHAR,
	UNIQUE(username,password,displayname,email,homepage),

);

DROP TABLE IF EXISTS description;
CREATE TABLE description(
song VARCHAR,
songdesc VARCHAR,
link VARCHAR,
UNIQUE(link),
)
Insert into tracks(title, artist, length, link, artwork)
VALUES("Yesterday", "Beetles","2:00", "C://music//yesterday.mp3", "https://beetlesArtwork")