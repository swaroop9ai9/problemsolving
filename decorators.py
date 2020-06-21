# Decorators are powerful tools, these are used to modify the behavior of the function.
# Decorators provide the flexibility to wrap another function to expand the working of warrped function without permanently modifying it.
# In decorators functions are passed as argument into another dunction and then called inside the wrapper function
# Also called as meta programming

# Python treats everything as an object including classes or any variable.
# Functions are first-class objects, because they can reference to, passed to a variable and returned from other functions as well
# Example
def func1(msg):
    print(msg)
func1("hii")
func2 = func1
func2("Hiii")

# IN THE ABOVE PROGRAM 'FUNC2' REFFERED TO 'FUNC1' AND ACT AS FUNCTION. THEREFORE
#   1) THE FUNCTION CAN BE REFERENCED AND PASSED TO A VARIABLE AND RETURNED FROM OTHER FUNCTIONS AS WELL
#   2) THE FUNCTIONS CAN BE DECLARED INSIDE OTHER FUNCTION AND PASSED AS AN ARGUMENT TO ANOTHER FUNCTION

# INNER FUNCTION
print("Inner function example")
def func():
     print("We are in first function")  
     def func1():  
           print("This is first child function")  
     def func2():  
           print(" This is second child function")  
     func1()  
     func2()  
func()

# HIGHER ORDER FUNCTION , passing function as an argument
print("Higher order function example")
def add(x): 
    return x+1
def sub(x):
    return x-1
def operator(func,x):
    temp=func(x)
    return temp
print(operator(sub,10))
print(operator(add,20))

# RETURNING ANOTHER FUNCTION
print("Returning another function")
def hello():
    def hi():
        print("hello")
    return hi
new = hello() # now new is a function (first class object), where we can call new() to invoke hi() function
new()

# Decorating functions with parameters
print(" Decorator functions with parameters: ")
def divide(x,y):
    print(x/y)
def outer_div(func):
    def inner(x,y):
        if(x<y):
            x,y=y,x
        return func(x,y)
    return inner
divide1 = outer_div(divide)
divide1(2,4)

print("Syntactic Decorator")
def outer_div(func):  
    def inner(x,y):  
        if(x<y):  
           x,y = y,x
        return func(x,y)  
    return inner
# syntax of generator  
@outer_div  
def divide(x,y):  
     print(x/y)  



