import sqlite3

class DB():
    def __init__(self, db_name):
        self.con = sqlite3.connect(db_name)
        self.cur = self.con.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS songs(title, url)")
    def insert(self, title, url):
        self.cur.execute("INSERT INTO songs VALUES(?, ?)", [title, url])
        self.con.commit()
    def select(self, title):
        self.cur.execute("SELECT * FROM songs WHERE title LIKE ?", ('%'+title+'%',))
        rows = self.cur.fetchall()
        for row in rows:
            print(row)
