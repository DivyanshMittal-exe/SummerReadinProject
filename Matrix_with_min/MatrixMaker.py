
import numpy as np
import heapq



#Tells if number is non square or not

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

def func(inp,coeff_array,outputfile):

    
    #Construucts the non square numbers array
    numbers = np.zeros(inp)
    k= 0
    for i in range(2,200):
        if isNonSquare(i):
            if k >= inp:
                break
            numbers[k] = np.sqrt(i)
            k+=1




    arr = np.empty(2**inp)
    data = [] 
    initial_dict = {}
    data_dict = {}


    #Function to make matrix
    def converter(data,size,row):
        sums = np.zeros(size)
        values = data_dict[data]
        for i in range (size):
            if (values[1] & 1 << i) > 0 and  (values[0] & 1 << i) == 0:
                coeff_array[row,i] = 1
            elif (values[0] & 1 << i) > 0 and  (values[1] & 1 << i) == 0:
                coeff_array[row,i] = -1
            else:
                coeff_array[row,i] = 0
 
        outputfile.write(str(coeff_array[row])+ '\n')



    ## Initialise heap with values -ve enough to not cause problem
    for i in range(3*inp):
        data.append(-100 + i)
        data_dict[100-i] = (0,i)


    ##Calculates Sum
    for i in range(2**inp):
        sum = 0
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
            if i+j < 2**inp and (initial_dict[arr[i]] & initial_dict[arr[i+j]] == 0):
                diff = arr[i] - arr[i+j]
                if diff > data[0]:
                    removed_element = heapq.heapreplace(data, diff)
                    
                    #Use -ve here as it makes easier to sort with dictionary
                    data_dict[-diff] = (initial_dict[arr[i]],initial_dict[arr[i+j]])
                    data_dict.pop(-removed_element,100)


    
    #Calculates the matrix
    l=1             
    for i in sorted(data_dict.keys()):
        
        converter(i,inp,l-1)
        
        if np.linalg.matrix_rank(coeff_array) == l:
            l+=1
            
        if l == inp + 1 and np.linalg.det(coeff_array) != 0:
            break
       
                
        
    print("Done with " + str(inp))
    return coeff_array
    
