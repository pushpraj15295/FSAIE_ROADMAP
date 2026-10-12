# everything is object
def fun(x):
    return x**2

print(fun(2))
print(type(fun))





# i can assign a function to a variable
variable = fun
print(variable(3))
print(type(variable))

# or 
list = [1,2,3,4,5,variable]
# i can assign a function to a list
print(list[-1](4))
print(type(list))

# or 
tuple = (1,2,3,4,5,variable)
# i can assign a function to a tuple
print(tuple[-1](4))
print(type(tuple))


#  a function can take a function as an argument and return a function

def new_fun():
    print("new_fun")

def fun2(fun):
    print("fun2")
    return fun()

print(fun2(new_fun))


# nested function 
def fun5():
    def x(a,b):
        return a+b
    return x

print("result of fun5() is",fun5()(1,2))   # fun5() = x and x(1,2) = 3

