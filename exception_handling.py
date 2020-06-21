try:  
    a = int(input("Enter a:"))  
    b = int(input("Enter b:"))  
    c = a/b;  
    print("a/b = %d"%c)  
except Exception:  
    print("can't divide by zero")  
else:  
    print("Hi I am else block")   


try:  
    #this will throw an exception if the file doesn't exist.   
    fileptr = open("file.txt","r")  
except IOError:  
    print("File not found")  
else:  
    print("The file opened successfully")  
    fileptr.close()  

try:  
    age = int(input("Enter the age?"))  
    if age<18:  
        raise ValueError;  
    else:  
        print("the age is valid")  
except ValueError:  
    print("The age is not valid")


class ErrorInCode(Exception):    
    def __init__(self, data):    
        self.data = data    
    def __str__(self):    
        return repr(self.data)    
    
try:    
    raise ErrorInCode(2000)    
except ErrorInCode as ae:    
    print("Received error:", ae.data)    
