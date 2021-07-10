from os import path
import numpy as np
import heapq
import math
import MatrixMaker

 


outputfile = open("MatrixMethodCheckNew.txt",'a')

def matrixmethod(inp):
    outputfile.write("********************************************************************************\n")
    outputfile.write("For n = " + str(inp) + '\n')
    print("At " + str(inp))
    
    
    #Construucts the non square numbers array
    
    numbers = np.empty(2*inp)
    k = 0
    for i in range(2,200):
        if MatrixMaker.isNonSquare(i):
            if k>=2*inp:
                break
            numbers[k] = np.sqrt(i)
            k+=1
    

    
    temp_matrix = np.empty(inp)      

    #Fuction to make the indices
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




    ### Solving the matrix here

    coeff_array = np.zeros((inp,inp))

    # MatrixMaker.func(inp,coeff_array,outputfile)
    
    coeff_array = np.array([[-1, -1,  1,  1,  1,  1,  0, -1, -1,],
                            [-1, -1, -1,  0,  1,  1,  1,  0, -1,],
                            [ 0, -1, -1,  0, -1,  1,  1, -1,  1,],
                            [ 1,  0,  1,  1, -1,  0, -1,  1, -1,],
                            [-1, -1, -1,  1,  1,  0, -1,  1,  0,],
                            [ 1,  0,  1,  1, -1, -1,  1, -1,  0,],
                            [ 0, -1,  0, -1,  0, -1,  0,  1,  1,],
                           [-1,  1,  1, -1,  1, -1, -1,  0,  1],
                            [ 1, -1,  0, -1,  1,  0,  0, -1,  1,]])

    # [-1,  1,  1, -1,  1, -1, -1,  0,  1]

    b = np.ones(inp)

    x = np.linalg.solve(coeff_array, b)

    print("Made matrix for " + str(inp))

    Trues = 0
    falses = 0
    
    
    ## Computing true false by checking all 
    for i in range(1,3**inp):
        sign_val = make_sum(i)
        out = np.dot(temp_matrix,x)
        if np.sign(out) == np.sign(sign_val):
            # outputfile.write(str(temp_matrix) + " Added value: "+ str(sign_val) + " Dot Product value : "+ str(out) + "True \n")
            
            Trues+=1
        else:
            outputfile.write(" \n" +str(temp_matrix) + " Added value: "+ str(sign_val) + " Dot Product value : "+ str(out) + "False " + " \n \n")
            
            
            falses+=1
            


    ##Outputing the findings
    outputfile.write('\n  \n Final Array taken : \n')
    outputfile.write(str(coeff_array))
    outputfile.write('\n ')
    outputfile.write(str(x))
    outputfile.write('\n ')
    outputfile.write("Trues: " + str(Trues) + "\t Falses " + str(falses) + '\n \n \n')
    print("File Written for" + str(inp))
    
    

# for i in range (2,15):
#     matrixmethod(i)
matrixmethod(9)
    
    