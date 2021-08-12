import sqlalchemy
import psycopg2
from pprint import pprint

db = 'postgresql://neto20210730:neto20210730@localhost:5432/neto0730'
engine = sqlalchemy.create_engine(db)
connection = engine.connect()

print('название и год выхода альбомов, вышедших в 2018 году:')
res = connection.execute("""SELECT title_album, year_release 
FROM album
WHERE year_release = 2018; """).fetchall()

pprint(res)
print('________________')

print('название и продолжительность самого длительного трека;')
res = connection.execute("""SELECT title_track, duration
FROM track
WHERE duration = (
         SELECT MAX(duration) 
         FROM track); """).fetchall()

pprint(res)
print('________________')

print('название треков, продолжительность которых не менее 3,5 минуты;')
res = connection.execute("""SELECT title_track 
FROM track
WHERE duration > 3.5; """).fetchall()

pprint(res)
print('________________')

print('названия сборников, вышедших в период с 2018 по 2020 год включительно;')
res = connection.execute("""SELECT name 
FROM collection
WHERE yaer_release BETWEEN 2018 and 2020; """).fetchall()

pprint(res)
print('________________')

print('исполнители, чье имя состоит из 1 слова;')
res = connection.execute("""SELECT name
FROM artist
WHERE name NOT LIKE '%% %%'; """).fetchall()

pprint(res)
print('________________')

print('название треков, которые содержат слово "мой"/"my".')
res = connection.execute("""SELECT title_track
FROM track
WHERE title_track ILIKE '%%мой%%' OR title_track ILIKE '%%my%%'; """).fetchall()

pprint(res)
print('________________')

print('_______________HW5_____________')

pprint('количество исполнителей в каждом жанре;')
res = connection.execute("""SELECT g.title_genre, COUNT(a.artist_id) count 
FROM genre g
JOIN artist_genre ag ON g.genre_id = ag.genre_genre_id
JOIN artist a ON ag.artist_artist_id = a.artist_id
GROUP BY  g.name
ORDER BY  count DESC; """).fetchall()

pprint(res)
print('________________')

pprint('количество треков, вошедших в альбомы 2019-2020 годов;')
res = connection.execute("""SELECT COUNT(t.track_id) count FROM album a
JOIN track t ON t.album_id = a.album_id
WHERE a.year_release >= 2019
AND a.year_release <= 2020; """).fetchall()

pprint(res)
print('________________')

pprint('средняя продолжительность треков по каждому альбому;')
res = connection.execute("""SELECT a.title_album, AVG(t.duration) avg 
FROM album a
JOIN track t ON t.album_id = a.album_id
GROUP by a.title_album
ORDER BY avg DESC; """).fetchall()

pprint(res)
print('________________')

pprint('все исполнители, которые не выпустили альбомы в 2020 году;')
res = connection.execute("""SELECT a.name FROM artist a
JOIN artist_album aa ON a.artist_id = aa.artist_artist_id
JOIN album al ON aa.album_album_id = al.album_id
WHERE NOT EXISTS(SELECT * FROM artist WHERE al.year_release = 2020)
GROUP BY a.name
ORDER BY a.name; """).fetchall()

pprint(res)
print('________________')

pprint('названия сборников, в которых присутствует конкретный исполнитель (выберите сами);')
res = connection.execute("""SELECT c.name FROM collection c
JOIN track_collection tc ON c.collection_id = tc.collection_collection_id
JOIN track t ON tc.track_track_id = t.track_id
JOIN album a ON t.album_album_id = a.album_id
JOIN artist_album aa ON al.album_id = aa.album_album_id
JOIN artist a on a.artist_id = aa.artist_artist_id
WHERE a.name = 'Ария'
GROUP BY c.name
ORDER BY c.name; """).fetchall()

pprint(res)
print('________________')
pprint('название альбомов, в которых присутствуют исполнители более 1 жанра;')
res = connection.execute("""SELECT a.name 
FROM album a
JOIN artist_album aa ON al.album_id = aa.album_album_id
JOIN artist a ON aa.artist_artist_id = a.artist_id
JOIN artist_genre ag ON ag.artist_artist_id = a.artist_id
JOIN genre g ON ag.genre_genre_id = g.genre_id
GROUP BY a.name
HAVING COUNT(g.genre_id) > 1; """).fetchall()

pprint(res)
print('________________')

pprint('наименование треков, которые не входят в сборники;')
res = connection.execute("""
SELECT t.name 
FROM track t
LEFT JOIN track_collection tc ON tc.track_track_id = t.track_id 
WHERE tc.collection_collection_id IS NULL
GROUP BY t.name; """).fetchall()

pprint(res)
print('________________')

pprint('исполнителя(-ей), написавшего самый короткий по продолжительности трек (теоретически таких треков может быть '
       'несколько);')
res = connection.execute("""
SELECT a.name FROM artist a
JOIN artist_album aa ON a.artist_id = aa.artist_artist_id
JOIN album al ON aa.album_album_id = a.album_id
JOIN track t ON t.album_id = a.album_id
WHERE t.duration = (SELECT MIN(duration) from track)
GROUP BY a.name
ORDER BY a.name """).fetchall()

pprint(res)
print('________________')

pprint('название альбомов, содержащих наименьшее количество треков.')
res = connection.execute("""
SELECT a.name 
FROM track t 
JOIN album a ON a.album_id = t.album_id
GROUP BY a.title_album 
HAVING COUNT(t.track_id) = (SELECT MIN(count) FROM 
                                (SELECT album.title_album, COUNT(track.track_id) count FROM track
                                JOIN album ON album.album_id = track.album_id
                                GROUP BY album.title_album) as c; """).fetchall()

pprint(res)
print('________________')
