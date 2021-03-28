import sqlite3

class todo_database:
    def __init__(self, tododb):
        self.conn = sqlite3.connect(tododb)
        self.cur = self.conn.cursor()
        self.cur.execute("""CREATE TABLE IF NOT EXISTS todo_lists (id INTEGER PRIMARY KEY, To_do text, date_added text)""")
        self.conn.commit()


    def fetch(self):
        self.cur.execute("SELECT * FROM todo_lists")
        rows = self.cur.fetchall()
        return rows


    def insert(self, To_do, date_added):
        self.cur.execute('INSERT INTO todo_lists VALUES(NULL, ?,?)', (str(To_do), str(date_added)))
        self.conn.commit()

    def remove(self,id):
        self.cur.execute('DELETE FROM todo_lists WHERE id=?', (id,))
        self.conn.commit()

    
    def __del__(self):
        self.conn.close()

