"""
Created on Fri Feb 25 18:27:50 2022

@author: thomastesselaar

Power-Hungry
"""
import numpy as np
from itertools import combinations
import time
import math

#More efficient (O(n) efficincy)
def greatestProduct(xs):
    
    if len(xs) == 1:
        return str(xs[0])
    
    negatives = [x for x in xs if x < 0]
    positives = [x for x in xs if x > 0]
    
    if len(positives) == 0 and xs.count(0) and len(negatives) == 1:
        return '0'

    if len(negatives) % 2 != 0:
        negatives.remove(max(negatives))

    if positives or negatives:
        product = 1
        for i in positives + negatives:
            product = int(product * i)

        return str(product)

    return '0'

#This was found to be the most efficient 
def maxProductSubset(xs): 
    n = len(xs)
    
    if n == 1: 
        return str(xs[0])
  
    max_neg = -1001
    count_neg = 0
    count_zero = 0
    prod = 1
    for i in xs: 

        if i == 0:  
            count_zero += 1
            continue
 
        if i < 0:  
            count_neg += 1
            max_neg = max(max_neg, i) 

        prod = prod * i 

 
    if count_zero == n:  
        return '0'

  
    if count_neg % 2:  

        if (count_neg == 1 and count_zero > 0 and 
            count_zero + count_neg == n): 
            return '0'
 
        prod = int(prod / max_neg)

    return str(prod)

#This has a meh efficiency, significantly less than above two
def answer(xs):

    if len(xs) == 1: 
        return str(xs[0])
    max_product = 0
    
    def max_single_sign_prod(arr):
        if arr[0] == 0:
            return 0  # all zero
        if arr[0] > 0:
            return np.prod(arr) # all positive

        # all negative
        p = np.prod(arr)
        if len(arr) > 1 and len(arr) % 2:
            return p // max(arr)
        else:
            return p

    # Generate all positive, all negative and all zero sublists of arr
    pos = [i for i in xs if i > 0]
    neg = [i for i in xs if i < 0]
    zeros = [i for i in xs if i == 0]

    # Find non-empty sublists
    b = [x for x in [pos, neg, zeros] if len(x) > 0]

    products = list(map(max_single_sign_prod, b))

    for i in range(len(b)+1):
        for c in combinations(products, i):
            max_product = int(max(max_product, math.prod(c)))

    return str(max_product)

#Checking all sub-arrays -- very inefficient especially with large arrays
def inefficientSolution(xs):
    
    result = 0

    for i in range(1, len(xs)+1):
        for subset in combinations(xs, i):
            result = max(result, np.prod(subset))
                
    return str(result) 


def CompareEfficiency(n):
    start = time.time()
    greatestProduct(n)
    end = time.time()
    print(end-start)
    
    start = time.time()
    maxProductSubset(n)
    end = time.time()
    print(end-start)
    
#    start = time.time()
#    answer(n)
#    end = time.time()
#    print(end-start)
       
    start = time.time()
    inefficientSolution(n)
    end = time.time()
    print(end-start)


#CompareEfficiency([1, 1, 0, -2, -3])

CompareEfficiency([1, 2, 3, 4, 5, 6, 7, 0, 0, 0, -2, -3, -4, -5, -1, -2, 3, 4, 1234, 43,654, 45, 765, 8,5  ,867, 679, 679, 8576, 745, 346, 4,63 ,346 ,543 ,5234 ,345 ,346 ])
