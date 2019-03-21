from sys import argv

d={1:'a', 2:'b', 3:'c', 4:'a', 5:'d', 6:'e', 7:'a',8:'b'}

result = []
value = argv[1]

for key in d:
    if d[key] == value:
        result.append(key)

print(result)