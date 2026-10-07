# modules in python
# A module is a file containing Python definitions and statements. 
# The file name is the module name with the suffix .py added. Within a module, 
# the module’s name (as a string) is available as the value of the global variable __name__.
# we can see all the modules list in "help" function.

help("modules")


# example - math ---------------------------------------
import math

print(math.pi)
print(math.floor(3.9))
print(math.ceil(3.9))


# random 
# time 
# os

import os
print(os.curdir)
print(os.getcwd())
