
import numpy as np
import heapq



from os import path
#import mpmath
#from mpmath.ctx_mp_python import _mpf
import numpy as np
import heapq
import random
import math
import sympy





outputfile = open("Hamming dist 1, same sign.txt",'a')


#Determines if number is non square
def isNonSquare(number):
        iterator = number 
        for i in range(2,iterator):
            if number%i == 0:
                count = 0 
                while number%i == 0:
                    number = number/i
                    count += 1
                if count > 1:
                    return False
        return True
    
    

    


def HammingFinder(inp):

    outputfile.write("********************************************************************************\n")
    outputfile.write("For n = " + str(inp) + '\n')
    print("At " + str(inp))
    
    arr = np.empty(2**inp)
    
    
    sign_dict = {}
       
    
    numbers = np.zeros(inp)
    k= 0
    for i in range(2,200):
        if isNonSquare(i):
            if k >= inp:
                break
            numbers[k] = np.sqrt(i)
            k+=1   


    ##Calculates Sum
    for i in range(2**inp):
        sum = 0
        for k in range(inp):
            if i & 1<<k:
                sum += numbers[k]
            else:
                sum -= numbers[k]
        arr[i] = sum 
        # initial_dict[arr[i]] = i

    print("Made sum ")

    
    # for each element by flipping each bit checks if sign is same or not
    for i in range(2**inp):
        samesigns = 0
        for k in range(inp):
            newElement = i ^ (1<<k)
            if np.sign(arr[newElement]) == np.sign(arr[i]):
                samesigns+=1
        # samesignarray[i] = samesigns
        sign_dict[arr[i]] = np.array([i,samesigns],dtype = int)
        
    arr.sort(kind='heapsort',axis=-1)
    
    for i in range(2**(inp-1),2**inp):
        outputfile.write(str( bin(sign_dict[arr[i]][0])[2:].zfill(inp)) + "     " + str(int(sign_dict[arr[i]][1])) + "     " + str(arr[i])+" \n")
            
    print("Done for " + str(inp))

## Here function executed
if __name__ == "__main__":
    outputfile.write("The binary number in column 1 represents the coefficients taken , 1 => +1 coefficient, 0 => -1 coefficient \n Coefficients     Same sign hamming dist 1     Evaluated value(sorted)\n")
    for i in range(2,15):
        HammingFinder(i)
