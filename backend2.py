import sqlite3


def connect():
    conn = sqlite3.connect('games2.db')
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS game (id INTEGER PRIMARY KEY, title text, gameCreator text, year integer, upc integer)")
    conn.commit()
    conn.close()


def insert(title, gameCreator, year, upc):
    conn = sqlite3.connect('games2.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO game VALUES (NULL,?,?,?,?)",
                (title, gameCreator, year, upc))
    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect('games2.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM game")
    rows = cur.fetchall()
    conn.close()
    return rows


def search(title="", gameCreator="", year="", upc=""):
    conn = sqlite3.connect('games2.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM game WHERE title=? OR year=? OR gameCreator=? OR upc=?",
                (title, year, gameCreator, upc))
    rows = cur.fetchall()
    conn.close()
    return rows


def delete(id):
    conn = sqlite3.connect('games2.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM game WHERE id=?", (id,))
    conn.commit()
    conn.close()


def update(id, title, gameCreator, year, upc):
    conn = sqlite3.connect('games2.db')
    cur = conn.cursor()
    cur.execute("UPDATE game SET title=?, gameCreator=?, year=?, upc=? WHERE id=?",
                (title, gameCreator, year, upc, id))
    conn.commit()
    conn.close()


# connect()
#rint(search(gameCreator="Naughty Dog"))
delete(18)
print(view())
