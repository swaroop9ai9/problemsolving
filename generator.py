# Python generators are the functions that return the traversal object and used to create iterators.
# It traverses the entire items at once
# The generato can also be an expression in which syntac is similar to list comprehension
# There is a lot of complexity in creating iteration in python, we need to implement __iter__() and __next__() method to keep track of internal states
# Generator plays an essential role in simplifying this process.
# If no value it raises "StopIteration" exception

# Syntax to create a generator function
# Similar to normal function, but uses 'yeild' keyword instead of return
import time
def simple_even():
    for i in range(10):
        print("gen_func")
        time.sleep(2)
        if(i%2==0):
            yield i

# Successive function call using for loop, this returns the even number list
for i in simple_even():
    print("loop")
    time.sleep(2)
    print(i)

# The yeild keyword, is responsible for controlling the flow of the generator function.
# It pauses the function execution by saving all states and yielded to the caller,
# Later resumes execution, when a successive function is called.
# But, a return statement returns a value and terminates the whole function, (only one return can be used).
time.sleep(3)
print("Multiple Yield's")
def multiple_yield():
    str1="First String"
    yield str1

    str2 = "second string"
    yield str2

    str3="Third String"
    yield str3
obj = multiple_yield()
print(next(obj))
time.sleep(2)
print(next(obj))
time.sleep(2)
print(next(obj))

# In Generator functions are called, the normal function is paused immediately and control transferred to the caller
# Local variable and their states are remembered between succesive calls
# StopIteration exception is raised automatically when the function terminates

# Generator Expression: Could be created easily without useer-defined function.
# Similar to Lambda function, which created an anonymous generator function
# Very similar to list comprehension, but square braces are replaced with ()
print("Generator Expression")
lis = [1,2,3,4,5,78]
a = (x**3 for x in lis)
print(a)
print(next(a))
print(next(a))


# Advantages of Generators
#   1) Easy to implement
#   2) Memory Efficient
#   3) Pipelining with Generators
#   4) Generate Infinite Sequence

