from time import clock

start = clock()
number = 13195 #600851475143
primes = set(range(2,number+1))   #This is killing my computer -> Makes an exclusion list instead
primeFactors = []
i = 1
print(number)

# Generate all primes - Sieve of Erathosthenes
while (i < number):
    i += 1
    if i in primes:  # Determines if this value is prime (This algorithm will remove non-primes as it proceeds)
        if (number % i == 0):  # Prime factor of our number
            while (number % i == 0):
                primeFactors.append(i)
                number = number/i
                print(number)
            newSet = set(range(2,int(number+1)))            
            primes = primes & newSet # Uses the new number to vastly shorten the primes we must look through.                        
            j = 2
            while (i*j<=number):  # Now we remove multiples of our primes. The lowest non-removed value becomes a prime automatically (no factors underneath it)
                primes.discard(i*j)
                j += 1        

print(primeFactors)
print('Max:',max(primeFactors))
end = clock()
print ('Computation Time:',end-start, 'seconds')