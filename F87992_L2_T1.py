# F87992_L2_T1.py
import sys 

argument = sys.argv[1:]

if sorted(argument[0]) >= '9' :
    argumentint = [int(i) for i in argument]
    if sorted(argumentint) == argumentint : print ("sorted")
    else : print("unsorted")
else :
    if sorted(argument) == argument : print ("sorted")
    else : print("unsorted")
