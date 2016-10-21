from math import factorial

n = factorial(100)
answer = sum([int(i) for i in str(n)])

print "The sum of 100!'s digits is",answer
