
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
import sys


sys.setrecursionlimit(10**8)





outputfile = open("Walking.txt",'a')


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
    index_arr = np.empty(2**inp,dtype = int)
    # samesignarray = np.empty(2**inp)
    
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
        index_arr[i] = i
        # initial_dict[arr[i]] = i

    print("Made sum ")
    
    walkedarray = np.zeros(2**inp)
    
    
    def walk(i,SignOfValue):
        walkedarray[i] = 2*inp
        walk_dist_min = 2*inp
        for k in range(inp):
            newElement = i ^ (1<<k)
            if np.sign(arr[newElement])  != SignOfValue:
                walkedarray[i] = 1
                walkedarray[newElement] = 1
                return 1
            if walkedarray[newElement] == 0:
                dist_new = walk(newElement,SignOfValue)
            else:
                dist_new = walkedarray[newElement]
            if (dist_new < walk_dist_min):
                walk_dist_min = dist_new
            walkedarray[i] = walk_dist_min+1
        return walk_dist_min+1
    
    
    
    walk(2**inp - 1,np.sign(arr[2**inp - 1]))
    # for i in range(2**inp):
    #     if walkedarray[i] == 0:
    #         walk(i,np.sign(arr[i]))
        
    # arr.sort(kind='heapsort',axis=-1)
    a_s, b_s, c_s = map(list, zip(*sorted(zip(arr, walkedarray, index_arr))))
    
    
    
    for i in range(2**(inp-1),2**inp):
        outputfile.write(str( bin(c_s[i])[2:].zfill(inp)) + "     " + str(int(b_s[i])) + "     " + str(a_s[i])+" \n")
            
    print("Done for " + str(inp))

## Here function executed
if __name__ == "__main__":
    for i in range(13,15):
        HammingFinder(i)
