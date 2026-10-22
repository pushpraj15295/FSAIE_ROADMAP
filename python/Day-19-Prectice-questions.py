###  1st Problem  ---->   User will input (3ages).Find the oldest one ?

age = 0

age1 = int(input("give your 1st age: "))
if age < age1:
 age = age1

age2 = int(input("give your 2nd age: "))
if age < age2:
 age = age2

age3 = int(input("give your 3rd age: "))
if age < age3:
 age = age3

print("This age is oldest:", age)


# ------------------------------------------------------------------------------------------------------------------------------------------


###  2nd Problem  --->   Write a program that will convert celsius value to fahrenheit  ?
 

temp = input("Please enter the celsius value")
#f = ( c * 1.8 ) + 32

temp = int(temp) * 1.8
fahrenheit = temp + 32

print("value in fahrenheit is -", fahrenheit)


# ------------------------------------------------------------------------------------------------------------------------------------------

###  3rd Problem  --->   User will input (2numbers).Write a program to swap the numbers  ? 


num1 = input("inter your first number")
num2 = input("inter your second number")

temp = num1
num1 = num2
num2 = temp

print(f"{temp} your swap is {num1}")
print(f"{num1} your swap is {num2}")

# ------------------------------------------------------------------------------------------------------------------------------------------

###   4th Problem    ---->  Write a program that will give you the sum of 3 digits ?


n1 = int(input("Enter 1st number"))
n2 = int(input("Enter 2nd number"))
n3 = int(input("Enter 3rd number"))


def sum(a=0,b=0,c=0):
 return n1+n2+n3

result = sum(n1,n2,n3)
print("sum of given number is",result)


# ------------------------------------------------------------------------------------------------------------------------------------------

###  5th Problem   ---->   Write a program that will reverse a four digit number.Also it checks whether the reverse is true ?


num = input("enter your 4 digit number")

reverse_num = num[::-1]

print(reverse_num)
print(reverse_num[::-1] == num)  


# ------------------------------------------------------------------------------------------------------------------------------------------
#  6th  Problem  ---->   Write a program that will tell whether the number entered by the user is odd or even ?


num = int(input("enter your number"))

if num % 2 == 0:
 print("your number is Even")
else: print("your number is Odd")


# ------------------------------------------------------------------------------------------------------------------------------------------

### 7th Problem  ---->  Write a program that will tell whether the given year is a leap year or not. ? 

year = int(input("enter your year"))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
 print("Leap Year")
else: print("Normal year")


# ------------------------------------------------------------------------------------------------------------------------------------------

### 8th Problem    ----->   Write a program to find the euclidean distance between two coordinates. ?  (2,3) (4,5) 

import math

x1 = int(input("enter x1"))
y1 = int(input("enter y1"))


x2 = int(input("enter x2"))
y2 = int(input("enter y2"))


uclidean_dist = math.sqrt((x2-x1)**2 + (y2-y1)**2)
print("uclidean distance between your coordinates is", uclidean_dist)

# ------------------------------------------------------------------------------------------------------------------------------------------

###  9th Problem   ---->  Write a program that take a user inputr of three angles and will find out whether it can form a triangle or not ? 

angle1 = int(input("enter you first engle"))
angle2 = int(input("enter you second engle"))
angle3 = int(input("enter you third engle"))

if angle3 + angle2 + angle1 == 180:
 print("triangle is posibale")
else : print("triangle is not posibale")


# ------------------------------------------------------------------------------------------------------------------------------------------

### 10th Problem  ---->  Write a program that will take user input of cost price and selling price and determines whether its a loss or a profit  ?

cost = int(input("enter your cost price"))
sell = int(input("enter your selling price"))

if cost < sell:
 print("You are in profit of" ,sell - cost)
else: print("You are in Loss of" ,cost - sell )


# ------------------------------------------------------------------------------------------------------------------------------------------
### 11th Problem ---->   Write a program to find the simple interest when the value of principle,rate of interest and time period is given.


principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate of interest: "))
time = float(input("Enter time in years: "))

simple_interest = (principal * rate * time) / 100

print("Simple Interest:", simple_interest)


# ------------------------------------------------------------------------------------------------------------------------------------------

### 12th Problem    --->  Write a program to find the volume of the cylinder. Also find the cost when ,when the cost of 1litre milk is 40Rs.

import math

radius = float(input("Enter radius in cm: "))
height = float(input("Enter height in cm: "))

volume = math.pi * radius ** 2 * height

litres = volume / 1000
cost = litres * 40

print("Volume of cylinder:", volume, "cm³")
print("Milk capacity:", litres, "litres")
print("Cost of milk: Rs.", cost)


# ------------------------------------------------------------------------------------------------------------------------------------------