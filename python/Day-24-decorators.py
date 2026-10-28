# decorators are a way to modify the behavior of a function or method.
# A decorator in Python is a function that adds extra functionality to another function or method without changing its original code.


# Imagine you have a function that prints a message
def say_hello():
    print("Hello!")

say_hello()


# Now, suppose you want to print a message before and after every function call. 
# You could modify the function, but what if you want this behavior for 100 different functions?

# A decorator lets you add this behavior without changing each function's code.


def my_decorator(func):
    def wrapper():
        print("Before function execution")

        func()

        print("After function execution-------------")

    return wrapper


@my_decorator
def say_hello():
    print("Hello!")


say_hello()



# Let's understand each part.
# - my_decorator(func) receives the original function.
# - wrapper() adds behavior before and after calling it.
# - func() executes the original function.
# - return wrapper returns the enhanced function.
# - @my_decorator applies the decorator to say_hello or any other function.

# Now, whenever you call say_hello(), it will print "Before function execution" and "After function execution".

# You can apply the decorator to any function:

@my_decorator
def say_goodbye():
    print("Goodbye!")

say_goodbye()










# Practical use case: Logging function execution --------------------------------
# Suppose your Expense Tracker app has several functions, and you want to know when each function starts and finishes.

from functools import wraps

def log_execution(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Starting: {func.__name__}")

        result = func(*args, **kwargs)

        print(f"Finished: {func.__name__}")

        return result

    return wrapper


@log_execution
def add_expense(amount, category):
    print(f"Added ₹{amount} for {category}")
    return amount


total = add_expense(500, "Food")
print("Returned amount:", total)


# What is new here?
# - *args allows positional arguments, such as 500.
# - **kwargs allows keyword arguments, such as category="Food".
# - result = func(...) captures the original function's return value.
# - return result preserves that return value.
# - @wraps(func) preserves useful metadata such as the original function's name.