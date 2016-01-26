from time import clock

start = clock()
i = 0  # The first number
j = 1  # The second number
sum = 0  # Empty to start
output = 0

while sum < 4000000:
    i = j
    j = sum
    sum = i + j  # Shift old values over 1. Get a new sum
    if sum % 2 == 0:
        output += sum
                

print(output)
end = clock()
print(end-start)