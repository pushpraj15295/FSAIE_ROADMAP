# Global and Local Variable


# example - 1 -------------------------------
def fun(y):
    x = 1 
    x += 1
    print("x",x)

x = 5
fun(x)
print("outer",x)


# example-2 ---------------------------------
def fun1(y):
    y = 6 
    # if i comment this line like y = 6 then
    # it will take global 3 and make it 4 but if i don't comment it will take 6 and make it 7
    y+=1
    print("y",y)

y = 3
fun1(y)
print("out1",y)


# example-3 ---------------------------------
def fun3():
    a += 1 
# you can't change the global variable inside a function
# you can only change the local variable inside a function
# so if you want to change the global variable inside a function you have to use the global keyword
# global keyword is used to declare a variable as global
a = 5
# fun3()
print("a",a)

# example-4 ---------------------------------
def fun4():
    global a
    a += 1
    print("a",a)

a = 5
fun4()
print("a",a)
# output will be update because global variable is changed inside the function

# example-5 ---------------------------------
# nested function
def fun5():
    def fun6():
        print("fun6")
    fun6()
    print("fun5")

fun5()
# output will be fun6 fun5 because nested function is called inside the function    