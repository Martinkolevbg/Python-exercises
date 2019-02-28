# F87992_L2_T4 Martin Kolev
import sys

niz = sys.argv[1:]

nizInt = [int(i) for i in niz]
nizIntSorted = sorted(nizInt)
setList = []

for x in range(0,len(nizIntSorted)):
    if nizIntSorted[x] != nizIntSorted[x-1]:
        setList.append(nizIntSorted[x])
print(setList)