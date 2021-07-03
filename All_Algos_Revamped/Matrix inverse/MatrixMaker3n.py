from os import path
import mpmath
from mpmath.ctx_mp_python import _mpf
import numpy as np
import heapq
import math

import random

from mpmath import mp 







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

def myfunc(inp,coeff_array,b):
    
    #mp.dps = precc
    numbers = np.empty(2*inp)
    data = {}
    
    
    
    k = 0
    for i in range(2,200):
        if isNonSquare(i):
            if k>=2*inp:
                break
            numbers[k] = np.sqrt(i)
            k+=1
    

    temp_matrix = np.empty(inp)      

    def make_sum(val):
        sum = 0
        for ind in range(inp):
            tester = val%3
            temp_matrix.fill(0)
            if tester == 1:
                sum -=  numbers[ind]
                temp_matrix[ind] = -1
            elif tester == 2:
                sum +=  numbers[ind]
                temp_matrix[ind] = 1
            val = int(val/3)
            if val == 0:
                break
        return sum

    # for i in range(inp):
    #         data.append((-100,1))
            
    # heapq.heapify(data)
            
            
    for i in range(1,3**inp):
        val_out = make_sum(i)
        # if val_out in data:
        #     print(val_out)
        data[val_out] = i
        
    indexArray = random.sample(range(0, 3**inp-1), inp)
    
    k = 0
    for index in indexArray:
        val_out = make_sum(index)
        coeff_array[k] = temp_matrix
        b[k] = np.sign(val_out)
        
        
    #print("Making array det not 0")
        
    while np.linalg.det(coeff_array) == 0:
        radom_row = int(random.random()*3*(inp))%inp
        im = random.randrange(0, 3**inp-1)	
        val_out = make_sum(im)
        coeff_array[radom_row] = temp_matrix
        b[radom_row] = np.sign(val_out)
      
      
                
    # for i in range(inp):
    #     print(data[i])
    # print(3**inp - 1)
    # print(len(data))

    # if 3**inp - 1 == len(data):
    #     print("Precision for " + str(inp)  + " is " + str(precc))
    # else:
    #     myfunc(inp,precc+1)
    
    
# inp = int(input())
# prec = int(input())

# for i in range(4,15):
#     myfunc(inp=i,precc=i//2)