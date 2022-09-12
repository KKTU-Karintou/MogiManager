import sqlite3 as SQL
import DAO_VARIABLE as V
import Global as G

#variable_name
#FunctionName

class Dao():
    # Common
    def __init__(self):
        self._file_name = "Date.db"
        self.conn = SQL.connect(self._file_name)

        self.ordersTable = "O" + G.OpenDateStr

    # Products
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
        query = "INSERT INTO items (item, price, inTax, redTax, stock) VALUES (?, ?, ?, ?, ?)"

        cur.execute(query, data)
        self.conn.commit()

    def UpdateItem(self, identity: V.item):
        self.CreatItemsTable()

        cur = self.conn.cursor()

        data = (identity.name, identity.price, identity.inTax, identity.reduceTax, identity.stocks, identity.id)
        query = "UPDATE items SET item=?, price=?, inTax=?, redTax=?, stock=? WHERE id=?"

        cur.execute(query, data)
        self.conn.commit()

    def DeleteItem(self, id: int):
        self.CreatItemsTable()
        
        cur = self.conn.cursor()

        id = (id,)
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

    # Orders
    def CreatOrdersTable(self):
        cur = self.conn.cursor()

        query = "CREATE TABLE IF NOT EXISTS " + self.ordersTable + " (id INTEGER PRIMARY KEY AUTOINCREMENT, refNum INTEGER, orderTime TEXT, orders TEXT, state TEXT)"

        cur.execute(query)
        self.conn.commit()

    def DropOrdersTable(self):
        cur = self.conn.cursor()

        query = "DROP TABLE IF EXISTS " + self.ordersTable

        cur.execute(query)
        self.conn.commit()

    def AddOrder(self, order: V.order):
        self.CreatOrdersTable()

        cur = self.conn.cursor()

        data = (order.refNum, order.orderTime, order.orders, order.state)
        query = "INSERT INTO " + self.ordersTable + " (refNum, orderTime, orders, state) VALUES (?, ?, ?, ?)"

        cur.execute(query, data)
        self.conn.commit()

    def UpdateOrder(self, order: V.order):
        self.CreatOrdersTable()

        cur = self.conn.cursor()

        data = (order.orders, order.state, order.id)
        query = "UPDATE " + self.ordersTable + " SET orders=?, state=? WHERE id=?"

        cur.execute(query, data)
        self.conn.commit()

    def DeleteOrder(self, id: int):
        self.CreatOrdersTable()
        
        cur = self.conn.cursor()

        id = (id,)
        query = "DELETE FROM " + self.ordersTable + " WHERE id=?"
        cur.execute(query, id)
        self.conn.commit()

    def FindAllOrder(self):
        self.CreatOrdersTable()

        cur = self.conn.cursor()

        ret = []
        for data in cur.execute("SELECT * FROM " + self.ordersTable):
            print(data)
            d = V.order()
            d.id = data[0]
            d.refNo = data[1]
            d.orderTime = data[2]
            d.orders = data[3]
            d.state = data[4]

            ret.append(d)

        return ret

    def FindOrderById(self, id: int):
        self.CreatOrdersTable()

        id = (id,)
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM " + self.ordersTable + " WHERE id=?", id)

        data = cur.fetchone()

        ret = V.order
        if(data != None):
            print(data)
            d = V.order()
            d.id = data[0]
            d.refNo = data[1]
            d.orderTime = data[2]
            d.orders = data[3]
            d.state = data[4]

            return ret
        else:
            return None