from os import path
import mpmath
from mpmath.ctx_mp_python import _mpf
import numpy as np
import heapq
import math
from mpmath import mp 


outputfile = open("First N least Values Brute Force.txt", 'a')

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


def getFirstNValues(inp):
    
    ## Precision, hange to increase or decrease
    mp.dps = 20


    numbers = np.empty(2*inp, dtype = _mpf)
    data = []

    k = 0
    for i in range(2,200):
        if isNonSquare(i):
            if k>=2*inp:
                break
            numbers[k] = mpmath.mpf(i)**mpmath.mpf('0.5')
            k+=1
    

    temp_matrix = np.empty(inp)      

    
    print("At " + str(inp))
    
    ## Uses a ternary number system type approach to form 3**inp sums 
    def make_sum(val):
        sum = 0
        temp_matrix.fill(0)
        for ind in range(inp):
            tester = val%3
            
            if tester == 1:
                sum -=  numbers[ind]
                temp_matrix[ind] = -1
                # print('-1',end= " ")
            elif tester == 2:
                sum +=  numbers[ind]
                temp_matrix[ind] = 1
                # print('1',end= " ")
            else:
                temp_matrix[ind] = 0
                # print('0',end= " ")
            val = int(val/3)
            if val == 0:
                break
        return sum

    for i in range(inp):
            data.append((-100,1))
            
    heapq.heapify(data)
    
    
    #Uses heap to store values        
    for i in range(1,3**inp):
        val_out = make_sum(i)
        # print("             " + str(val_out))
        if  val_out < 0:
            if val_out > data[0][0]:
                #print(str(val_out)+"           " + str(i))
                heapq.heapreplace(data,(val_out,i))
    
    print("Made sum for " + str(inp))
    
    outputfile.write("At value n = " + str(inp) + "\n")
    
    
    for i in range(inp):
        make_sum(data[i][1])
        outputfile.write(str(data[i][0])+ " " +str(temp_matrix)   + "\n" )
        
        
    outputfile.write("\n\n\n")
    print("Done with " + str(inp))
    

for i in range(12):

    getFirstNValues(i)