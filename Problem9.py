# -- Solve for b in terms of a -- 
#[a^2 + b^2 = c^2] & [a + b + c = n]
# a^2 + b^2 = (n-a-b)^2
# a^2 + b^2 = (n^2 - 2an - 2bn + 2ab + a^2 + b^2)
# 0 = n^2 - 2an - 2bn + 2ab
# bn - ab = (n^2)/2 - an
# b = [(n^2)/2-an]/(n-a)

from time import clock
from math import sqrt


start = clock()
n = 1000
a = 0.0   # Starting point
b = None  # Unknown
c = None  # Unknown
found = False

while not found:
    a += 1
    b = ((n**2)/2-a*n)/(n-a)
    c = sqrt(a**2+b**2)
    if a.is_integer() and c.is_integer():
        found = True  

end = clock()
print('{} + {} + {} = {}'.format(a,b,c,n))
print('{} * {} * {} = {}'.format(a,b,c,a*b*c))
print('Computation Time: {} seconds'.format(end-start))
