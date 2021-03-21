# DROP TABLES


user_table_drop = "DROP TABLE IF EXISTS users "
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"
song_table_drop = "DROP TABLE IF EXISTS songs"
songplay_table_drop = "DROP TABLE IF EXISTS songplays"

# CREATE TABLES

user_table_create = (""" CREATE TABLE IF NOT EXISTS users( user_id int, first_name varchar, last_name varchar, gender varchar, level varchar);
""")

artist_table_create = ("""CREATE TABLE IF NOT EXISTS artists(artist_id varchar, name varchar, location varchar, latitude float, longitude float);
""")


time_table_create = ("""CREATE TABLE IF NOT EXISTS time(start_time bigint, hour int, day int, week int, month int, year int, weekday int);
""")

song_table_create = ("""CREATE TABLE IF NOT EXISTS songs(song_id varchar, title varchar, artist_id varchar, year int, duration numeric);
""")

songplay_table_create = (""" CREATE TABLE IF NOT EXISTS songplays(songplay_id serial PRIMARY KEY, start_time bigint, user_id int, level varchar, song_id varchar, artist_id varchar, session_id varchar, location varchar, user_agent varchar);
""")

# INSERT RECORDS

user_table_insert = (""" INSERT INTO users(user_id, first_name, last_name, gender, level) VALUES (%s, %s, %s, %s, %s);
""")

artist_table_insert = ("""INSERT INTO artists(artist_id, name, location, latitude, longitude) VALUES (%s, %s, %s, %s, %s);
""")


time_table_insert = ("""INSERT INTO time(start_time, hour,day, week, month, year, weekday) VALUES (%s, %s, %s, %s, %s, %s, %s);
""")

song_table_insert = ("""INSERT INTO songs(song_id, title, artist_id, year, duration) VALUES (%s, %s, %s, %s, %s);
""")

songplay_table_insert = (""" INSERT INTO songplays(start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
""")

# FIND SONGS

song_select = (""" Select s.song_id, a.artist_id from songs as s join artists as a on a.artist_id=s.artist_id where s.title=(%s) and a.name=(%s) and s.duration=(%s);
""")

# QUERY LISTS

create_table_queries = [user_table_create, artist_table_create, time_table_create,song_table_create,songplay_table_create]
drop_table_queries = [ user_table_drop,  artist_table_drop, time_table_drop,song_table_drop,songplay_table_drop]
