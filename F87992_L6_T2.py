from sys import argv
def power(x, y):
    if y == 0:
        return 1

    if y >= 1:
        return x * power(x, y - 1)
n = int(argv[1])
p = int(argv[2])
res = power(n , p)
print res

