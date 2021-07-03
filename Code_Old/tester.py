import numpy as np
import mpmath
from mpmath.ctx_mp_python import _mpf


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


mpmath.mp.dps = 50

inp = int(input())
nsqr = np.empty(2*inp, dtype =np.longdouble)

k = 0
for i in range(2,200):
    if isNonSquare(i):
        if k>=2*inp:
            break
        nsqr[k] = np.sqrt(np.longdouble(i))
        k+=1


int1 = 82561


int2 = 6222


sum1 = np.longdouble(0)
sum2 = np.longdouble(0)


for i in range(32):
    if 1<<i & int1:
        sum1 += nsqr[i]
        print(nsqr[i])
        
print("\n")
for i in range(32):
    if 1<<i & int2:
        sum2 += nsqr[i]
        print(nsqr[i])
        
        
print()        
print(sum2)
print(sum1)
print(sum2 - sum1)
print("\n")
print("\n")
print("\n")

int1 =17064


int2 =6215

sum1 =  np.longdouble(0)
sum2 =  np.longdouble(00)


for i in range(32):
    if 1<<i & int1:
        sum1 += nsqr[i]
        print(nsqr[i])
        
print("\n")
for i in range(32):
    if 1<<i & int2:
        sum2 += nsqr[i]
        print(nsqr[i])
print()        
        
print(sum2)
print(sum1)
print(sum2 - sum1)

def rand():

    82561
    6222

    17064
    6215
    pass