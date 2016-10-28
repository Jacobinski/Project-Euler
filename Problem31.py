from math import floor

count = 1 # L2 included
num = 200

for A in range(0,int(floor(num/100))+1):
    numA = num - 100*A
    for B in range(0,int(floor(numA/50))+1):
        numB = numA - 50*B
        for C in range(0,int(floor(numB/20))+1):
            numC = numB - 20*C
            for D in range(0,int(floor(numC/10))+1):
                numD = numC - 10*D
                for E in range(0,int(floor(numD/5))+1):
                    numE = numD - 5*E
                    for F in range(0,int(floor(numE/2))+1): 
                        count += 1 # One combination of pennies

print count
