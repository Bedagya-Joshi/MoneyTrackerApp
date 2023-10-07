import sqlite3
from datetime import date, timedelta

global rows

class Database:
    def __init__(self, db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        sql = """
        CREATE TABLE IF NOT EXISTS Money(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Balance INT NOT NULL,
            Remarks VARCHAR(100),
            Date VARCHAR(50),
            FinalBal INT NOT NULL
        )
        """
        print ("Table created successfully")
        self.cur.execute(sql)
        self.con.commit()

    def insert(self, bal, rem, dat, finbal):
        self.cur.execute("insert into Money values (NULL,?,?,?,?)",(bal, rem, dat, finbal))
        self.con.commit()

    def fetch(self):
        self.cur.execute("SELECT * from Money")
        rows = self.cur.fetchall()
        return rows
    
    def fetchFinal(self):
        self.cur.execute("SELECT * FROM Money ORDER BY FinalBal DESC LIMIT 1")
        rows = self.cur.fetchall()
        return rows

    def search(self,sort):
        find = ("SELECT * FROM Money WHERE Date like ")+f"'{sort}'"
        self.cur.execute(find)
        rows = self.cur.fetchall()
        return rows

    # def rangSearch(self,fdate,ldate):
    #     word = ("SELECT * FROM Money WHERE DATE(Date) BETWEEN ")+f"'{fdate}'"+(" AND ")+f"'{ldate}'"
    #     self.cur.execute(word)
    #     rows = self.cur.fetchall()
    #     return rows

    def delete(self):
        self.cur.execute("DROP TABLE Money")
        self.con.commit()
