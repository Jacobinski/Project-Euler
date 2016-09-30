# Non-trial division implementation of the sieve
# http://stackoverflow.com/questions/19345627/python-prime-numbers-sieve-of-eratosthenes

from time import clock


start = clock()

limit = 2000000
sieve = [True] * (limit + 1)
primes = []

for p in range (2, limit +1):
    if sieve[p] is True:
        primes.append(p)
        for n in range (p, limit + 1, p):
            sieve[n] = False  #All prime multiples = false

end = clock()

print('The sum of the primes below {} is {}'.format(limit,sum(primes)))
print('This computation took {} seconds'.format(end-start))

