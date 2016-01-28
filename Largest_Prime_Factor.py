from time import clock

start = clock()
number = 600851475143
primeFactors = []
i = 1
print(number)

# We factor our number from lower values -> higher values
# This means that each lowest prime will eliminate higher composites 
# --> A 2 factored out will simplify composites ( 6 = 2*3 -> 3)
# We will loop this structure until we finish
# This method relates to the Sieve of Eratosthenes

while (i < number):
    i += 1
    if (number % i == 0):  # Factor of our number 
        while (number % i == 0): #Multiple factors
            primeFactors.append(i)
            number = number/i

print(primeFactors)
print('Max:',max(primeFactors))
end = clock()
print ('Computation Time:',end-start, 'seconds')