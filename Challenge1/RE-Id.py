"""
Created on Mon Feb 14 16:42:14 2022

@author: thomastesselaar

RE-Id
"""
import sympy as sp
import time

#using sieve of eratosthenes algorithm, this is the most efficient algorithm
def SieveOfEratosthenes(n):
     
    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):
         
        # If prime[p] is not changed, then it is a prime
        if (prime[p] == True):
             
            # Update all multiples of p
            for i in range(p ** 2, n + 1, p):
                prime[i] = False
        p += 1
    prime[0]= False
    prime[1]= False
    
    primes = ''
    
    for p in range(n + 1):
        if prime[p]:
            primes = primes + str(p)
            
    return primes
            
    
#Using sympy to check primes    
def StringOfPrimes(n):
    
    primes = ''
    
    for i in range(n + 1):

        if sp.isprime(i):
            
            primes = primes + str(i)
             
    return primes


def InefficientSolution(n): 
    primes = ''
    notprime_list = []
    for k in range(2, 20261):
        if k not in notprime_list:
            primes = primes + str(k)
            for j in range(k*k, 20262, k):
                notprime_list.append(j)
    return primes


#Compares the efficiency of two algorithms by returning their runtimes
def CompareEfficiency(n):
    start = time.time()
    StringOfPrimes(n)
    end = time.time()
    print(end-start)
    
    start = time.time()
    SieveOfEratosthenes(n)
    end = time.time()
    print(end-start)
    
    start = time.time()
    InefficientSolution(n)
    end = time.time()
    print(end-start)
    

def GetID(n, primes):
    return primes[n:n + 5]

#20221 is the minimum input to get a string length of 10000. Note that a length of 10005 is needed
CompareEfficiency(1000)
