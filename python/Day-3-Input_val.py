# input 

input1 = input("Enter your name: ")
print("Hello, " + input1 + "!")

# additional input example
val_1 = input("Enter a number -1 : ")
val_2 = input("Enter a number -2 : ")

# or  int_val_1 = int(input("Enter a number -1 : "))


# user input allways returns string data type. 
# beccause any data type we can convert to string data type.
type_of_val_1 = type(val_1)
print("Data type of val_1 is:" ,  type_of_val_1)

sum = int(val_1) + int(val_2)
print("Sum of " + val_1 + " and " + val_2 + " is: " + str(sum)) 



# ---------------------------------------------------------------------
#  type conversion - we can convert one data type to another data type in python.
#  type conversion is not a parmanent process. it is a temporary process. once the program is executed the data type will be converted back to original data type.
#  impicit type conversion - python automatically converts one data type to another data type if it is possible.

sum  = 10 + 20.5
print("Sum of 10 and 20.5 is: " + str(sum))

# or 

sum1 = 4.5 + 5 + 5j
print("Sum of 4.5 and 5 and 5j is: " ,sum1)


#  explicit type conversion - we can convert one data type to another data type using built-in functions like int(), float(), str(), etc.

bool_val = bool(1)
print("Data type of bool_val is: " , bool_val)

complex_val = complex(3)
print("Data type of complex_val is: " , complex_val)


list_val = list(("hellow"))
print("Data type of list_val is: " ,list_val)


int_val = int(3.5)
print("Data type of int_val is: " , int_val)  


