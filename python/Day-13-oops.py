# Oops concept in python ------------------------------------------------

# what is object ? that need understand first before understanding oops
# ans: object is instance of class

# what is class ? that need understand first before understanding oops
# ans: class is blueprint of object

# what is inheritance ? that need understand first before understanding oops
# ans: inheritance is a mechanism that allows a class to inherit properties and methods from another class

# what is polymorphism ? that need understand first before understanding oops
# ans: polymorphism is a mechanism that allows a class to take on multiple forms

# what is encapsulation ? that need understand first before understanding oops  
# ans: encapsulation is a mechanism that allows a class to encapsulate its properties and methods

# what is abstraction ? that need understand first before understanding oops
# ans: abstraction is a mechanism that allows a class to abstract its properties and methods

# what is inheritance ? that need understand first before understanding oops
# ans: inheritance is a mechanism that allows a class to inherit properties and methods from another class

# what is polymorphism ? that need understand first before understanding oops
# ans: polymorphism is a mechanism that allows a class to take on multiple forms

# what is oops ? that need understand first before understanding oops
# ans: oops is a programming paradigm that allows a class to encapsulate its properties and methods


# class besic structure ------------------------------------------------
# use pascal case for class name
# variable name use snake_case
# function name use snake_case  

class Dog:
    name = "Buddy"
    age = 3
    breed = "Labrador"
    color = "Brown"
    gender = "Male"
    owner = "John"
    owner_age = 30
    owner_gender = "Male"
    owner_email = "john@example.com"
    owner_phone = "1234567890"
    def bark(self):
        print(f"{self.name} is barking")

dog1 = Dog()
print(dog1.name)
print(dog1.bark())


# what is custom object ? that need understand first before understanding oops
# ans: custom object is a object that is created by the user to represent a real world entity.
# example: Dog, Cat, Bird, Fish, etc.

# what is standard object ? that need understand first before understanding oops
# ans: standard object is a object that is created by the python interpreter to represent a real world entity.
# example: int, float, str, bool, list, tuple, dict, set, etc.

# what is built-in object ? that need understand first before understanding oops
# ans: built-in object is a object that is created by the python interpreter to represent a real world entity.  
# example: print, input, len, type, etc.


#  what is difference between Inheritance and Composition ? ------------------------------------------------------------------

# The easiest way to remember the difference is:

# - Inheritance = IS-A relationship [Parent -> Child] [is a]

# example: Dog is a Animal [Dog -> Animal]
# example: Car is a Vehicle [Car -> Vehicle]
# example: House is a Building [House -> Building]
# example: Person is a Human [Person -> Human]
# example: Employee is a Person [Employee -> Person]
# example: Manager is a Employee [Manager -> Employee]
# example: Developer is a Employee [Developer -> Employee]
# example: Tester is a Employee [Tester -> Employee]


# - Composition = HAS-A relationship [Object -> Object] [has a]

# example: Car has a Engine [Car -> Engine]
# example: House has a Building [House -> Building]
# example: Person has a Human [Person -> Human]
# example: Employee has a Person [Employee -> Person]
# example: Manager has a Employee [Manager -> Employee]
# example: Developer has a Employee [Developer -> Employee]
# example: Tester has a Employee [Tester -> Employee]



# what is the difference between abstraction and encapsulation ? ------------------------------------------------------------------

# The easiest way to remember the difference is: 

# - Abstraction = Hiding implementation complexity. 

from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class CreditCardPayment(Payment):

    def pay(self, amount):
        print(f"Paid ₹{amount} using credit card")


class UpiPayment(Payment):

    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI")


payment = UpiPayment()
payment.pay(500)


# - Encapsulation = Protecting and controlling access to data.

class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")

        self.__balance += amount

    def get_balance(self):
        return self.__balance


account = BankAccount(1000)

account.deposit(500)

print(account.get_balance())


