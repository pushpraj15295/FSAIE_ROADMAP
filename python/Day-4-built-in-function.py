# built in functions

# print() - print() function is used to print the output on the console. 
# it can take multiple arguments and it will print them in a single line.
print("Hello, World!")

# input() - input() function is used to take input from the user.
#  it will always return a string data type. we can convert the string data type to other data types using built-in functions like int(), float(), str(), etc.
name = input("Enter your name: ")
print("Hello, " + name + "!")

# type() - type() function is used to check the data type of a variable.
#  it will return the data type of the variable.
val = 10
print("Data type of val is: " , type(val))  


# len() - len() function is used to check the length of a string, list, tuple, set, dictionary, etc.
#  it will return the length of the variable.
str_val = "Hello, World!"
print("Length of str_val is: " , len(str_val))  


# abs() - abs() function is used to check the absolute value of a number. 
# it will return the absolute value of the variable.
num_val = -10
print("Absolute value of num_val is: " , abs(num_val))  


# round() - round() function is used to round a number to the nearest integer. 
# it will return the rounded value of the variable.
float_val = 10.5
print("Rounded value of float_val is: " , round(float_val)) 


# max() - max() function is used to check the maximum value of a list, tuple, set, etc.
#  it will return the maximum value of the variable.
list_val = [1, 2, 3, 4, 5]
print("Maximum value of list_val is: " , max(list_val))


# min() - min() function is used to check the minimum value of a list, tuple, set, etc.
#  it will return the minimum value of the variable.
list_val = [1, 2, 3, 4, 5]
print("Minimum value of list_val is: " , min(list_val)) 


# sum() - sum() function is used to check the sum of a list, tuple, set, etc. 
# it will return the sum of the variable.
list_val = [1, 2, 3, 4, 5]
print("Sum of list_val is: " , sum(list_val))


# sorted() - sorted() function is used to sort a list, tuple, set, etc.
#  it will return the sorted value of the variable.
list_val = [5, 4, 3, 2, 1]
print("Sorted value of list_val is: " , sorted(list_val))


# divmod() - divmod() function is used to check the quotient and remainder of a division operation. 
num1 = 10
num2 = 3
print("Quotient and Remainder of num1 and num2 is: " , divmod(num1, num2))   # bhag - sesh


# enumerate() - enumerate() function is used to check the index and value of a list, tuple, set, etc.
#  it will return a tuple containing the index and value of the variable.
list_val = ["a", "b", "c", "d", "e"]

for index, value in enumerate(list_val):
    print("Index: " , index , "Value: " , value)    


# zip() - zip() function is used to combine two or more lists, tuples, sets, etc. 
# it will return a zip object containing the combined values of the variables.
list1 = [1, 2, 3, 4, 5]
list2 = ["a", "b", "c", "d", "e"]
zipped = zip(list1, list2)
print("Zipped value of list1 and list2 is: " , list(zipped))


# map() - map() function is used to apply a function to all the items in a list, tuple, set, etc. 
# it will return a map object containing the applied values of the variable.
list_val = [1, 2, 3, 4, 5]


def square(x):
    return x * x
mapped = map(square, list_val)
print("Mapped value of list_val is: " , list(mapped))   


# filter() - filter() function is used to filter the items in a list, tuple, set, etc. 
# it will return a filter object containing the filtered values of the variable.
list_val = [1, 2, 3, 4, 5]
def is_even(x):
    return x % 2 == 0
filtered = filter(is_even, list_val)
print("Filtered value of list_val is: " , list(filtered))   



# reduce() - reduce() function is used to apply a function to all the items in a list, tuple, set, etc.
#  it will return a single value containing the reduced value of the variable.
from functools import reduce
list_val = [1, 2, 3, 4, 5]
def add(x, y):
    return x + y
reduced = reduce(add, list_val)
print("Reduced value of list_val is: " , reduced)   


# any() - any() function is used to check if any item in a list, tuple, set, etc. is True. 
# it will return True if any item is True, otherwise it will return False.
list_val = [0, 0, 0, 1, 0]
print("Any value of list_val is: " , any(list_val)) 


# all() - all() function is used to check if all items in a list, tuple, set, etc. are True. 
# it will return True if all items are True, otherwise it will return False.
list_val = [1, 1, 1, 1, 1]
print("All value of list_val is: " , all(list_val)) 



# eval() - eval() function is used to evaluate a string as a Python expression. 
# it will return the evaluated value of the variable.
expression = "2 + 3 * 4"
print("Evaluated value of expression is: " , eval(expression))


# exec() - exec() function is used to execute a string as a Python statement. 
# it will return the executed value of the variable.
statement = "x = 5\ny = 10\nz = x + y"
exec(statement)
print("Executed value of statement is: " , z)   



# help() - help() function is used to get the documentation of a function, class, module, etc. 
# it will return the documentation of the variable.
print("Help value of print() function is: " , help(print))



# dir() - dir() function is used to get the list of attributes and methods of a function, class, module, etc.
#  it will return the list of attributes and methods of the variable.
print("Dir value of print() function is: " , dir(print))


# id() - id() function is used to get the unique identifier of a function, class, module, etc. 
# it will return the unique identifier of the variable.
print("Id value of print() function is: " , id(print))  


# isinstance() - isinstance() function is used to check if a variable is an instance of a class or not. 
# it will return True if the variable is an instance of the class, otherwise it will return False.
x = 10
print("Is x an instance of int? : " , isinstance(x, int))   
