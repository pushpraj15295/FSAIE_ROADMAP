# Oops concept in python ------------------------------------------------

# what is object ? that need understand first before understanding oops
# ans: object is instance of class

# what is class ? that need understand first before understanding oops
# ans: class is blueprint of object

# what is inheritance ? that need understand first before understanding oops
# ans: inheritance is a mechanism that allows a class to inherit properties and methods from another class

# what is polymorphism ? that need understand first before understanding oops
# ans: polymorphism is a mechanism that allows a class to take on multiple forms

# what is encapsulation ? that need understand first before understanding oops  
# ans: encapsulation is a mechanism that allows a class to encapsulate its properties and methods

# what is abstraction ? that need understand first before understanding oops
# ans: abstraction is a mechanism that allows a class to abstract its properties and methods

# what is inheritance ? that need understand first before understanding oops
# ans: inheritance is a mechanism that allows a class to inherit properties and methods from another class

# what is polymorphism ? that need understand first before understanding oops
# ans: polymorphism is a mechanism that allows a class to take on multiple forms

# what is oops ? that need understand first before understanding oops
# ans: oops is a programming paradigm that allows a class to encapsulate its properties and methods


# class besic structure ------------------------------------------------

class Dog:
    name = "Buddy"
    age = 3
    breed = "Labrador"
    color = "Brown"
    gender = "Male"
    owner = "John"
    owner_age = 30
    owner_gender = "Male"
    owner_email = "john@example.com"
    owner_phone = "1234567890"
    def bark(self):
        print(f"{self.name} is barking")

dog1 = Dog()
print(dog1.name)
print(dog1.bark())




