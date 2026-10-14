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


# lambda used with higher order functions
# higher order function is a function that takes a function as an argument.
# or returns a function.