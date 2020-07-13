import sqlite3


def connect():
    conn = sqlite3.connect('games.db')
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS game (id INTEGER PRIMARY KEY, title text, gameCompany text, year integer, upc integer)")
    conn.commit()
    conn.close()


def insert(title, gameCompany, year, upc):
    conn = sqlite3.connect('games.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO game VALUES (NULL,?,?,?,?)",
                (title, gameCompany, year, upc))
    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect('games.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM game")
    rows = cur.fetchall()
    conn.close()
    return rows


def delete(id):
    conn = sqlite3.connect('games.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM game WHERE id=?", (id,))
    conn.commit()
    conn.close()


def update(id, title, gameCompany, year, upc):
    conn = sqlite3.connect('games.db')
    cur = conn.cursor()
    cur.execute("UPDATE game SET title=?, gameCompany=?, year=?, upc=? WHERE id=?",
                (title, gameCompany, year, upc, id))
    conn.commit()
    conn.close()


def search(title="", gameCompany="", year="", upc=""):
    conn = sqlite3.connect('games.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM game WHERE title=? OR year=? OR gameCompany=? OR upc=?",
                (title, gameCompany, year, upc))
    rows = cur.fetchall()
    conn.close()
    return rows


connect()
insert('The Last Of Us', 'Naughty Dog', 2012, 711719051794)
print(view())
