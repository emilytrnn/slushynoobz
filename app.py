from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__, template_folder='.')

def query_database(search_term):
    conn = sqlite3.connect('transcripts.db')
    cursor = conn.cursor()

    cursor.execute("SELECT video_id FROM transcripts WHERE transcript LIKE ?", ('%' + search_term + '%',))
    result = cursor.fetchall()

    conn.close()
    return result

@app.route('/', methods=['GET', 'POST'])
def index():
    result = []
    if request.method == 'POST':
        search_term = request.form.get('search_term')
        video_ids = query_database(search_term)
        result = ['https://www.youtube.com/watch?v=' + video_id[0] for video_id in video_ids]

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)