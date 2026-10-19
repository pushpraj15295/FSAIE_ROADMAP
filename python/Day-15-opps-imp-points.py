# class objesct are also mutable like list, dictionary, set etc.
class Customer:
    def __init__(self,name):
        self.name = name 

# function 
def greet(customer):
    print(id(customer))
    customer.name = "John" # this is mutable from inside the function
    print(id(customer))
    print(customer.name)


customer1 = Customer("Raj")
greet(customer1)
# to avoid mutability from inside the function this we can use deepcopy
# from copy import deepcopy
# customer2 = deepcopy(customer1)

print(id(customer1))
# print(id(customer2))
print(customer1.name)


# collections of objects ----------------------------------------------------
class Customer:
    def __init__(self,name):
        self.name = name 

customers = [Customer("Raj"), Customer("John"), Customer("Doe")]

for customer in customers:
    print(customer.name)

# collections of objects are also mutable like list, dictionary, set etc.


# static counter ------------------------------------------------------------

class Counter:
    count = 0 
    def __init__(self):
        Counter.count += 1
    # @staticmethod # static method is a method that is not bound to any instance of the class
    def get_count():
        return Counter.count

counter1 = Counter()
print(Counter.get_count()) # 1
counter2 = Counter()
print(Counter.get_count()) # 2
counter3 = Counter()
print(Counter.get_count()) # 3


# that counter is incremented for each call of the constructor by +1

