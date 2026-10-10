# Garbage colletion in python 
# Garbage colletion is the process of collecting the garbage from the memory 
# Garbage is the memory that is not used by the program 
# Garbage collection is done by the python interpreter automatically 

# how garbage collection works in python ?
#  It check that is there any memory which has no reference 
#  if there is no reference then it is garbage and it is collected by the garbage collector 
#  and the memory is freed up 

# example 
a = 10 
b = a 
print(id(a))
print(id(b))
del a
del b
print(id(10)) # 10 is in same memory 
print(id(a)) # but for a we deleted the refrence from the memory

# output will be NameError: name 'a' is not defined
# if not refrence then it is garbage and it is collected by the garbage collector 