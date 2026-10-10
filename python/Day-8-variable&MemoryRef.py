# variable and there Memory Refrence in the python  
# python call varible as a name of the memory location 
# call by object reference 


# what is aliasing ?
#  when two or more varible are pointing to the same memory location 
#  example 
a = 10 
b = a 
print(id(a))
print(id(b))
print(a is b)
# output will be true 
# because a and b are pointing to the same memory location 
# this is called aliasing


# with get ref count we can know how many varible are pointing to the same memory location
import sys

print(sys.getrefcount(a))
print(sys.getrefcount(b))
# output will be 2 
# because a and b are pointing to the same memory location 
# this is called aliasing 