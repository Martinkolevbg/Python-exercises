from sys import argv

text = argv[1]

dict = {}

for char in text:
    if char in dict:
        dict[char] += 1
    else:
        dict[char] = 1

print(dict.items())