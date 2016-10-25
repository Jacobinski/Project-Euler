from math import factorial
from math import floor

digits = [0,1,2,3,4,5,6,7,8,9]
position = 1000000 - 1
length = 10
sequence = []

#digits = [0,1,2]
#position = 4 - 1 # The (-1) was discovered using the test case
#length = 3
#sequence = []

# The idea is to find the combinations of (length-1). This acts like an odometer, rolling over changes the first number in the sequence
# This rolling over is what we will try to calculate. The digits is in the order of priority which we can assign numbers to the odometer

while len(digits) > 0:
    combs = factorial(length - 1)
    rollover = int(floor(position/combs))
    sequence.append(digits[rollover])
    del digits[rollover]
    length -= 1
    position -= rollover * combs

print sequence
