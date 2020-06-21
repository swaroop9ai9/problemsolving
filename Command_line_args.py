#Command line arguments
# We can pass parameters along with the file name while executing the script
# Provides a module 'getopt' in which command line arguments can be passed
# Python sys module gives access to CLA using 'sys.argv'
# sys.argv[0] is always the name of the file

import sys
print(type(sys.argv))
print("The command line arguments are :")
for i in sys.argv:
    print(i)

# Using getopt
import getopt
argv = sys.argv[1:]
try:
    opts, args = getopt.getopt(argv, 'hm:d', ['help', 'my_file='])  
    print(opts)  
    print(args)  
except getopt.GetoptError:  
    # Print a message or do something useful  
    print('Something went wrong!')  
    sys.exit(2)  
