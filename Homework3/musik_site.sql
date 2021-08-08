CREATE TABLE IF NOT EXISTS genre (
  genre_id SERIAL PRIMARY KEY, 
  title_genre VARCHAR(50) NOT NULL
);
CREATE TABLE IF NOT EXISTS artist (
  artist_id SERIAL PRIMARY KEY, 
  name VARCHAR(30) NOT NULL
);
CREATE TABLE IF NOT EXISTS album (
  album_id SERIAL PRIMARY KEY,
  title_album VARCHAR(100) NOT NULL,
  year_release NUMERIC(4,
0) NOT NULL
);
CREATE TABLE IF NOT EXISTS track (
track_id SERIAL PRIMARY KEY,
title_track VARCHAR(50) NOT NULL,
duration NUMERIC(4.2) NOT NULL,
album_album_id INTEGER REFERENCES album(album_id)
);
CREATE TABLE IF NOT EXISTS collection (
collection_id SERIAL PRIMARY KEY,
name VARCHAR(100) NOT NULL,
yaer_release NUMERIC(4.0) NOT NULL
);
CREATE TABLE IF NOT EXISTS artist_album (
artist_album_id SERIAL PRIMARY KEY,
artist_artist_id INTEGER REFERENCES artist(artist_id) NOT NULL,
album_album_id INTEGER REFERENCES album(album_id) NOT NULL
);
CREATE TABLE IF NOT EXISTS artist_genre (
artist_genre_id SERIAL PRIMARY KEY,
artist_artist_id INTEGER REFERENCES artist(artist_id) NOT NULL,
genre_genre_id INTEGER REFERENCES genre(genre_id) NOT NULL
);
CREATE TABLE IF NOT EXISTS track_collection (
track_collection_id SERIAL PRIMARY KEY,
track_track_id INTEGER REFERENCES track(track_id),
collection_collection_id INTEGER REFERENCES collection(collection_id)
);

