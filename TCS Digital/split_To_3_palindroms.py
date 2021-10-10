"""
In this 3 Palindrome question, Given an input string word, split the string into exactly 3 palindromic substrings. 
Working from left to right, choose the smallest split for the first substring that still allows the remaining word to be split into 2 palindromes.

Similarly, choose the smallest second palindromic substring that leaves a third palindromic substring.

If there is no way to split the word into exactly three palindromic substrings, print “Impossible” (without quotes). 
Every character of the string needs to be consumed.

Cases not allowed –

After finding 3 palindromes using above instructions, if any character of the original string remains unconsumed.
No character may be shared in forming 3 palindromes.

"""
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