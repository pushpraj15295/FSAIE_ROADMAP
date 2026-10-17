# atm machine 

# diffrene between function and method with example
# function is a block of code that is designed to perform a specific task
# example:  len(x) or print(x)

# method is a function that is associated with an object
# example: "hello".upper() or  x.append(1)


class ATM:

    def __init__(self):      #init is a constructor that is used to initialize the object [magic method]
        self.pin = 1234     # self 
        self.balance = 0
        self.menu()

    def menu(self):
        user_input = input("""
        Hello! Welcome to the ATM!
        [1] Check Balance
        [2] Deposit
        [3] Withdraw
        [4] Change PIN
        [5] Exit
        """)
        if user_input == "1":
            self.check_balance()
        elif user_input == "2":
            amount = int(input("Enter the amount to deposit: "))
            self.deposit(amount)
        elif user_input == "3":
            amount = int(input("Enter the amount to withdraw: "))
            self.withdraw(amount)
        elif user_input == "4":
            new_pin = int(input("Enter the new PIN: "))
            self.change_pin(new_pin)
        elif user_input == "5":
            exit()
        else:
            print("Invalid input")
            self.menu()

    def check_balance(self):
        print(f"Your balance is {self.balance}")
        self.menu()

    def deposit(self, amount):
        self.balance += amount
        print(f"Your balance is {self.balance}")
        self.menu()

    def withdraw(self, amount):
        self.balance -= amount
        print(f"Your balance is {self.balance}")
        self.menu()

    def change_pin(self, new_pin):
        self.pin = new_pin
        print("PIN changed successfully")
        self.menu()

    def exit(self):
        exit()  



Sbi_atm = ATM()

# or we can create multiple objects of the same class
kotak_atm = ATM()


