# if and else statements in Python

# with Simple login flow -----------------------------

username = input("Enter your username: ")
password = input("Enter your password: ")

if username == "admin" and password == "admin123":
    print("Login successful!")
elif username == "admin" and password != "admin123":
    print("Login failed! Please check your password.")
    password = input("Enter your password again: ")
    if password == "admin123":
        print("Login successful!")
    else:
        print("Login failed! please try again later.")
else:
    print("Login failed! Please check your username and password.")


