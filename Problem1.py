from time import time

start = time()

maxNumber = 1000
sum = 0

for i in range(maxNumber):
    if i%3 == 0 or i%5 == 0:
        sum += i

print(sum)
end = time()
print(end-start)