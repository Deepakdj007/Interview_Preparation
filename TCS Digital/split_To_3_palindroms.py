import sys

def isPalindrome(s):
    if len(s)==1:
        return True
    return s == s[::-1]

def findPalindrome(instring):
    l = len(instring)
    for i in range(1,l-1):
        s1 = instring[:i]
        if isPalindrome(s1):
            for j in range(1,l-1):
                s2 = instring[i:i+j]
                s3 = instring[i+j:]
                if isPalindrome(s2) and isPalindrome(s3):
                    print(s1)
                    print(s2)
                    print(s3)
                    sys.exit()
    print("Impossible")

if __name__ == '__main__':
    input_string = input()
    findPalindrome(input_string)