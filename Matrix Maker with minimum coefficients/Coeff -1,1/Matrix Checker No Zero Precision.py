
import numpy as np
import heapq



from os import path
from mpmath import mp 

from mpmath.ctx_mp_python import _mpf
import numpy as np
import heapq
import random
import math
import sympy


mp.dps = 40


outputfile = open("Matrix Checker No Zero Precision.txt",'a')

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

def MatrixMaker(inp):

    outputfile.write("********************************************************************************\n")
    outputfile.write("For n = " + str(inp) + '\n')
    print("At " + str(inp))
    
    
    
    coeff_array = np.zeros((inp,inp))
    arr = np.empty(2**inp,dtype=_mpf)

    initial_dict = {}
    
    
    numbers = np.zeros(inp,dtype= _mpf)

    k= 0
    for i in range(2,200):
        if isNonSquare(i):
            if k >= inp:
                break
            numbers[k] = mp.mpf(i)**mp.mpf('0.5')
            k+=1


    def RowMaker(value,size):
        
        arraymade = np.zeros(inp)
        signdata = initial_dict[value]
        for i in range (size):
            if signdata & (1 << i) > 0 :
                arraymade[i] = 1
            else:
                arraymade[i] = -1
        
        return arraymade

        # outputfile.write(str(coeff_array[row])+ '\n')
        
            
    def converter(value,size,row):
        
        signdata = initial_dict[value]
        for i in range (size):
            if signdata & (1 << i) > 0 :
                coeff_array[row,i] = 1
            else:
                coeff_array[row,i] = -1     

        

    ##Calculates Sum
    for i in range(2**inp):
        sum = 0
        for k in range(inp):
            if i & 1<<k:
                sum += numbers[k]
            else:
                sum -= numbers[k]
        arr[i] = sum 
        initial_dict[arr[i]] = i

    print("Made sum ")

    arr.sort(kind='heapsort',axis=-1)

    print("Sorted sum ")




    b = np.ones(inp)
    
    
    ## Makes matrix    
    l=1             
    for i in range(2**(inp-1),2**inp): #2**(inp-1) to take n lowest by magnitude
        value = arr[i]
        
        converter(value,inp,l-1)
        
        if np.linalg.matrix_rank(coeff_array) == l:
            l+=1
            
        if l == inp + 1 and np.linalg.det(coeff_array) != 0:
            break
       
    
    
    

    x = np.linalg.solve(coeff_array, b)
    
    CountTrue = 0
    CountFalse= 0
    
    
    #Checks all 
    for element in arr:
        output = RowMaker(element,inp)
        valueByMultiply = np.dot(x,output)
        
        if np.sign(valueByMultiply) == np.sign(element):
            CountTrue+=1
        else:
            outputfile.write(" \n" +str(output) + " Added value: "+ str(element) + " Dot Product value : "+ str(valueByMultiply) + "False " + " \n \n")
            CountFalse+=1
     
    print(CountTrue)        
    print(CountFalse)
    outputfile.write('\n  \n Final Array taken : \n')
    outputfile.write(str(coeff_array))
    outputfile.write('\n ')
    outputfile.write(str(x))
    outputfile.write('\n ')
    outputfile.write("Trues: " + str(CountTrue) + "\t Falses " + str(CountFalse) + '\n \n \n')
    print("File Written for" + str(inp))
                   
    

## Here function executed
if __name__ == "__main__":
    for i in range(3,25):
        
        MatrixMaker(i)
