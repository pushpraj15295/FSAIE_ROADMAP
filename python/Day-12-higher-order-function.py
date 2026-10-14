# higher order function is a function that takes a function as an argument. [inbuilt functions]


# map function ------------------------------------------------------------
# map(function, iterable)

# example 1:
# map function with lambda function
x = map(lambda x : x**2, list(range(1, 11)))
print(list(x)) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# example 2:
# map function with a regular function
def square(x):
    return x ** 2
x = map(square, list(range(5)))
print(list(x)) # [0, 1, 4, 9, 16]  

# example 3:
list_of_students = [
    {"name": "John", "age": 20},
    {"name": "Jane", "age": 21},
    {"name": "Jim", "age": 22},
    {"name": "Jill", "age": 23},
    {"name": "Jack", "age": 24},
]

x = map(lambda x : x["name"], list_of_students)
print(list(x)) # ["John", "Jane", "Jim", "Jill", "Jack"]


# filter function ------------------------------------------------------------
# filter(function, iterable)

# example 1:
# filter function with lambda function
x = filter(lambda x : x % 2 == 0, list(range(1, 11)))
print(list(x)) # [2, 4, 6, 8, 10]

# example 2:
# filter function with a regular function
def is_even(x):
    return x > 4 # true or false  [condition]
x = filter(is_even, list(range(1, 11)))
print(list(x)) # [5, 6, 7, 8, 9, 10]

list_of_students = [
    {"name": "John", "age": 20},
    {"name": "Jane", "age": 21},
    {"name": "Jim", "age": 22},
    {"name": "Jill", "age": 23},
    {"name": "Jack", "age": 24},
]

#  name starts with 'J' 
x = filter(lambda x : x["name"][0] == 'J', list_of_students)        # true or false  [condition]    
print(list(x)) 



# reduce function ------------------------------------------------------------
import functools

# example 1:
# reduce function with lambda function
x = functools.reduce(lambda x, y : x + y, list(range(1, 11)))
print(x) # 55

# example 2:
# reduce function with a regular function
def add(x, y):
    return x + y
x = functools.reduce(add, list(range(1, 11)))
print(x) # 55


# example 3: how to implement a reduce function
# initializer is the starting total. Without it, result begins as the first item.
def reduce(function, iterable, initializer=None):
    items = iter(iterable)
    if initializer is None:
        result = next(items)
    else:
        result = initializer
    for i in items:
        result = function(result, i)
    return result
x = reduce(lambda x, y : x + y, list(range(1, 11)))
print(x) # 55


# add to cart example ------------------------------------------------------------
cart = [
    {"name": "apple", "price": 10},
    {"name": "banana", "price": 20},
    {"name": "cherry", "price": 30},
    {"name": "date", "price": 40},
    {"name": "elderberry", "price": 50},
]

# start at 0. Otherwise x is the first dict, and int(x) fails.
x = reduce(lambda total, item : total + item["price"], cart, 0)
print("total price of the cart is: ", x) # 150



# new example ------------------------------------------------------------
list_of_numbers = [15, 22, 13, 41, 35, 46, 37, 58, 69, 10]

x = reduce(lambda x,y : x if x > y else y, list_of_numbers) # find the largest number
print(x) # 69