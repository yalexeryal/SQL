import sqlalchemy
from pprint import pprint

artists = ['Ария', 'Филипп Киркоров', 'StaFFорд63', 'Chris Stapleton', 'Andrea Bocelli', 'Powerwolf', 'Medsound',
           'Gorgon City', 'Kid Ory', 'Ketty Lester', 'Big Noise', 'Santana', 'Lordi', 'Люся Чеботина', 'Gidayyat']
genres = ['поп', 'Рок', 'рэп', 'электронная музыка', 'шансон', 'метал', 'классика', 'rnb', 'house', 'кантри',
          'джаз', 'инструментальная', 'танцевальная музыка']
albums = [('Мания величия', 1985), ('Незнакомка', 2003), ('10 Историй', 2021), ('Traveller', 2015),
          ('Базара Нет', 2021), ('Cinema', 2016), ('Blessed & Possessed ', 2015), ('A Journey To House ', 2018),
          ('Olympia', 2021)]
tracks = [('Это Мой Рок', 5.54, 1), ('Роза чайная', 4.22, 2), ('Жестокая любовь', 3.47, 2),
          ('Вы Простите Меня', 3.19, 3),
          ('Глубоко в Сердце', 2.45, 3), ('Might As Well Get Stoned', 4.53, 4), ('Whiskey And You', 3.56, 4),
          ('Малой', 4.22, 5), ('Рубаха Парень', 3.46, 5), ('From Breakfast At Tiffany', 3.49, 6),
          ('Moon River', 4.21, 6),
          ('Let There Be Night', 7.19, 7), ('Dead Until Dark', 3.49, 7), ('Distant Frequencies', 4.56, 8),
          ('When We Fly', 6.20, 8), ('Lost Feelings', 4.17, 9), ('Sweet Temptation', 3.40, 9), ('Лунная Соната', 6.35),
          ('Someday Sweetheart', 8.22), (' Love Letters', 2.37), ('Keep On Pushing', 7.34), ('Ballin', 6.10),
          ('Hard Rock Halllujah', 4.08), ('Trend', 2.21), ('Акунаматата', 2.01)]
collection = [('Шедевры Классики', 2013), ('The Complete Kid Ory Verve Sessions', 1999),
              ('Anthology: First Recordings', 2020), ('Best Of Underground Dance', 1994), ('Folsom Street', 1971),
              ('Хиты всех времён', 2021), ('Весёлые песни для гулянки', 2021), ('Молодёжные', 2021)]
artist_album = [(1, 1), (2, 2), (3, 3), (4, 4), (3, 5), (5, 6), (6, 7), (7, 8), (8, 9)]
artist_genre = [(1, 2), (2, 1), (3, 3), (4, 10), (3, 5), (5, 7), (6, 6), (7, 9), (8, 13), (9, 9), (10, 1), (11, 9),
                (12, 1), (13, 6), (14, 1), (15, 3)]
track_collection = [(18, 1), (19, 2), (20, 3), (21, 4), (22, 5), (23, 6), (24, 7), (25, 8)]

db = 'postgresql://neto20210730:neto20210730@localhost:5432/neto0730'
engine = sqlalchemy.create_engine(db)
connection = engine.connect()

"""Заполнение таблицы genre"""
connection.execute("""INSERT INTO genre (title_genre) VALUES ('поп', 'Рок', 'рэп', 'электронная музыка', 'шансон', 'метал', 'классика', 'rnb', 'house', 'кантри',
          'джаз', 'инструментальная', 'танцевальная музыка')""")


# connection.execute("""INSERT INTO artist_genre(artist_artist_id, genre_genre_id) VALUES(8, 1)""")
# connection.execute("""DELETE FROM collection WHERE collection_id = 3;""")


res = connection.execute("""SELECT genre_id, title_genre 
FROM genre; """).fetchall()

pprint(res)