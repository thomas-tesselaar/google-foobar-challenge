"""
Created on Fri Feb 25 18:27:50 2022

@author: thomastesselaar

En-Route-Salute
"""
import time

#Using nested for loops, this is a less efficient solution
def inefficientSolution(s):
    
    salutes = 0
    
    for i in range(len(s)):
         
        if (s[i] == '>') :
         
            for j in s[i:len(s)]:
             
                if (j == '<') :
                     
                    salutes = salutes + 2

    return salutes

#Most efficient solution, only has a single for loop (O(n) efficiency)
def numSalutes(s):
    salutes = 0
    count = 0
    
    for i in s:
        if (i == '<') :
            salutes = salutes + (count * 2)
            
        elif (i == '>') :
            count = count + 1
    
    return salutes


#Compares the efficiency of the algorithms by returning their runtimes
#Large strings are needed to gain a meaningful difference
def compareEfficiency(s):
    start = time.time()
    inefficientSolution(s)
    end = time.time()
    print(end-start)
    
    start = time.time()
    numSalutes(s)
    end = time.time()
    print(end-start)
    
    
compareEfficiency(">--<><><>>><<<")

print(inefficientSolution(">--<><><>>><<<"))
print(numSalutes(">--<><><>>><<<"))
