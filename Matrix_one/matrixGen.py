from os import path
import mpmath
from mpmath.ctx_mp_python import _mpf
import numpy as np
import heapq
import random
import math

from mpmath import mp 

def isNonSquare(number):
        iterator = number 
        for i in range(2,iterator):
            if number%i == 0:
                count = 0 
                while number%i == 0:
                    number = number/i
                    count += 1
                if count%2 == 0:
                    return False
        return True

def func(inp,coeff_array):

    mp.dps = 50

    numbers = []
    for i in range(2,200):
        if isNonSquare(i):
            numbers.append(mpmath.mpf(i)**mpmath.mpf('0.5'))


    # print(numbers)
    # inp = int(input())

    arr = np.empty(2**inp,dtype=_mpf)

    # print("Presently at " + str(user_inp))

    outputfile = open("mpmathpout_new_new.txt",'a')
    data = [] 
    initial_dict = {}
    data_dict = {}

    def converter(data,size,row):
        sums = np.zeros(size)
        values = data_dict[data]
        for i in range (size):
            if (values[1] & 1 << i) > 0 and  (values[0] & 1 << i) == 0:
                coeff_array[row,i] = 1
            elif (values[0] & 1 << i) > 0 and  (values[1] & 1 << i) == 0:
                coeff_array[row,i] = -1
                
        
            
                
        #outputfile.write(str(sums))


    ## Initialise heap with values -ve enough to not cause problem
    for i in range(2*inp):
        data.append(-100 + i)
        data_dict[100-i] = (0,i)


    ##Calculates Sum
    for i in range(2**inp):
        sum = mpmath.mpf('0')
        for k in range(inp):
            if i & 1<<k:
                sum += numbers[k]
        arr[i] = sum
        initial_dict[arr[i]] = i

    print("Made sum ")

    arr.sort(kind='heapsort',axis=-1)

    print("Sorted sum ")

    heapq.heapify(data)


    ##Iterates over the data to calculate difference and insert in heap

    for i in range(2**inp - 1):
        for j in range(1,inp + 1):
            
            # doing & and check for 0 is important so that values dont repeat
            if i+j < 2**inp and initial_dict[arr[i]] & initial_dict[arr[i+j]] == 0:

                diff = arr[i] - arr[i+j]
                if diff > data[0]:
                    removed_element = heapq.heapreplace(data, diff)
                    
                    #Use -ve here as it makes easier to sort with dictionary
                    data_dict[-diff] = (initial_dict[arr[i]],initial_dict[arr[i+j]])
                    data_dict.pop(-removed_element,100)
                
    #outputfile.write(str(inp) + ' : \n')

    l=0             
    for i in sorted(data_dict.keys()):
        if l >= inp:
            if np.linalg.det(coeff_array) == 0:
                radom_row = int(random.random()*(inp-1))
                converter(i,inp,radom_row)
            else:
                break
        #outputfile.write(str(i) + " ") 
        else:
            converter(i,inp,l)
        #outputfile.write('\n')  
        l+=1
                       
    #outputfile.write('\n')  
    #outputfile.write('\n') 
    
    print(data_dict)
    # for dat in data:
    #     outputfile.write(str(dat) + " ") 
    #     converter(-dat,inp)
    #     outputfile.write('\n') 

        
    print("Done with " + str(inp))
    return coeff_array
