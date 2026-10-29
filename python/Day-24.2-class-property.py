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

try:
    product.price = -50   # Raises ValueError
except ValueError as error:
    print(error)


# Read-only property example
# Sometimes you want to calculate a value without allowing users to assign it directly.

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height


rectangle = Rectangle(10, 5)

print(rectangle.area)  # 50