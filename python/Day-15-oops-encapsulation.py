# Nothing in Python is truly Private
# __ is used to make a variable private
# to access private variable we use _class_name__variable_name


# encapsulation is the process of hiding the internal details of a class and exposing only the necessary interfaces
# using getters and setters we can access and modify the private variables of a class

class Atm_Card:
    def __init__(self):
        self.__pin = 1234
        self.__balance = 10000

    def get_pin(self):
        return self.__pin

    def set_pin(self,new_pin):
        if type(new_pin) != int:
            print("Not a valid pin, please enter a valid pin")
        else:
            self.__pin = new_pin
            print("Pin changed successfully")
    
    def get_balance(self,pin):
        if pin == self.__pin:
            return self.__balance
        else:
            print("Please enter a valid pin")
    def update_balance(self,pin,amount):
        if pin == self.__pin:
            self.__balance += amount
            print("Balance updated successfully")
        else:
            print("Please enter a valid pin and amount")



my_card = Atm_Card()
print(my_card.get_pin())
my_card.set_pin("hjsdfhks") #not a valid pin, please enter a valid pin


my_card.set_pin(6789) #Pin changed successfully
print(my_card.get_pin())

print("your Account balance is - ",my_card.get_balance(6789))

print("update", my_card.update_balance(6789,4440))

print("your New Account balance is - ",my_card.get_balance(6789))

#  this complete process is called encapsulation