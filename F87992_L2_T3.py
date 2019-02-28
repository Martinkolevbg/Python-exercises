# F87992_L2_T3
import sys

niz = sys.argv[1:]

nizint = [int(i) for i in niz]
nizintsorted = sorted(nizint)

res = 0
for x in range(1,len(nizintsorted)):
    if nizintsorted[x]== nizintsorted[x-1]:
        res += 1
if res!=0:
    print("True")
else:
    print("False")