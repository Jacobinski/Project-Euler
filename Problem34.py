from math import factorial

sumX = 0

for x in range(3,1000000):
    fact = sum([factorial(int(i)) for i in str(x)])
    if fact == x:
        print x
        sumX += x

print "The answer is",sumX
