# list in python and it's hectrogenous [you can add diffrent data type]
# list are mutable

# create --------------------
l = list()
print("l",l)

l1 = list("welcome")
print("l1",l1)


# edit -----------------------
l3 = [2,4,5,67]
l3[3] = 6
print("l3",l3)
# or
l3[1:3] = [100,200,300]
print("l33",l3)

# add -------------------------

l4 = [2,3,4,5,6]
l4.append(7)  # one item
print("l4",l4)

l4.extend([8,9,10,11]) #mutiple items
print("l4e",l4)

l4.insert(2,"hello")
print("l4i",l4)

# delete ------------------------
del(l4[0])
print("l4d",l4)

# /remove
l4.remove("hello")
print("l4r",l4) #any item 

# pop
l4.pop() 
print("l4p",l4) #last item


# clear
l4.clear()
print("l4c",l4) #remove all the items 

# add as a new list 
l5 = [2,3,4,"-"]
l6 = [5,6,7]

print("l5+l6",l5+l6)

# multiple [copy the list]
print("multi-l5",l5*3)

# length / min / max 
print(len(l6))
print(min(l6))
print(max(l6))


# sorted and reverse sorted [new list]
# sort [same list modify]
l7 = [8,5,7,5,8,89,4]

print("s",sorted(l6))
print("sr",sorted(l6,reverse=True))


# index
l7 = [8, 5, 7, 5, 8, 89, 4]

l7.sort()
print("srt", l7)
print("in", l7.index(7))


# remove dublicate number 
ex = [1,1,2,2,7,2,3,4,5,6,6]
new_l = []
for i in ex:
    if i not in new_l:
        new_l.append(i)

print("nl",new_l)   