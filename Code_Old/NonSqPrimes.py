import math

numbers = []



def isNonSquare( number ):
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


for i in range(2,1000):
    if isNonSquare(i):
        numbers.append(math.sqrt(i))

print(numbers)