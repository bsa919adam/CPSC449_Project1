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

INSERT INTO users(username,password,displayname,email,homepage)
VALUES
    ("Edward Cena","TOtoR0","Edna","ecena@yahoo.com","www.nowheretobefound.com")
    ("Tony Montana","ToTan4","BigTony","BigTony@hotmail.com","www.idontexist.com")
    ("Armand DeLaRosa","Arosa@1","ArmLaRosa","ArmLaRosa@gmail.com","www.whereismycheese.com")
INSERT INTO descriptions(title,description,link)
VALUES
    ("my lost dog","an owner for the love of dogs has lost his pet resently","www.mydog.com/lostdog")
    ("in the darkest day","the day doesnt seem bright for a lost soul that feels empty","www.emptyspace.com/darkness")
    ("find me partying in heaven", "a person who likes to party and writes about how he will still party in heaven if he goes to heaven","www.heavensdoor.com/party")