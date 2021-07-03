from os import path
import mpmath
from mpmath.ctx_mp_python import _mpf
import numpy as np
import heapq
import math


mpmath.mp.dps = 50
i = mpmath.mpf(2)**mpmath.mpf('0.5')

print(i)
print(mpmath.mpf(i)*mpmath.mpf(i))
