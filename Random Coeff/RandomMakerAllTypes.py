from os import path
#import mpmath
#from mpmath.ctx_mp_python import _mpf
import numpy as np
import heapq
import random
import math
import sympy


TOTAL = 50
#The first n numbers from hich random elements are chosen from, change to increase/decrease raange


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

def MatrixMaker(inp,coeff_array):

    
    numbers_list = random.sample(list(range(1,TOTAL)), inp)
    numbers = np.zeros(inp)
    #initial_numbers = np.zeros(TOTAL)
    # k= 0
    # for i in range(2,200):
    #     if isNonSquare(i):
    #         if k >= TOTAL:
    #             break
    #         initial_numbers[k] = np.sqrt(i)
    #         k+=1
    k = 0
    for num in numbers_list:
        numbers[k] = np.sqrt(num)
        k+=1    



    arr = np.empty(2**inp)
    initial_dict = {}
    
    
    #Chooses numbers
    #numbers_list = random.sample(list(initial_numbers), inp)
    #print(numbers_list)
    #numbers = np.array(numbers_list)
    numbers.sort(kind='heapsort',axis=-1)
    print(numbers)


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
    for i in range(2**(inp-1),2**inp):
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
            CountFalse+=1
     
    print(CountTrue)        
    print(CountFalse)
                   
    

## Here function executed
if __name__ == "__main__":
    makefor = int(input())
    for i in range(10):
        coeff =np.zeros((makefor,makefor ))
        MatrixMaker(makefor,coeff_array=coeff)