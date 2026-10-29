# Python Context Managers and the with Statement 

# A context manager is a Python feature that helps you manage resources safely
#  by handling setup and cleanup automatically.
# The with statement is the most common way to use a context manager.

# Imagine you want to write data into a file.

from ast import Or


file = open("notes.txt", "w")
file.write("This is a test")
file.close()

# The with statement is the most common way to use a context manager.

# This works, but there is a problem: if an error occurs before file.close(), the file might remain open longer than intended.
# We could use try and finally to ensure cleanup:

try:
    file = open("notes.txt", "w")
    file.write("This is a test")
finally:
    file.close()

# This works, but it is not very readable.
# We could use a context manager to ensure cleanup: 

# Using the with statement, we can ensure cleanup:

with open("notes.txt", "w") as file:
    file.write("This is a test")

# The with statement is a context manager that ensures cleanup:
# 1. The file is opened
# 2. The file is written to
# 3. The file is closed


# Or we can use a class to create a context manager:

class MyContext:
    def __enter__(self):
        print("Entering the block")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Leaving the block")


with MyContext() as context:
    print("Doing some work")
