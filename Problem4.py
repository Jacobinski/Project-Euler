from time import clock

start = clock()

# 999 * 999 = 988,001 
counter = 988-1 # This will be mirrored to make decreasing palindromes
multiples = list(reversed(range(100,999+1)))
output = []
found = False

def makePalindrome(num):
    start = str(num)
    end = start[::-1] # Reverse
    return int(start+end)

while (found != True):
    num = makePalindrome(counter)
    div = 0
    for i in multiples:
        if (num/i).is_integer() and (num/i > 99) and (num/i < 1000):
            output.append(i)
            output.append(num/i)
            found = True
            break 
    counter = counter - 1    
    
print(output[0],'*',output[1],'=',output[0]*output[1])
end = clock()
print('Computation Time:',end-start,'seconds')
