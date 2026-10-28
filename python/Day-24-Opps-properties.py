# Properties are a way to define methods that can be accessed like attributes.

class Product:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value


product = Product(100)

print(product.price)  # Calls the getter

product.price = 200   # Calls the setter
print(product.price)

product.price = -50   # Raises ValueError