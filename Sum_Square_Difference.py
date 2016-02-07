from time import clock
from functools import reduce

start = clock()
range = list(range(1,100+1))
sumSquare = []
squareSum = []

for i in range:
    sumSquare.append(i)
    squareSum.append(i*i)

sumSquare = reduce(lambda x,y: x+y, sumSquare)
sumSquare *= sumSquare
squareSum = reduce(lambda x,y: x+y, squareSum)
print(sumSquare,'-',squareSum,'=',sumSquare-squareSum)

end = clock()
print('Computation time:',end-start,'seconds')