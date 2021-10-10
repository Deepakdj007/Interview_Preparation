"""
In this even odd problem Given a range [low, high] (both inclusive), select K numbers from the range (a number can be chosen multiple times) such that sum of those K numbers is even.

Calculate the number of all such permutations.

As this number can be large, print it modulo (1e9 +7).

"""

def evenSum(l,h,k):
    mod = 1000000007

    even_count = h//2 - (l-1)//2
    odd_count = (h+1)//2 - l//2

    even_sum = 1
    odd_sum = 0

    for i in range(0,k):
        prev_even = even_sum
        prev_odd = odd_sum

        even_sum = prev_even*even_count + prev_odd*odd_count
        odd_sum = prev_even*odd_count + prev_odd*even_count

    return even_sum%mod



if __name__ == '__main__':
    low, high = map(int,input().split())
    k = int(input())

    print(evenSum(low,high,k))