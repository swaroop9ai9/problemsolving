# Writing python output to the files
# check_call() method of module subprocess is used to execute a python script and write the output of a script to a file
temperatures=[10,-20,-289,100]
def c_to_f(c):
    if c<-273.15:
        return "That the temperature doesn't make sense!"
    else:
        f=(c*9/5)+32
        return f
for t in temperatures:
    print(c_to_f(t))
