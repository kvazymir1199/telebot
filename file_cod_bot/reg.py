import sqlite3


def register(user_name, user_id):
    conn = sqlite3.connect("basa.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER, user TEXT);")
    cur.execute("SELECT id FROM users WHERE id=?", (user_id, ))
    if cur.fetchone() is None:
        cur.execute("INSERT INTO users (id, user) VALUES(?, ?);", (user_id, user_name))
        conn.commit()

    conn.close()
