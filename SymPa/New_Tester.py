import numpy as np
from os import path
import mpmath
from mpmath.ctx_mp_python import _mpf
import numpy as np
import heapq
import math
import matrixGen
from mpmath import mp 



lis = [(('-0.0000044621293978802881326738'), 41129874),
(('-0.0000039910829957883996719527'), 67331664),
(('-0.0000044610741846366815262746'), 110878185),
(('-0.0000035319675021669953837375'), 103833603),
(('-0.0000020349918927848071746774'), 117296419),
(('-0.0000044610741846366747500111'), 24784770),
(('-0.0000038474348253577462857997'), 18584088),
(('-0.000001574012341305287051435'), 113519765),
(('-2.1462602876809921872286e-7'), 24756687),
(('-2.2771366351227500992443e-7'), 49270273),
(('-2.2771366351226823366086e-7'), 6223525),
(('-2.2771366351226823366086e-7'), 6223769),
(('-9.5702373594211718544136e-7'), 21919741),
(('-0.0000035319675021669886074739'), 17740188),
(('-0.0000015740123413052802751715'), 27426350),
(('-9.5702373594209008038705e-7'), 21919985),
(('-2.2771366351227500992443e-7'), 49270517)]

inp = 17

var = np.zeros(inp)

outputfile = open("New_algo.txt",'a')
lis.sort()
def maker(number):
    var.fill(0)
    for ind in range(inp):
        tester = number%3
        
        if tester == 1:
            var[ind] = -1
        elif tester == 2:
           var[ind] = 1
        number = int(number/3)
        if number == 0:
            break
        
outputfile.write('\n')

for item in lis:
    maker(item[1])
    
    outputfile.write(str(item[0]))
    outputfile.write(str(var) + '\n')