# function in python
# function is a block of code which only runs when it is called.
# after function called global frame will be deleted for memory management
#  function default return None


# exp-1 ----------------------------------------
# without parameter and without return value
def fun_name():
    print("Hello World")

fun_name()


# exp-2 ----------------------------------------
# with parameter and without return value
def hellowUser(name):
    print(f"Hello {name}")

hellowUser("John")

# exp-3
# without parameter and with return value
def is_odd(i):
    if type(i) == int:
        if i%2 == 0:
            return True
        else:
            return False
    else:
        return "Not an initger"

print(is_odd(10))
print(is_odd("11"))   

# exp-4 ----------------------------------------
# with parameter with default value and with return value
def add(a=2, b=3):
    return a + b

print(add(10, 20))
print(add())


# exp-5 ----------------------------------------
# with any number of arguments
# *args is a tuple of arguments


def mul(*args):
    result = 1
    for i in args:
        result *= i
    return result

print(mul(10, 20))
print(mul(3,6, 4,10))

# exp-6 ----------------------------------------
# **kwargs is a dictionary of arguments

def add_dict(**kwargs):
    result = 0
    for i in kwargs.values():
        result += i
    return result

print(add_dict(a=10, b=20, c=30))           

