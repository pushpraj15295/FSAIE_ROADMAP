# Polymorphism is a concept in object-oriented programming that allows objects of different classes to be treated as objects of the same class.

# Polymorphism [Many Forms]
# 1. Method Overriding [Polymorphism] ------------------->  
# Definition: When a child class provides its own implementation of a method already defined in the parent class.
# 2. Method Overloading [Polymorphism] -------------------> 
# Definition: Using the same method name with different parameter lists to perform different operations.
# 3. Operator Overloading [Polymorphism] ------------------->
# Definition: Giving a built-in operator, such as +, -, or *, a custom meaning for objects of your class.



# 1. Method Overriding [Polymorphism] ------------------->  
# Definition: When a child class provides its own implementation of a method already defined in the parent class.
class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):  # Overrides parent method
        print("Dog barks")

class Cat(Animal):
    def sound(self):  # Overrides parent method
        print("Cat meows")

a = Animal()
d = Dog()
c = Cat()

a.sound()  # Animal makes a sound
d.sound()  # Dog barks
c.sound()  # Cat meows



# 2. Method Overloading [Polymorphism] -------------------> 
# Definition: Using the same method name with different parameter lists to perform different operations.

class Calculator:
    def add(self, a, b):
        return a + b

    def add(self, a, b, c):
        return a + b + c

    def add(self, a, b, c, d):
        return a + b + c + d
        
    # area of rectangle
    def area(self, length, width):
        return length * width

    # area of rectangle
    def area(self, length, width, height):
        return length * width * height

    # area of circle
    def area(self, radius):
        return 3.14 * radius * radius

print(c.add(1, 2)) # 3  [Method Overloading]
print(c.add(1, 2, 3)) # 6  [Method Overloading]
print(c.add(1, 2, 3, 4)) # 10  [Method Overloading]

print(c.area(10, 20)) # 200  [Method Overloading]
print(c.area(10, 20, 30)) # 600  [Method Overloading]
print(c.area(10)) # 314  [Method Overloading]




# 3. Operator Overloading
# Definition: Giving a built-in operator, such as +, -, or *, a custom meaning for objects of your class.

class Book:
    def __init__(self, pages):
        self.pages = pages

    def __add__(self, other):
        return self.pages + other.pages

    def __sub__(self, other):
        return self.pages - other.pages

    def __mul__(self, other):
        return self.pages * other.pages

book1 = Book(100)
book2 = Book(200)

print(book1 + book2)  # 300
print(book1 - book2)  # -100
print(book1 * book2)  # 20000   


