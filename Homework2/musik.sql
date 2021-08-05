CREATE TABLE IF NOT EXISTS artist (
  artist_id SERIAL PRIMARY KEY, 
  name VARCHAR(30) NOT NULL,
  genre_genre_id INTEGER REFERENCES genre(genre_id) NOT NULL
);
CREATE TABLE IF NOT EXISTS genre (
  genere_id SERIAL PRIMARY KEY, 
  title_genres VARCHAR(50) NOT NULL
);
CREATE TABLE IF NOT EXISTS album (
  album_id SERIAL PRIMARY KEY, 
  title_album VARCHAR(50) NOT NULL, 
  year_release INTEGER NOT NULL, 
  artist_artist_id INTEGER REFERENCES artist(artist_id) NOT NULL
);
CREATE TABLE IF NOT EXISTS track (
  track_id SERIAL PRIMARY KEY, 
  title_track VARCHAR(50) NOT NULL, 
  duration INTEGER NOT NULL, 
  album_album_id INTEGER REFERENCES album(album_id) NOT NULL
);