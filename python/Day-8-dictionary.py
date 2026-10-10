# dictionary stores the data in the key value pair

#  dict is a mutable data type and has no indexing 
#  keys are imutable only value can be change
#  keys allways unic 
# 
# create a dict [object]

D = {"name":"raj","age":30,"mark":{"math":99,"eng":80}}
print(D["mark"]["math"])

# edit 
D["mark"]["math"] = 100
print(D["mark"]["math"])

# add new 
D["sex"] = "male"
print("D",D)

#  delete 
# del D  -- complete dictionary
# item 
del D["age"]
print("d",D)
# with clear we can crear the complete dectionary 


# loops -----------------------------------------------------------------------
D1 = {"name":"raj","age":30,"mark":{"math":99,"eng":80},"sex":"male","blood":"B+"}

for i in D1:
    print("key",i , "and value is -->" , D1[i])


