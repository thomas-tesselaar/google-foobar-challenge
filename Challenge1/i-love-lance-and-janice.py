"""
Created on Mon Feb 14 16:42:14 2022

@author: thomastesselaar

I love Lance and Janice
"""
import time

#Using an array of lower case letters
def DecryptMessage(str):
    
    arr = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    newstr = ''
    
    for i in range(len(str)):
        
        if str[i].islower():
            
            k = arr[25-arr.index(str[i])]
            
            newstr = newstr + k
        
        else:
            newstr = newstr + str[i]
    
    return newstr
            
#Using an string for lowercases. This is most efficient
def Answer(str):
    
    newstr = ''
    
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    for i in range(len(str)):
        
        if str[i].islower():
            
            k = alphabet[25-alphabet.index(str[i])]
            
            newstr = newstr + k
        
        else:
            newstr = newstr + str[i]
    
    return newstr


def CompareEfficiency(n):    
    start = time.time()
    DecryptMessage(n)
    end = time.time()
    print(end-start)
    
    start = time.time()
    Answer(n)
    end = time.time()
    print(end-start)

    

CompareEfficiency("wrw blf hvv ozhg mrtsg'h vkrhlwv?")
