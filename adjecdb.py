import sqlite3

class adj_database:
    def __init__(self, adjecdb):
        self.conn = sqlite3.connect(adjecdb)
        self.cur = self.conn.cursor()
        #self.cur.execute('CREATE TABLE foodadjective (adjective TEXT)')
        #self.cur.execute("INSERT INTO foodadjective VALUES ('SALTY,')")
        self.conn.commit()

    def get_data(self):
        self.cur.execute("SELECT * FROM foodadjective")
        rows = self.cur.fetchall()
        return rows
    
    def addtodb(self, word):
        self.cur.execute("INSERT INTO foodadjective VALUES(?)", (word,))
        self.conn.commit()
    
    def delete_list(self):
        self.cur.execute("DELETE FROM foodadjective")
        self.conn.commit()
    
    
    def __del__(self):
        self.conn.close()