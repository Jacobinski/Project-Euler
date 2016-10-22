from time import clock

start = clock()
primes = []
sumDivisors = [1]*10002 #  Num=2 will go in index 2
# 1 as we will be multiplying this by prime sum of divisors later

for i in range(1,10001):
    num = i + 1 # Start @ 2 
    # Get new primes
    if all(num % prime is not 0 for prime in primes):
        primes.append(num)
    # Determine the sum of proper divisors
    # http://www.cut-the-knot.org/blue/NumberOfFactors.shtml
    for prime in primes:
        c = 0
        temp = num
        while temp % prime is 0:
            c += 1
            temp = temp / prime
        # http://mathschallenge.net/library/number/sum_of_divisors
        if num % prime is 0:
            sumDivisors[num] *= (prime ** (c+1) - 1)/(prime-1)
    # As we want the proper sum of divisors, we don't want the number itself to be a divisori
    sumDivisors[num] -= num

amicable = 0
for i in range(2,10000):
    k = sumDivisors[i]

    # Note: use ==, not 'is' as we do not want reference equality
    if k < 10000 and i == sumDivisors[k] and i != k:
        amicable += i + k
        print "Amicable pair",i,"|",k
    #if sumDivisors[i] < 10000:
        #print "1",i,"2",sumDivisors[i]

amicable = amicable / 2 # Exclude redundancies
end = clock()

print "The sum of amicable numbers under 10000 is",amicable
print "This computation took",end-start,"seconds"
