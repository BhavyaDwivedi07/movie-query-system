import sqlite3
import csv
import requests
from io import StringIO

url = "https://raw.githubusercontent.com/sundeepblue/movie_rating_prediction/master/movie_metadata.csv"
response = requests.get(url)
data = response.text

csv_file = StringIO(data)
reader = csv.DictReader(csv_file)

conn = sqlite3.connect('movies.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS movies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    year INTEGER,
    genre TEXT,
    director TEXT,
    rating REAL
)''')

for row in reader:
    try:
        title = row['movie_title'].strip()
        year = int(row['title_year']) if row['title_year'] else None
        director = row['director_name']
        genre = row['genres'].split('|')[0]
        rating = float(row['imdb_score']) if row['imdb_score'] else None

        if title and year and genre and rating:
            c.execute('INSERT INTO movies (title, year, genre, director, rating) VALUES (?, ?, ?, ?, ?)',
                      (title, year, genre, director, rating))
    except:
        continue

conn.commit()
conn.close()
print("✅ Movies imported successfully from online dataset.")
