import sys
str=sys.argv[1]
def isPalindrome(s):
    if len(s)<=1:
        return True
    else:
        first = s[0]
        last = s[len(s)-1]
        if first==last:
            mid=s[1:len(s)-1]
            return isPalindrome(mid)
        else:
            return False
print isPalindrome(str.lower())