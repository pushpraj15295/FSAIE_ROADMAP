# Data classes are a way to create classes that are primarily used to store data.

# Suppose you want to store expense details in your Expense Tracker project.

class Expense:
    def __init__(self, category, amount, date):
        self.category = category
        self.amount = amount
        self.date = date


expense = Expense("Food", 250, "2026-10-27")

print(expense.category)
print(expense.amount)


# This works, but you have to write the __init__() method yourself.
# We can use dataclasses to simplify this.

from dataclasses import dataclass


@dataclass
class Expense:
    category: str
    amount: float
    date: str


expense = Expense("Food", 250, "2026-10-27")

print(expense)
print(expense.category)
print(expense.amount)


# What does @dataclass generate?
# By default, it generates several useful methods.

#    Method	                Purpose
# __init__()	     Initializes the object's fields
# __repr__()	    Provides a readable representation
# __eq__()	        Compares objects by their fields