# Types of Inheritance 5 Types

# 1. Single Inheritance [Parent -> Child]---------------------------->
# 2. Multiple Inheritance [Parent1, Parent2 -> Child]---------------------------->
# 3. Multi-level Inheritance [GrandParent -> Parent -> Child]---------------------------->
# 4. Hierarchical Inheritance [Parent -> Child1, Child2]---------------------------->
# 5. Hybrid Inheritance [Any combination of the above]---------------------------->



# 1. Single Inheritance [Parent -> Child]---------------------------->
# A class that inherits from another class. It is a one-to-one relationship.
class Parent:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Child(Parent):
    def __init__(self, name, age, gender):
        super().__init__(name, age)
        self.gender = gender

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}")

child1 = Child("John", 20, "Male")
child1.display() # Name: John, Age: 20, Gender: Male


# 2. Multiple Inheritance [Parent1, Parent2 -> Child]---------------------------->
# A class that inherits from multiple classes. It is a one-to-many relationship.
class Parent1:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Parent2:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age  
        self.gender = gender

class Child(Parent1, Parent2): # first Parent1 then Parent2 [MRO]
    def __init__(self, name, age, gender):
        Parent1.__init__(self, name, age)
        Parent2.__init__(self, name, age, gender)

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}")

child2 = Child("John", 20, "Male")
child2.display() # Name: John, Age: 20, Gender: Male


# 3. Multi-level Inheritance [GrandParent -> Parent -> Child]---------------------------->
# A class that inherits from a class that inherits from another class. It is a one-to-one relationship.
class GrandParent:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Parent(GrandParent):
    def __init__(self, name, age, gender):
        super().__init__(name, age)
        self.gender = gender

class Child(Parent):
    def __init__(self, name, age, gender, address):
        super().__init__(name, age, gender)
        self.address = address

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}, Address: {self.address}")

child3 = Child("John", 20, "Male", "123 Main St")
child3.display() # Name: John, Age: 20, Gender: Male, Address: 123 Main St  



# 4. Hierarchical Inheritance [Parent -> Child1, Child2]---------------------------->
# A class that inherits from a class that inherits from another class. It is a one-to-many relationship.
class Parent:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Child1(Parent):
    def __init__(self, name, age, gender):  
        super().__init__(name, age)
        self.gender = gender

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}")

class Child2(Parent):
    def __init__(self, name, age, gender):
        super().__init__(name, age)
        self.gender = gender

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}")

child4 = Child1("John", 20, "Male")
child4.display() # Name: John, Age: 20, Gender: Male

child5 = Child2("John", 20, "Male")
child5.display() # Name: John, Age: 20, Gender: Male    


# 5. Hybrid Inheritance [Any combination of the above]---------------------------->
# A class that inherits from a class that inherits from another class. It is a one-to-many relationship.
class GrandParent:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Parent(GrandParent):
    def __init__(self, name, age, gender):
        GrandParent.__init__(self, name, age) 
        self.gender = gender

class Child3(Parent):
    def __init__(self, name, age, gender, address):
        Parent.__init__(self, name, age, gender)
        self.address = address

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}, Address: {self.address}")

child6 = Child3("John", 20, "Male", "123 Main St")
child6.display() # Name: John, Age: 20, Gender: Male, Address: 123 Main St    
