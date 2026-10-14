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




