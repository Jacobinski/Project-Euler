primes = []
B = [] # All b's have to be primes as n=0 is a prime
maxA = 0
maxB = 0
maxN = 0
maxPrime = 0

# I'm guessing we won't need primes over 50k
for num in range(2,50001):
    if all(num % prime is not 0 for prime in primes):
        primes.append(num)
        if num <= 1000:
            B.append(num)
            B.append(-num)

maxPrime = primes[-1]

for a in range(-999,1000):
    for b in B:
        n = 0
        while n*n+a*n+b in primes:
            n += 1
        if n*n+a*n+b > maxPrime:
            print "We need a longer prime list"
        if n > maxN:
            maxA = a
            maxB = b
            maxN = n

print "a =",maxA
print "b =",maxB
print "The max product is",maxA * maxB
