from collections import Counter as mset
from functools import reduce
from time import clock

start = clock()
factors = mset() # Empty
range = list(range(1,20+1)) 

# This program finds the smallest multiple using the highest multiplicity of each prime
# Code based on Problem 3 from Project Euler
for num in range:
    i = 1
    tempFactors = mset()
    while (i < num):
        i += 1
        if (num % i == 0):  # Factor of our number 
            while (num % i == 0): # Multiple factors
                tempFactors[i] += 1
                num = num/i
    factors = factors | tempFactors # Union

factors = list(factors.elements())
output = reduce(lambda x,y: x*y, factors)
print(factors)
print(output)
end = clock()
print('Computation Time:',end-start,'seconds')