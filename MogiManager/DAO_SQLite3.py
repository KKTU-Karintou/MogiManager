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
        self.conn.row_factory = SQL.Row

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
        query = "UPDATE "\
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

        id = (id, )
        query = "DELETE FROM " + self.productsTableName + " WHERE id=?"
    
        cur.execute(query, id)
        self.conn.commit()

    def FindAllItems(self):
        self.CreatItemsTable()

        cur = self.conn.cursor()

        query = "SELECT * FROM " + self.productsTableName
        cur.execute(query)

        ret = []
        while(True):
            data = cur.fetchone()
            if(data!=None):
                print(tuple(data))
                d = V.item()
                d.id = data["id"]
                d.name = data["item"]
                d.price = data["price"]
                d.inTax = __class__.BinToBool(data["inTax"])
                d.reduceTax = __class__.BinToBool(data["redTax"])
                d.stocks = data["stock"]

                ret.append(d)
            else:
                break
        return ret

    def FindItemById(self, id: int):
        self.CreatItemsTable()
        
        cur = self.conn.cursor()
        
        id = (id,)
        query = "SELECT * FROM " + self.productsTableName + " WHERE id=?"
        
        cur.execute(query, id)

        data = cur.fetchone()
        if(data != None):
            ret = V.item()
            ret.id = data["id"]
            ret.name = data["item"]
            ret.price = data["price"]
            ret.inTax = __class__.BinToBool(data["inTax"])
            ret.reduceTax = __class__.BinToBool(data["redTax"])
            ret.stocks = data["stock"]
            
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

    def FindAllOrders(self):
        self.CreatOrdersTable()

        cur = self.conn.cursor()

        query = "SELECT * FROM " + self.ordersTableName
        cur.execute(query)

        ret = []
        while(True):
            data = cur.fetchone()
            if(data!=None):
                print(tuple(data))
                d = V.order()
                d.id = data["id"]
                d.refNum = data["refNum"]
                d.orderTime = data["orderTime"]
                d.orders = data["orders"]
                d.total = data["total"]
                d.inTax = data["inTax"]
                d.outTax = data["outTax"]
                d.receive = data["receive"]
                d.changes = data["changes"]
                d.state = data["state"]

                ret.append(d)
            else:
                break
    
        return ret

    def FindOrderById(self, id: int):
        self.CreatOrdersTable()
        
        cur = self.conn.cursor()
        
        id = (id,)
        query = "SELECT * FROM " + self.ordersTableName + " WHERE id=?"

        cur.execute(query, id)

        data = cur.fetchone()
        if(data != None):
            print(tuple(data))
            d = V.order()
            d.id = data["id"]
            d.refNum = data["refNum"]
            d.orderTime = data["orderTime"]
            d.orders = data["orders"]
            d.total = data["total"]
            d.inTax = data["inTax"]
            d.outTax = data["outTax"]
            d.receive = data["receive"]
            d.changes = data["changes"]
            d.state = data["state"]

            return d
        else:
            return None

    def CheckRefnumUsing(self, refnum: int):
        self.CreatOrdersTable()
        
        cur = self.conn.cursor()
        
        refnum = (refnum,)
        query = "SELECT * FROM " + self.ordersTableName + " WHERE refNum=?"
        cur.execute(query, refnum)

        ret = []
        while(True):
            data = cur.fetchone()
            if(data!=None):
                print(tuple(data))
                state = data["state"]
                if(state=="ordered" or state=="available"):
                    return False
            else:
                break

        return True