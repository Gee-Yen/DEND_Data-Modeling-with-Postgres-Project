# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplays 
( 
  songplay_id SERIAL PRIMARY KEY, 
  start_time TIMESTAMP NOT NULL REFERENCES time(start_time), 
  user_id INT NOT NULL REFERENCES users(user_id), 
  level VARCHAR, 
  song_id VARCHAR REFERENCES songs(song_id), 
  artist_id VARCHAR REFERENCES artists(artist_id), 
  session_id INT, 
  location TEXT, 
  user_agent TEXT
)
""")

user_table_create = ("""
CREATE TABLE IF NOT EXISTS users 
( 
  user_id INT PRIMARY KEY, 
  first_name VARCHAR, 
  last_name VARCHAR, 
  gender CHAR(1), 
  level VARCHAR
)
""")

song_table_create = ("""
CREATE TABLE IF NOT EXISTS songs 
( 
  song_id VARCHAR PRIMARY KEY, 
  title VARCHAR, 
  artist_id VARCHAR, 
  year INT, 
  duration FLOAT
)
""")

artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artists 
( 
  artist_id VARCHAR PRIMARY KEY, 
  name VARCHAR, 
  location VARCHAR, 
  latitude VARCHAR, 
  longitude VARCHAR
)
""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS time 
( 
  start_time TIMESTAMP PRIMARY KEY, 
  hour INT, 
  day INT, 
  week INT, 
  month INT, 
  year INT, 
  weekday INT
)
""")

# INSERT RECORDS

songplay_table_insert = ("""
INSERT INTO songplays(start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) 
values(%s, %s, %s, %s, %s, %s, %s, %s)
""")

user_table_insert = ("""
INSERT INTO users(user_id, first_name, last_name, gender, level) 
values(%s, %s, %s, %s, %s)
ON CONFLICT(user_id) DO UPDATE SET level = excluded.level
""")

song_table_insert = ("""
INSERT INTO songs(song_id, title, artist_id, year, duration) 
values(%s, %s, %s, %s, %s)
ON CONFLICT(song_id) DO UPDATE SET title = EXCLUDED.title,
                                   artist_id = EXCLUDED.artist_id,
                                   year = EXCLUDED.year,
                                   duration = EXCLUDED.duration
""")

artist_table_insert = ("""
INSERT INTO artists(artist_id, name, location, latitude, longitude) 
values(%s, %s, %s, %s, %s)
ON CONFLICT(artist_id) DO UPDATE SET name = EXCLUDED.name
""")


time_table_insert = ("""
INSERT INTO time(start_time, hour, day, week, month, year, weekday) 
values(%s, %s, %s, %s, %s, %s, %s)
ON CONFLICT(start_time) DO NOTHING
""")

# FIND SONGS

song_select = ("""
SELECT s.song_id,
       a.artist_id
FROM   songs s INNER JOIN artists a
ON     s.artist_id = a.artist_id
WHERE  s.title     = %s
AND    a.name      = %s
AND    s.duration  = %s
""")

# QUERY LISTS
# I changed the order of creation of fact and dimension tables. I pushed the creation of fact table to last
create_table_queries = [user_table_create, song_table_create, artist_table_create, time_table_create, songplay_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]

