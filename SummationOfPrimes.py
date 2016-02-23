from time import clock


start = clock()

i = 2
primes = [2]
limit = 2000000
output = 2  # Automatically add first prime

while i < limit:
    if all(i%j != 0 for j in primes):
        primes.append(i)
        output += i
        print(i)
    i += 1

end = clock()
print('The sum of the primes below {} is {}'.format(limit,output))
print('This computation took {} seconds'.format(end-start))

