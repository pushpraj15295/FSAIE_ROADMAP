# exceptions : error handling in python with try, except, else, finally or raising custom Error

# try: Attempt the operation.
# except: Handle a failure.
# else: Run after success.
# finally: Run regardless of success or failure.

# Consider this code: --------------------------------------------------------------------------

num = int(input("Enter a number: "))
print(num)

# If the user enters a non-integer, the program will crash.
# To handle this, we can use a try-except block.

try:
    num = int(input("Enter a number: "))
    print(num)
except ValueError:
    print("Invalid input")

# The try block contains the code that may raise an error.
# The except block contains the code to execute if an error occurs.
# The else block contains the code to execute if no error occurs.
# The finally block contains the code to execute regardless of whether an error occurs or not.


# Handling multiple exceptions ------------------------------------------------------------------

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print(a / b)

except ValueError:
    print("Please enter numbers only.")

except ZeroDivisionError:
    print("You cannot divide by zero.")


# The "else" block runs only if no exception occurs in the try block. [optional] -------------------

try:
    num = int(input("Enter number: "))

except ValueError:
    print("Invalid number!")

else:
    print("Conversion successful!")
    print("Your number is:", num)



# The "finally" block runs whether an exception occurs or not, as normal control flow exits the try statement. [optional] -------------------

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = a / b

except ValueError:
    print("Please enter valid integers.")

except ZeroDivisionError:
    print("Division by zero is not allowed.")

else:
    print("Result:", result)

finally:
    print("Calculation attempt completed.")


# Raising custom exceptions with a message ------------------------------------------------------------------

amount = -100

if amount < 0:
    raise ValueError("Expense amount cannot be negative")



# or with class ------------------------------------------------------------------
class NegativeAmountError(Exception):
    pass

if amount < 0:
    raise NegativeAmountError("Amount cannot be negative")

