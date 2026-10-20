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