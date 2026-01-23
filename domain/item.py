class Item:
    def __init__(self, name: str, price: float, og_price: float, shipping: float, platform_fee: float):
        self._name = name
        self._price = price 
        self._og_price = og_price
        self._shipping = shipping
        self._platform_fee = platform_fee

    def __repr__(self):
        return f'item: {self._name}, price: {self._price}, Og_price: {self._og_price}, shipping: {self._shipping}, platform_fee: {self._platform_fee}'
    
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

    @property
    def shipping(self):
        return self._shipping
    
    @shipping.setter
    def shipping(self, shipping):
        print('shipping set')
        self._shipping = shipping

    @property
    def platform_fee(self):
        return self._platform_fee

    @platform_fee.setter 
    def platform_fee(self, platform_fee):
        print('platform_fee set')
        self._platform_fee = platform_fee
