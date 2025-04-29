import sqlite3

conn = sqlite3.connect('movies.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE movies (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        genre TEXT NOT NULL
    )
''')

sample_data = [
    ("Inception", "Action"),
    ("The Matrix", "Action"),
    ("The Hangover", "Comedy"),
    ("Superbad", "Comedy"),
    ("The Godfather", "Drama"),
    ("Forrest Gump", "Drama"),
    ("The Conjuring", "Horror"),
    ("It", "Horror")
]

cursor.executemany("INSERT INTO movies (title, genre) VALUES (?, ?)", sample_data)
conn.commit()
conn.close()