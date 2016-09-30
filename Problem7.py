from time import clock

start = clock()
primes = [2]
i = 1
end = False

while not end:
    i += 1
    if all(i%j != 0 for j in primes): # if no prime factors -> number is prime
        primes.append(i)
    if len(primes) == 10001:
        print(primes[10001-1])
        end = True

end = clock()
print('Computation Time:',end-start,'seconds')
