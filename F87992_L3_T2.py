import sys

def generateKey(string, key):
    key = list(key)
    if len(string) == len(key):
        return (key)
    else:
        for i in range(len(string) -
                       len(key)):
            key.append(key[i % len(key)])
    return ("".join(key))

def cipherText(string, key):
    cipher_text = []
    for i in range(len(string)):
        x = (ord(string[i]) +
             ord(key[i])) % 26
        x += ord('A')
        cipher_text.append(chr(x))
    return ("".join(cipher_text))

if __name__ == "__main__":
    b = sys.argv[1:]

    for i in range(len(b) - 1):
        string = b[i]

    keyword = sys.argv[2:]
    key = generateKey(string, keyword)
    cipher_text = cipherText(string, key)
    print cipher_text
