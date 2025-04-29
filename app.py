from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

def get_recommendations(genre):
    conn = sqlite3.connect('movies.db')
    cursor = conn.cursor()
    cursor.execute("SELECT title FROM movies WHERE genre = ?", (genre,))
    movies = cursor.fetchall()
    conn.close()
    return [movie[0] for movie in movies]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        genre = request.form['genre']
        movies = get_recommendations(genre)
        return render_template('recommendations.html', movies=movies, genre=genre)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)