# Data-Modeling-with-Postgres

Project: Data Modeling with Postgres

We are creating a Postgres database for a start up company named Sparkify. We have named the database as sparkifydb with tables to store information about song users and what they are listening to. It is designed with queries to optimize the song play analysis.

This project mainly work 5 tables for extraction, transformation and loading. The tables with their schema are as follows:

**Fact Table**
1. songplays - with the fields and datatypes:
songplay_id serial PRIMARY KEY, start_time bigint, user_id int, level varchar, song_id varchar, artist_id varchar, session_id varchar, location varchar, user_agent varchar

**Dimension Tables**

2. users - with the fields and datatypes:
user_id int, first_name varchar, last_name varchar, gender varchar, level varchar

3. songs - with the fields and datatypes:
song_id, title, artist_id, year, duration

4. artists - with the fields and datatypes:
artist_id, name, location, latitude, longitude

5. time - with the fields and datatypes:
start_time, hour, day, week, month, year, weekday

In order to create and run these tables we run **sql_queries.py** and **create_tables.py** in the terminal.

**File_1:-** **sql_queries.py**: contains all the sql queries to create,drop tables, insert the data into tables and fetch the required data from the tables.

**File_2:-** **create_tables.py**: is reponsible to create the schema structure into the PostgreSQL database before each time when ETL script is run.

Apart from these files we have following few files:

**File_3:-** **etl.ipynb**:is a python notebook which is written to develop the read and process files from song_data and log_data and load them to the tables. It basically contains instructions on ETL process for each of the tables.

**File_4:-** **etl.py**:is a file responsible for the main ETL process.

**File_5:-** **test.ipynb**: is a notebook used to display the results if our ETL process was being successful (or not).

