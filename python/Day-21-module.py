# What is a module? 

# A module is a Python file (.py) that contains code such as functions, variables, 
# or classes that you can reuse in another Python file. [reusable code in python]

# Imagine you have two files:
# calculator.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b


# and main.py

# import calculator from calculator.py [import the module]
# from calculator import add, subtract 

print(calculator.add(1, 2))
print(calculator.subtract(1, 2))
