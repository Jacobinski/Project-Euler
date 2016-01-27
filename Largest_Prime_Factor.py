from time import clock

start = clock()
number = 600851475143
primes = set(range(2,number+1))

# Generate all primes - Sieve of Erathosthenes
for y in range(2,number+1):
    if y in primes:  # Determine if number not already removed
        z = 2  #Remove multiples
        while (z*y<=number):
            primes.discard(z*y)
            z += 1

#We can also determine if a number is prime by looking at the prime factors of primes from before
#Do both loops at the same time

# Factorize our number
num = number
primeFactors = []

for j in primes:
    while (num % j == 0):
        primeFactors.append(j)
        num = num/j

print(number)
print(primeFactors)
print('Max:',max(primeFactors))
end = clock()
print ('Computation Time:',end-start, 'seconds')