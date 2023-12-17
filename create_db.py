import sqlite3

conn = sqlite3.connect('transcripts.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS transcripts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        video_id TEXT,
        transcript TEXT
    )
''')

# # Insert some data
# cursor.execute("INSERT INTO your_table (column_name) VALUES ('example')")
# cursor.execute("INSERT INTO your_table (column_name) VALUES ('another_example')")

conn.commit()
conn.close()