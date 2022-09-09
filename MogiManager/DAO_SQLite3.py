import sqlite3 as SQL
import DAO_VARIABLE as V

#variable_name
#FunctionName

class Dao():
    def __init__(self):
        self._file_name = "Date.db"
        self.conn = SQL.connect(self._file_name)

    def CreatItemsTable(self):
        cur = self.conn.cursor()

        query = '''CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY AUTOINCREMENT, item TEXT, price INTEGER, inTax BLOB, redTax BLOB, stock TEXT)'''

        cur.execute(query)
        self.conn.commit()

    def DropItemsTable(self):
        cur = self.conn.cursor()

        query = '''DROP TABLE IF EXISTS items'''

        cur.execute(query)
        self.conn.commit()

    def AddItem(self, identity: V.item):
        self.CreatItemsTable()

        cur = self.conn.cursor()

        data = (identity.name, identity.price, identity.inTax, identity.reduceTax, identity.stocks)
        query = 'INSERT INTO items (item, price, inTax, redTax, stock) VALUES (?, ?, ?, ?, ?)'

        cur.execute(query, data)
        self.conn.commit()

    def UpdateItem(self, identity: V.item):
        self.CreatItemsTable()

        cur = self.conn.cursor()

        data = (identity.name, identity.price, identity.inTax, identity.reduceTax, identity.stocks, identity.id)
        query = 'UPDATE items SET item=?, price=?, inTax=?, redTax=?, stock=? WHERE id=?'

        cur.execute(query, data)
        self.conn.commit()

    def DeleteItem(self, id: int):
        self.CreatItemsTable()

        id = (id,)
        cur = self.conn.cursor()

        cur.execute("DELETE FROM items WHERE id=?", id)
        self.conn.commit()

    def FindAllItems(self):
        self.CreatItemsTable()

        cur = self.conn.cursor()

        ret = []
        for data in cur.execute("SELECT * FROM items"):
            print(data)
            d = V.item()
            d.id = data[0]
            d.name = data[1]
            d.price = data[2]
            d.inTax = data[3]
            d.reduceTax = data[4]
            d.stocks = data[5]

            ret.append(d)

        return ret

    def FindItemById(self, id: int):
        self.CreatItemsTable()

        id = (id,)
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM items WHERE id=?", id)

        data = cur.fetchone()
        
        ret = V.item()
        if(data != None):
            ret.id = data[0]
            ret.name = data[1]
            ret.price = data[2]
            ret.inTax = data[3]
            ret.reduceTax = data[4]
            ret.stocks = data[5]
            
            return ret
        else:
            return None

