"""
Given two non-negative integers n1 and n2, where n1<n2. 
The task is to find the total number of integers in the range [n1, n2](both inclusive) which have no repeated digits.

"""

import sys

def noRepeatedDigits(n1,n2):

    count = 0

    for num in range(n1,n2+1):
        visited = [False]*10
        while(num>0):
            if visited[num%10] == True:
                break
            visited[num%10] = True
            num = num//10
        if num==0:
            count = count+1
    return count


if __name__ == '__main__':

    n1,n2 = [int(x) for x in sys.stdin.readlines()]
    print(f"The number of non repeated digit integers are: {noRepeatedDigits(n1,n2)}")