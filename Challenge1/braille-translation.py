"""
Created on Sat Feb 19 20:12:05 2022

@author: thomastesselaar

Braille Translation
"""

# This function is the answer to the problem
def stringToBraille(s):
    braille = ["100000", "110000", "100100", "100110", "100010", "110100", 
               "110110", "110010", "010100", "010110", "101000", "111000", 
               "101100", "101110", "101010", "111100", "111110", "111010", 
               "011100", "011110", "101001", "111001", "010111", "101101", 
               "101111", "101011", "001111" ]
    
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
                'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 
                'y', 'z']

    brailleDict = dict(zip(alphabet, braille))
    
    brailleString = ""
    
    for i in s:
        if (i == ' ') :
            brailleString = brailleString + "000000"
        else:
            if (i.isupper()) :
                brailleString = brailleString + "000001"
            brailleString = brailleString + brailleDict[i.lower()]
            
    
    return brailleString


# This is not part of the foo-bar challenge and does the inverse of the above
def brailleToString(n):
    braille = ["100000", "110000", "100100", "100110", "100010", "110100", 
               "110110", "110010", "010100", "010110", "101000", "111000", 
               "101100", "101110", "101010", "111100", "111110", "111010", 
               "011100", "011110", "101001", "111001", "010111", "101101", 
               "101111", "101011", "001111" ]
    
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
                'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 
                'y', 'z']

    inverseBrailleDict = dict(zip(braille, alphabet))

    s = ""
    
    if (type(n) == int) :
        n = str(n)
    
    if ((len(n) % 6) != 0) :
        return "Invalid Entry"
    
    s = ""
    nextCharIsUpper = False
    
    for i in range(0, int(len(n)), 6):
        temp = n[i:i+6]  
        if (temp == "000000") :
            s = s + ' '
            continue
        
        if (temp == "000001") :
            nextCharIsUpper = True
            continue
        
        else:
            if (nextCharIsUpper) :
                s = s + (inverseBrailleDict[temp].upper())
            else :
                s = s + (inverseBrailleDict[temp])
                
            nextCharIsUpper = False
        
    
    return s



print(stringToBraille("Hello there"))
print(brailleToString("000001110010100010111000111000101010000000011110110010100010111010100010"))
