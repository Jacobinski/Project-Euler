from time import clock

start = clock()
number = 2**1000
array = [int(i) for i in str(number)]
sum = 0
for j in array:
    sum += j
end = clock()

print "The sum of digits is" , sum
print "This problem took" ,end-start, "seconds"
