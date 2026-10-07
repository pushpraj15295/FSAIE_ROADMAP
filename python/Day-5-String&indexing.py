# indexing and opration in the string
string = "Hello world"

print("specific -- ",string[4])
print("slice -- ",string[2:8])
print("slice--" , string[2:])
print("slice--" , string[:5])
print("slice--" , string[:])
print("slice--" , string[2:8:2]) # last one is step 
print("reverse",  string[::-1])  # reverse the string


# edit the string is not posiable becuase string are Immutable  also we c't delete the charecter in the str.

# string concat
c = "hello" + "raj"
print("c-",c)

# multiply str'
m = "raj"*5
print("m-",m)

# loop in str ----------------------
s = "hello Raj bro"
for i in s[0:8:2]:
    print("i-->",i)

# or 
for i in s[::-1]:
    print("rvrs--->",i)