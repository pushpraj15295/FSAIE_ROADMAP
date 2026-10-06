# break ,continue and pass statements in python

# break statement in python [stops the loop]-----------------------------
for i in range(1, 11):
    if i == 4:
        break
    print("break",i)    


# continue statement in python [skips the current iteration] -----------------------------
for i in range(1, 11):
    if i == 5:
        continue
    print("continue",i)    


# pass statement in python [does nothing]-----------------------------
for i in range(1, 11):
    if i == 5:
        pass
    print("pass",i)    