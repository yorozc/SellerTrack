class Item:
    def __init__(self, name: str, price: float, og_price: float):
        self._name = name
        self._price = price 
        self._og_price = og_price

    def __repr__(self):
        return f'{self._name}: price: {self._price}, Og_price: {self._og_price}, Profit: {self.profit}'
    
    @property 
    def name(self):
        return self._name
    
    @name.setter 
    def name(self, name):
        print('Name set')
        self._name = name
    
    @property 
    def price(self):
        return self._price
    
    @price.setter 
    def price(self, price):
        print('price set')
        self._price = price

    @property 
    def og_price(self):
        return self._og_price
    
    @og_price.setter 
    def og_price(self, og_price):
        print('og_price set')
        self._og_price = og_price