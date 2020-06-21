# to write a python output to another file we make use of check_call() method from subprocess module
import subprocess

with open("output.txt",'wb') as f:
    subprocess.check_call(['python','celsuis_to_f.py'], stdout=f)
print("The above file has been executed")
