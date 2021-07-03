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
    temp_matrix.fill(0)
    for ind in range(inp):
        tester = val%3
        
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





#out_put = np.zeros(3**inp, dtype = bool)

coeff_array = np.zeros((inp,inp))

matrixGen.func(inp,coeff_array)

b = np.ones(inp)

x = np.linalg.solve(coeff_array, b)

Trues = 0
falses = 0
for i in range(3**inp):
    sign_val = make_sum(i)
    out = np.dot(temp_matrix,x)
    if np.sign(out) == np.sign(sign_val):
        #print (str(sign_val) + " True")
        #print("True ")
        Trues+=1
    else:
        print(out)
        print (str(sign_val) + " False")
        #print("False")
        falses+=1
        
print(Trues)

print(falses)        
#print(out_put)
    