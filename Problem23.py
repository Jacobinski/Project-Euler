from time import clock

start = clock()
primes = []
sumDivisors = [1]*(28123+1) #  Num=2 will go in index 2 -> 28123 is the upper limit for this problem
#abundant = [False] * (28134) # Every multiple of an abundant number is abundant
abundant = []
nonAbundantSum = []
# Much of this code was taken from Problem21

for i in range(1,28123):
     num = i + 1 # Start @ 2
     #print num
     #if abundant[num] == True:
     #    continue # We have shown this is abundant. Skip it
     # Get new primes
     if all(num % prime is not 0 for prime in primes):
        primes.append(num)
     for prime in primes:
        c = 0
        temp = num
        while temp % prime is 0:
            c += 1
            temp = temp / prime
        if num % prime is 0:
            sumDivisors[num] *= (prime ** (c+1) - 1)/(prime-1)
     # As we want the proper sum of divisors, we don't want the number itself to be a divisor
     sumDivisors[num] -= num
     if num < sumDivisors[num]:
        abundant.append(num)

print abundant

# Return True if it is the sum of two abundant
def isSumAbundant(num):
    for a in abundant:
        # Starts with lowest abundant -> increasing order
        sub = num - a
        if sub < 0:
            return False
        elif sub in abundant:
            return True
    return False # All checked

for num in range (1,28123):
    if not isSumAbundant(num):
        nonAbundantSum.append(num)
        print(num)

print sum(nonAbundantSum)
