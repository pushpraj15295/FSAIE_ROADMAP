# Operators in Python

# Arithmetic Operators  ==> [ +, -, *, /, //, %, ** ]
a = 10
b = 5
print("Addition: ", a + b)  # Addition
print("Subtraction: ", a - b)  # Subtraction
print("Multiplication: ", a * b)  # Multiplication
print("Division: ", a / b)  # Division
print("Floor Division: ", a // b)  # Floor Division
print("Modulus: ", a % b)  # Modulus
print("Exponentiation: ", a ** b)  # Exponentiation (a to the power of b)

# -----------------------------------------------------------------------

# Comparison Operators  ==>  [ ==, !=, >, <, >=, <= ]
x = 10
y = 20
print("Equal: ", x == y)  # Equal
print("Not Equal: ", x != y)  # Not Equal
print("Greater Than: ", x > y)  # Greater Than
print("Less Than: ", x < y)  # Less Than
print("Greater Than or Equal To: ", x >= y)  # Greater Than or Equal To
print("Less Than or Equal To: ", x <= y)  # Less Than or Equal To   


# -----------------------------------------------------------------------

# Logical Operators  ==>  [ and, or, not ]
p = True
q = False
print("Logical AND: ", p and q)  # Logical AND
print("Logical OR: ", p or q)  # Logical OR
print("Logical NOT: ", not p)  # Logical NOT    

#  ------------------------------------------------------------------------


# Assignment Operators  ==>  [ =, +=, -=, *=, /=, //=, %=, **= ]
m = 10
m += 5  # m = m + 5
print("Assignment Operator (+=): ", m)

#  ---------------------------------------------------------------------

# Bitwise Operators  ==>  [ &, |, ^, ~, <<, >> ]
a = 10  # 1010 in binary
b = 4   # 0100 in binary
print("Bitwise AND: ", a & b)  # Bitwise AND
print("Bitwise OR: ", a | b)  # Bitwise OR
print("Bitwise XOR: ", a ^ b)  # Bitwise XOR
print("Bitwise NOT: ", ~a)  # Bitwise NOT
print("Bitwise Left Shift: ", a << 1)  # Bitwise Left Shift
print("Bitwise Right Shift: ", a >> 1)  # Bitwise Right Shift   


# ------------------------------------------------------------------------


# Membership Operators  ==>  [ in, not in ]
list1 = [1, 2, 3, 4, 5]
print("Membership Operator (in): ", 3 in list1)  # Membership Operator (in)
print("Membership Operator (not in): ", 6 not in list1)  # Membership Operator (not in)


str  = "Hello, World!"
print("Membership Operator (in): ", "H" in str) 


# -----------------------------------------------------------------------

# Identity Operators for checking identity ==>  [ is, is not ]
a = 10
b = 10
print("Identity Operator (is): ", a is b)  # Identity Operator (is)
print("Identity Operator (is not): ", a is not b)  # Identity Operator (is not) 

# is operator checks whether two variables point to the same object in memory.


# ------------------------------------------------------------------------








