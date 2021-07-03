from os import path
import mpmath
from mpmath.ctx_mp_python import _mpf
import numpy as np
import heapq
import math
import matrixGen

from mpmath import mp 

inp = int(input())
mp.dps = 20


numbers = np.empty(2*inp, dtype = _mpf)
data = []

k = 0
for i in range(2,200):
    if matrixGen.isNonSquare(i):
        if k>=2*inp:
            break
        numbers[k] = mpmath.mpf(i)**mpmath.mpf('0.5')
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

for i in range(inp):
        data.append((-100,1))
        
heapq.heapify(data)
        
        
for i in range(1,3**inp):
    val_out = make_sum(i)
    if  val_out < 0:
        if val_out > data[0][0]:
            print(str(val_out)+"           " + str(i))
            
            heapq.heapreplace(data,(val_out,i))
            
for i in range(inp):
    print(data[i])