# loops used to repeat a block of code multiple times.
#  There are two types of loops in Python: for loops and while loops.

# while loop in python -----------------------------
i = 1
while i <= 5:
    print(i)
    print("multiple of 2", i * 2)
    i += 1  


# for loop in python --------------------------------
arr = [1, 2, 3, 4, 5,67, 8, 9, 10]
for i in arr:
    print(i)    


#  example of for loop with range() function in python ------------------------
for i in range(1, 11):
    print(i)



# or
new_list = list(range(11,1,-1))

for i in new_list:
    print(i)    


# example of nested for loop in python ---------------------------------------
for i in range(1, 6):
    for j in range(1, 6):
        print(i, j) 


        
# new way to use loops 
l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# duble the value of each element in the l1
l2 = [i * 2 for i in l1]
print(l2)   


# or even more advanced way to use loops with if statement
l3 = [i * 2 for i in l1 if i % 2 == 0]
print(l3)   