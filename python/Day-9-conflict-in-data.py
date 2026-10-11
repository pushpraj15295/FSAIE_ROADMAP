#  Data Integrity: Conflict in Data 

# Example 1:
a = [1, 2, 3, 4, 5]
b = a

b.append(6) # This will change the value of a as well because b is a reference to a

print(a) # [1, 2, 3, 4, 5, 6]
print(b) # [1, 2, 3, 4, 5, 6]

# To avoid this, we can use the copy() method
c = a.copy() # OR c = a[:]

c.append(7)

print(a) # [1, 2, 3, 4, 5, 6]
print(c) # [1, 2, 3, 4, 5, 6, 7]

# Example 2:
a = {1, 2, 3, 4, 5}
b = a

b.add(6) # This will change the value of a as well because b is a reference to a

print(a) # {1, 2, 3, 4, 5, 6}
print(b) # {1, 2, 3, 4, 5, 6}   # This is a set, so the order of the elements is not guaranteed

# To avoid this, we can use the copy() method
c = a.copy() # OR c = a[:]

c.add(7)    

print(a) # {1, 2, 3, 4, 5, 6}
print(c) # {1, 2, 3, 4, 5, 6, 7}

# Example 3: