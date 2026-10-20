# two types of relationships
# 1.Aggregate relationship (has-a relationship)
# 2.Inheritance relationship (is-a relationship)


# example:
# vehicle is-a object
# car is-a vehicle
# bike is-a vehicle

# vehicle has-a engine
# vehicle has-a wheels



# example: 1.Aggregate relationship (has-a relationship) ----------------------

# customer is-a object
# customer has-a address

class Customer:
    def __init__(self, name, gender, address):
        self.name = name
        self.gender = gender
        self.address = address

    def edit_profile(self, new_name=None, new_gender=None,new_city=None, new_postal_code=None, new_state=None):
        if new_name is not None:
            self.name = new_name
        if new_gender is not None:
            self.gender = new_gender
        if new_city is not None:
            self.address.change_address(new_city, new_postal_code, new_state)
        self.gender = new_gender
        self.address.change_address(new_city, new_postal_code, new_state)

class Address:
    def __init__(self,city, postal_code, state):
        self.city = city
        self.postal_code = postal_code
        self.state = state
    
    def change_address(self, city, postal_code, state):
        self.city = city
        self.postal_code = postal_code
        self.state = state


add = Address("New York", "10001", "NY")
customer = Customer("John", "Male",add)
print(customer.name)
print(customer.gender)
print(customer.address.city)
print(customer.address.postal_code)
print(customer.address.state)


customer.edit_profile("Jane", "Female", "Los Angeles", "90001", "CA")
print(customer.name)
print(customer.gender)
print(customer.address.city)
print(customer.address.postal_code)
print(customer.address.state)

# this is a example of aggregate relationship (has-a relationship)
# because customer has-a address and address is-a object






# example: 2.Inheritance relationship (is-a relationship) -----------------------------------
# why we use inheritance relationship? because we want to reuse the code and we want to avoid code duplication.
# we can inherit the properties and methods of the parent class to the child class. 
# we can use the super() function to inherit the properties and methods of the parent class. if we have method overriding, then the super() function is used to call the parent class method.
# private properties and methods are not inherited by the child class.
# methord overriding is possible in inheritance relationship. first the child class method is called, if it is not found, then the parent class method is called.
# but if child has countructor [__init__], then the parent class constructor is not called automatically. we have to call it manually.

class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
        self.__private_property = "This is a private property"

    def login(self):
        return "Login successful"

class Student(User): # Student is-a User
    def __init__(self, name, email, password, student_id):
        super().__init__(name, email, password)
        self.student_id = student_id

    def enroll(self):
        return "Enrolled successfully"

    def login(self): # this is a method overriding
        return "Student Login successful"

class Teacher(User):
    def __init__(self, name, email, password, teacher_id):
        super().__init__(name, email, password)
        self.teacher_id = teacher_id
        self.__private_property = "This is a private property"
    def teach(self):
        return "Teaching successfully"


stud1 = Student("John", "john@example.com", "password123", "123456")
print(stud1.name)
print(stud1.email)
print(stud1.password)
print(stud1.student_id)

teacher = Teacher("Jane", "jane@example.com", "password456", "789012")
print(teacher.name)
print(teacher.email)
print(teacher.password)
print(teacher.teacher_id)
print(teacher.teach())

# this is a example of inheritance relationship (is-a relationship)
# because student is-a User and teacher is-a User


# example:2. Inheritance relationship (is-a relationship) -----------------------------------

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    def drive(self):
        return "Driving the car"
    
class SportsCar(Car):
    def __init__(self, brand, model, year, speed):
        super().drive()
        self.speed = speed

    def accelerate(self):
        return "Accelerating the sports car"
        
    def brake(self):
        return "Braking the sports car"

car = Car("Toyota", "Corolla", "2020")
print(car.drive())
sports_car = SportsCar("Ferrari", "488", "2021", "300")
print(sports_car.drive())
print(sports_car.accelerate())
print(sports_car.brake())





