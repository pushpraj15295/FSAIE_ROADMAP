# Type Hinting in Python nothing but a way to tell the type of a variable or a function.

# For example:

def add(a: int, b: int) -> int:
    return a + b

print(add(1, 2))

# Understand the syntax:
# - a: int — a is expected to be an integer.
# - b: int — b is expected to be an integer.
# - -> int — the function is expected to return an integer.

# but This still runs and prints: for string 

print(add("hello", "world"))



