#  Sets 

# important --  1.  set do not allowed duplicates
        #   --  2.  set have no indexing and slicing becuase it follows hashing 
        #   --  3.  sets don't allowed mutable data types
        #   --  4.  sets itself is mutable data type 
        #.  --  5.  you can't access item inside the sets
        #   --  6.  we can't concat the 2 sets only 

#  exp. unic number in 2 sets --->  s1.union(s2)
#  in both sets common     --->  s1.intersection(s2)
#  


s1 = {2,3,4,5,9}
print("s1",s1)

print("id- ",id(s1)) # to check the memory location id


# we can add the element and remove the element in the same memory id
s1.add(10)
print("s1a",s1)

s1.remove(3)
print("s1r",s1)
