
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
  
Insert into tracks(title, artist, length, link, artwork)
VALUES("Yesterday", "Beetles","2:00", "C://music//yesterday.mp3", "https://beetlesArtwork")