# lambda function is a small anonymous function 
# that can have any number of arguments, but can only have one expression.
# lambda function is defined using the lambda keyword.
# lambda didn't have a name, it is an anonymous function.
# lambda did not have a return statement, it is an implicit return function.
# we can right a lambda function in one line of code.

# syntax: lambda arguments : expression (return value)


# example 1: simple lambda function
x = lambda a : a + 10
print(x(5))

# example 2: lambda function with multiple arguments
x = lambda a, b : a * b
print(x(5, 6))

# example 3: lambda function with multiple arguments
x = lambda a, b, c : a + b + c
print(x(5, 6, 7))

# example 4: lambda function even or odd
x = lambda a : "Even" if a % 2 == 0 else "Odd"
print(x(5)) # Odd


# lambda used with higher order functions
# higher order function is a function that takes a function as an argument.
# or returns a function.


def return_sum(func, list):
    result = 0
    for i in list:
        if func(i):  
            result += i
    return result

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even = lambda x : x % 2 == 0  # true or false 
odd = lambda x : x % 2 != 0 # true or false 
multiple_of_3 = lambda x : x % 3 == 0 # true or false 

print("even--",return_sum(even, list)) # 30
print("odd--",return_sum(odd, list)) # 25
print("multiple_of_3--",return_sum(multiple_of_3, list)) # 18