"""
Created on Fri Feb 25 18:27:50 2022

@author: thomastesselaar

Ion-Flux-Relabeling
"""

#Using nested for loops, this is a less efficient solution
def parentArr(h, q):
    
    arr = []
    
    size = (2 ** h) - 1
    
    for i in q:
        start = 0
        end = size
        
        if (i == size) :
            arr.append(-1)
            
        elif (i < 1 or i > size or i != int(i)) :
            arr.append(-2)
        
        else :
            while True:
                end = end - 1
                
                mid = start + (end - start) / 2
                
                if (i == mid or i == end) :
                    arr.append(int(end+1))
                    break
                elif (i < mid) :
                    end = mid
                else :
                    start = mid
    
    
    return arr

print(parentArr(4, [7, 3, 5, 1, 3.5, -1, 27]))
