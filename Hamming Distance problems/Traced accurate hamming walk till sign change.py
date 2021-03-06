
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


####This uses DFS, so the program halts for large n values, but is more accurate 


outputfile = open("Traced accurate hamming walk till sign change.txt",'a')


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
    daughterElemnt = np.zeros(2 ** inp, dtype=np.int32)
    
    #Recursive DFS approach to calculate how long to move till sign changes
    def walk(i,SignOfValue):
        walkedarray[i] = 2*inp
        walk_dist_min = 2*inp
        for k in range(inp):
            newElement = i ^ (1<<k)
            if np.sign(arr[newElement])  != SignOfValue:
                walkedarray[i] = 1
                walkedarray[newElement] = 1
                daughterElemnt[i] = newElement
                daughterElemnt[newElement] = i
                return 1
            if walkedarray[newElement] == 0:
                dist_new = walk(newElement,SignOfValue)
            else:
                dist_new = walkedarray[newElement]
            if (dist_new < walk_dist_min):
                walk_dist_min = dist_new
                daughterElemnt[i] = newElement

        walkedarray[i] = walk_dist_min+1
        return walk_dist_min+1
    
    
    
    walk(2**inp - 1,np.sign(arr[2**inp - 1]))
    a_s, b_s, c_s = arr, walkedarray, index_arr

    print(daughterElemnt)

    # for i in range(2**(inp-1),2**inp):
    for i in range(0, 2 ** inp):
        if arr[i] > 0:
            outputfile.write(
                str(bin(c_s[i])[2:].zfill(inp)) + "     " + str(int(b_s[i])) + "     " + str(a_s[i]) + "    ")
            temp = i
            outputfile.write(str(bin(temp)[2:].zfill(inp)))
            while (np.sign(arr[temp]) == np.sign(arr[daughterElemnt[temp]])) and temp != daughterElemnt[temp]:
                outputfile.write(" => " + str(bin(daughterElemnt[temp])[2:].zfill(inp)))
                temp = daughterElemnt[temp]
            outputfile.write(" => " + str(bin(daughterElemnt[temp])[2:].zfill(inp)))

            outputfile.write("\n")

    print("Done for " + str(inp))


## Here function executed
if __name__ == "__main__":
    outputfile.write("The binary number in column 1 represents the coefficients taken , 1 => +1 coefficient, 0 => -1 coefficient \n Coefficients     Steps till sign change    Evaluated value    Traced\n")
    
    for i in range(2, 9):
        
        HammingFinder(i)