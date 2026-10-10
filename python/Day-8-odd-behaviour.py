# odd behaviour in python   

import sys
# example 1
a=2
b=a
c=b

print(sys.getrefcount(a))
# a, b, and c are three names for the same object.
# CPython caches every integer from -5 to 256, so there is only one 2
# in the whole process. The interpreter already holds many references
# to it, so the count is large and changes with the Python version.
# It is not a fixed number such as 48 or 49.
# sys.getrefcount also adds 1 for the temporary reference created
# by passing the object into the function.



# example 2  [-5 to 256]
a = -5
b = -5
print("a-",id(a))
print("b-",id(b))

# or
a = 256
b = 256
print("a-",id(a))
print("b-",id(b))

# but 
a = 257
b = 257
print("a-",id(a))
print("b-",id(b))
# output will be different because 257 is not in the cache      