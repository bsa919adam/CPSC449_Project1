
DROP TABLE IF EXISTS tracks;
CREATE TABLE tracks(
	title VARCHAR,
	artist VARCHAR,
	length TIME,
	link VARCHAR primary key,
	artwork VARCHAR,
	UNIQUE(link),
	UNIQUE(title, artist, length)	
);
  
