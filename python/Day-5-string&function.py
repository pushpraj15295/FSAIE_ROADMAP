# String and function

s = "Indian Army"
print(len(s))

print(max(s)) #according to ask val

print(min(s))

print(sorted(s))


# capitalize  / upper / Lower / title / Swapcase 
print(s.capitalize())
print(s.upper())
print(s.lower())
print(s.title())
print(s.swapcase())

# count 
print(s.count("n"))


# find and index same but find don't show error if not find 
print(s.find("r")) 
print(s.index("r")) 
# print(s.index("k")) 

#  end with and start with 
print(s.endswith("my"))
print(s.startswith("nd"))


# format ------------------------------------------
s1 = "indian {} and {} airforce"
print(s1.format("army","indian"))


s1 = "indian {1} and {0} airforce" # we can change the place 
print(s1.format("army","indian"))


# split *******************
sp = s.split()
print(sp)


# join
print("-".join(sp))

# replace 
print(s.replace("Army","navy"))


# Strip -- nothing but trim iin str
s2 = "    raj patel. "
print(s2)
print(s2.strip())

