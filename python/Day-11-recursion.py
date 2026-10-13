# recursion is a function that calls itself

# example 1: factorial
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))

# 5 * factorial(4)
# 4 * factorial(3)
# 3 * factorial(2)
# 2 * factorial(1)
# 1


# example 2: fibonacci ------------------------------------------------------------
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(5))

# fibonacci(4) + fibonacci(3)
# fibonacci(3) + fibonacci(2)
# fibonacci(2) + fibonacci(1)
# fibonacci(1) + fibonacci(0)  
# 1 + 0
# 1
# 1 + 1
# 2
# 2 + 1
# 3
# 3 + 2
# 5
# 5 + 3
# 8