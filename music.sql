DROP TABLE IF EXISTS users;
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
title VARCHAR,
description VARCHAR,
link VARCHAR,
UNIQUE(link),
);

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

DROP TABLE IF EXISTS playlists;
CREATE TABLE playlists(
	id INTEGER  primary key,
	title VARCHAR,
	creator VARCHAR,
	description VARCHAR,
	UNIQUE(title, creator)

);

DROP TABLE IF EXISTS playlist_tracks;
CREATE TABLE playlist_tracks(
	playlist_id Integer,
	-- FOREIGN KEY (playlist_id)
	-- 	REFERENCES playlists (id),
	track_url VARCHAR,
	-- FOREIGN KEY (track_url)
	-- 	REFERENCES tracks (link),
	PRIMARY KEY(playlist_id, track_url)


);
Insert into tracks(title, artist, length, link, artwork)
VALUES
	("Yesterday", "Beetles","2:00", "C://music//yesterday.mp3", "https://beetlesArtwork"),
	("NoWhere man", "Beetles","3:00","C://music//nowhere man.mp3", "https://AlbumArt"),
	("Spirit of the Radio","Rush","3:45","C://music//Sirit.mp3", "https://AlbumArt");


INSERT INTO playlists(title, creator, description)
VALUES
	("My Playlist", "me", "Cool Songs");

INSERT INTO playlist_tracks(playlist_id, track_url )
VALUES
	(1, "C://music//yesterday.mp3" ),
	(1, "C://music//nowhere man.mp3"),
	(1, "C://music//Sirit.mp3");