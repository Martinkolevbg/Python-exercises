#F87992_L1_T2
import sys

args = sys.argv[1:]

anagram1 = args[0]+args[1]
anagram2 = args[2]+args[3]

if sorted(anagram1)==sorted(anagram2):
    print("true")
else:
    print("False")

