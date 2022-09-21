import sqlite3 as SQL
import DAO_VARIABLE as V
import Global as G

#variable_name
#FunctionName

class Dao():
    # Common
    def __init__(self):
        self._file_name = G.OpenDateYear + "_Data.db"
        self.conn = SQL.connect(self._file_name)

        self.productsTableName = "items"
        self.ordersTableName = "O" + G.OpenDateStr

    def BinToBool(num: int):
        if(num==1):
            return True
        else:
            return False

    # Products
    def CreatItemsTable(self):
        cur = self.conn.cursor()

        query = "CREATE TABLE IF NOT EXISTS "\
                + self.productsTableName + "("\
                "id INTEGER PRIMARY KEY AUTOINCREMENT, "\
                "item TEXT, "\
                "price INTEGER, "\
                "inTax BLOB, "\
                "redTax BLOB, "\
                "stock TEXT"\
                ")"

        cur.execute(query)
        self.conn.commit()

    def DropItemsTable(self):
        cur = self.conn.cursor()

        query = "DROP TABLE IF EXISTS " + self.productsTableName

        cur.execute(query)
        self.conn.commit()

    def AddItem(self, identity: V.item):
        self.CreatItemsTable()

        cur = self.conn.cursor()

        data = (identity.name, identity.price, identity.inTax, identity.reduceTax, identity.stocks)
        query = "INSERT INTO "\
                + self.productsTableName + "("\
                "item, "\
                "price, "\
                "inTax, "\
                "redTax, "\
                "stock"\
                ") VALUES (?, ?, ?, ?, ?)"

        cur.execute(query, data)
        self.conn.commit()

    def UpdateItem(self, identity: V.item):
        self.CreatItemsTable()

        cur = self.conn.cursor()

        data = (identity.name, identity.price, identity.inTax, identity.reduceTax, identity.stocks, identity.id)
        query = "UPDATE"\
                + self.productsTableName + " SET "\
                "item=?, "\
                "price=?, "\
                "inTax=?, "\
                "redTax=?, "\
                "stock=? "\
                "WHERE id=?"

        cur.execute(query, data)
        self.conn.commit()

    def DeleteItem(self, id: int):
        self.CreatItemsTable()
        
        cur = self.conn.cursor()

        id = (id,)
        query = "DELETE FROM " + self.productsTableName + "WHERE id=?"
    
        cur.execute(query, id)
        self.conn.commit()

    def FindAllItems(self):
        self.CreatItemsTable()

        cur = self.conn.cursor()

        query = "SELECT * FROM " + self.productsTableName

        ret = []
        for data in cur.execute(query):
            print(data)
            d = V.item()
            d.id = data[0]
            d.name = data[1]
            d.price = data[2]
            ret.inTax = __class__.BinToBool(data[3])
            ret.reduceTax = __class__.BinToBool(data[4])
            d.stocks = data[5]

            ret.append(d)

        return ret

    def FindItemById(self, id: int):
        self.CreatItemsTable()
        
        cur = self.conn.cursor()
        
        id = (id,)
        query = "SELECT * FROM " + self.productsTableName + " WHERE id=?"
        
        cur.execute(query, id)

        data = cur.fetchone()
        ret = V.item()
        if(data != None):
            ret.id = data[0]
            ret.name = data[1]
            ret.price = data[2]
            ret.inTax = __class__.BinToBool(data[3])
            ret.reduceTax = __class__.BinToBool(data[4])
            ret.stocks = data[5]
            
            return ret
        else:
            return None

    # Orders
    def CreatOrdersTable(self):
        cur = self.conn.cursor()

        query = "CREATE TABLE IF NOT EXISTS "\
                + self.ordersTableName + " ("\
                "id INTEGER PRIMARY KEY AUTOINCREMENT, "\
                "refNum INTEGER, "\
                "orderTime TEXT, "\
                "orders TEXT, "\
                "total INTEGER, "\
                "inTax INTEGER, "\
                "outTax INTEGER, "\
                "receive INTEGER, "\
                "changes INTEGER, "\
                "state TEXT"\
                ")"

        cur.execute(query)
        self.conn.commit()

    def DropOrdersTable(self):
        cur = self.conn.cursor()

        query = "DROP TABLE IF EXISTS " + self.ordersTableName

        cur.execute(query)
        self.conn.commit()

    def AddOrder(self, order: V.order):
        self.CreatOrdersTable()

        cur = self.conn.cursor()

        data = (order.refNum, 
                order.orderTime, 
                order.orders, 
                order.total, 
                order.inTax, 
                order.outTax, 
                order.receive, 
                order.changes, 
                order.state)
        query = "INSERT INTO "\
                + self.ordersTableName + " ("\
                "refNum, "\
                "orderTime, "\
                "orders, "\
                "total, "\
                "inTax, "\
                "outTax, "\
                "receive, "\
                "changes, "\
                "state"\
                ") VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"

        cur.execute(query, data)
        self.conn.commit()

    def UpdateOrder(self, order: V.order):
        self.CreatOrdersTable()

        cur = self.conn.cursor()

        data = (order.refNum, 
                order.orderTime, 
                order.orders, 
                order.total, 
                order.inTax, 
                order.outTax, 
                order.receive, 
                order.changes, 
                order.state, 
                order.id)
        query = "UPDATE "\
                + self.ordersTableName + " SET "\
                "refNum=?, "\
                "orderTime=?, "\
                "orders=?, "\
                "total=?, "\
                "inTax=?, "\
                "outTax=?, "\
                "receive=?, "\
                "changes=?, "\
                "state=? "\
                "WHERE id=?"

        cur.execute(query, data)
        self.conn.commit()

    def DeleteOrder(self, id: int):
        self.CreatOrdersTable()
        
        cur = self.conn.cursor()

        id = (id,)
        query = "DELETE FROM " + self.ordersTableName + " WHERE id=?"

        cur.execute(query, id)
        self.conn.commit()

    def FindAllOrder(self):
        self.CreatOrdersTable()

        cur = self.conn.cursor()

        query = "SELECT * FROM " + self.ordersTableName

        ret = []
        for data in cur.execute(query):
            print(data)
            d = V.order()
            d.id = data[0]
            d.refNo = data[1]
            d.orderTime = data[2]
            d.orders = data[3]
            d.total = data[4]
            d.inTax = data[5]
            d.outTax = data[6]
            d.receive = data[7]
            d.changes = data[8]
            d.state = data[9]

            ret.append(d)

        return ret

    def FindOrderById(self, id: int):
        self.CreatOrdersTable()
        
        cur = self.conn.cursor()
        
        id = (id,)
        query = "SELECT * FROM " + self.ordersTableName + " WHERE id=?"

        cur.execute(query, id)

        data = cur.fetchone()
        ret = V.order
        if(data != None):
            print(data)
            d = V.order()
            d.id = data[0]
            d.refNo = data[1]
            d.orderTime = data[2]
            d.orders = data[3]
            d.total = data[4]
            d.inTax = data[5]
            d.outTax = data[6]
            d.receive = data[7]
            d.changes = data[8]
            d.state = data[9]

            return ret
        else:
            return None