class item():
    def __init__(self):
        self._name: str
        self._price: int
        self._inTax: str
        self._reduceTax: str
        self._stocks: str

    @property
    def name(self):
        pass
    @name.getter
    def name(self):
        return self._name
    @name.setter
    def name(self, name: str):
        self._name = name

    @property
    def price(self):
        pass
    @price.getter
    def price(self):
        return self._price
    @price.setter
    def price(self, price: int):
        self._price = price

    @property
    def inTax(self):
        pass
    @inTax.getter
    def inTax(self):
        return self._inTax
    @inTax.setter
    def inTax(self, inTax: str):
        self._inTax = inTax

    @property
    def reduceTax(self):
        pass
    @reduceTax.getter
    def reduceTax(self):
        return self._reduceTax
    @reduceTax.setter
    def reduceTax(self, reduceTax: str):
        self._reduceTax = reduceTax
    
    @property
    def stocks(self):
        pass
    @stocks.getter
    def stocks(self):
        return self._stocks
    @stocks.setter
    def stocks(self, stocks: str):
        self._stocks = stocks

class stock():
    @property
    def change(self):
        pass
    @change.getter
    def change(self):
        return self._change
    @change.setter
    def change(self, change):
        self._change = change
