import sqlite3


class Database:
    def __init__(self,db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS users(username text,password text,email text)")
        self.conn.commit()

    def fetchRecord(self, query,username,password):
        self.cur.execute(query,(username,password))
        rows = self.cur.fetchall()
        return rows
    
    def insertRecord(self,username,password,email):
        self.cur.execute("INSERT INTO users VALUES (?,?,?)",
                         (username,password,email))
        self.conn.commit()







