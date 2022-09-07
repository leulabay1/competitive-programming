#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    # Write your code here
    n = len(a)
    swaps = 0
    itration = 0
    swapped = True
    while(swapped):
        swapped = False
        for j in range(0, n-itration-1):
 
            if a[j] > a[j + 1]:
                swapped = True
                a[j], a[j + 1] = a[j + 1], a[j]
                swaps += 1
        itration += 1       
        
    print("Array is sorted in " + str(swaps) +" swaps.")
    print("First Element: " + str(a[0]))
    print("Last Element: " + str(a[n-1]))
    return
    
if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
