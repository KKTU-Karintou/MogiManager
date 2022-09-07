from math import prod
import sqlite3 as SQL
import DAO_VARIABLE as V

class Dao():
    def __init__(self):
        self._fileName = "MMDate.db"
        self.conn = SQL.connect(self._fileName)
    
    def CreatItemsTable(self):
        cur = self.conn.cursor()

        query = '''CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY AUTOINCREMENT, item TEXT, price INTEGER, inTax TEXT, redTax TEXT, stock TEXT)'''

        cur.execute(query)
        self.conn.commit()

    def AddItem(self, identity: V.item):
        cur = self.conn.cursor()

        data = (identity.name, identity.price, identity.inTax, identity.reduceTax, identity.stocks)
        query = 'INSERT INTO items (item, price, inTax, redTax, stock) VALUES (?, ?, ?, ?, ?)'

        cur.execute(query, data)
        self.conn.commit()

    def FindItem(self):
        cur = self.conn.cursor()
        for d in cur.execute("SELECT * FROM items"):
            print(d)

d = Dao()
d.CreatItemsTable()
product = V.item()
product.name = "test1"
product.price = 100
product.inTax = "True"
product.reduceTax = "False"
product.stocks = "1, 2, 3"

d.AddItem(product)
d.FindItem()

input()

d.conn.close()