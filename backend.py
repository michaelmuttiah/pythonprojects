#Backend sql DB for Books Tkinter GUI
import sqlite3

class Database:

    #Establish database connection and create table
    def __init__(self,db):
        self.conn=sqlite3.connect(db)
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS book1 ( id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer) ")
        self.conn.commit()

    #Function for Add Entry Button
    def add_entry(self,title, author, year, isbn):
        self.cur.execute("INSERT INTO book1 VALUES (NULL,?,?,?,?)",(title,author,year,isbn))
        self.conn.commit()

    #Funtion for View All Button
    def view_all(self):
        self.cur.execute("SELECT * FROM book1")
        rows=self.cur.fetchall()
        return rows

    #Function for Search Entry Button
    def search(self,title="",author="",year="",isbn=""):
        self.cur.execute("SELECT * FROM book1 WHERE title=? OR author=? OR year=? OR isbn=?",(title,author,year,isbn))
        rows=self.cur.fetchall()
        return rows

    #Function for Delete Selected Button
    def delete(self,id):
        self.cur.execute("DELETE FROM book1 WHERE id=?",(id,))
        self.conn.commit()

    #Function for Update Selected Button
    def update(self,id,title,author,year,isbn):
        self.cur.execute("UPDATE book1 SET title=?, author=?, year=?, isbn=? WHERE id=?",(title,author,year,isbn,id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()