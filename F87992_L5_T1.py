import sys

def F(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return F(n-1)+F(n-2)

bot = int(sys.argv[1])
top = int(sys.argv[2])
fiblist = []

for i in range(top):
    fiblist.append(F(i))
    i+=1
print fiblist[bot:]
