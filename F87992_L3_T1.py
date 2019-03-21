import sys

a = sys.argv[1:]

text = ''.join(a)
key = int(a[0])
result = ""
for i in range(len(text)-1):
		char = text[i]
		if (char.isupper()):
			result += chr((ord(char) + key-65) % 26 + 65)
		else:
			result += chr((ord(char) + key - 97) % 26 + 97)
print result[1:]