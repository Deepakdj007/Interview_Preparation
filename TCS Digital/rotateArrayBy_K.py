"""
Given an array Arr[ ] of N integers and a positive integer K. 
The task is to cyclically rotate the array clockwise by K.

"""


import sys

def rotate(size,arr,k):

    rotarr = [0]*size
    for i in range(0,k):
        rotarr[i] = arr[size-k+i]
    
    index = 0
    for i in range(k,size):
        rotarr[i] = arr[index]
        index = index+1
    
    return rotarr


if __name__ == '__main__':

    inputs = [int(x) for x in sys.stdin.readlines()]
    inputsize = len(inputs)
    size = inputs[0]
    arr = inputs[1:inputsize-1]
    k = inputs[inputsize-1]
    print(f"The normal array: \n{arr}")
    print(f"The rotated array: \n{rotate(size,arr,k)}")