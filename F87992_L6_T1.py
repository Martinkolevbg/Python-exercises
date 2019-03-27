import sys

def F(n):
    if n == 1: 
        fiblist[0] = 0
        return fiblist[0]
    elif n == 2:
        fiblist[1] = 1
        fiblist[0] = 0
        return fiblist[1]
    else: 
        if fiblist[n-1] != -1:
            return fiblist[n-1]
        else: 
            fiblist[n-1] = F(n-1)+F(n-2)
            return fiblist[n-1]

bot = int(sys.argv[1])
top = int(sys.argv[2])
fiblist = [-1]*top
F(top)
print fiblist[bot-1:]
