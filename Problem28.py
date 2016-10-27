size = 1001*1001
check = [1]
add = 2
num = check[-1]

# Notice that the spacing in the spiral follows a 2*n pattern
while num+add*4 <= size:
    for x in [1,2,3,4]:
        check.append(num+add*x)
    add += 2
    num = check[-1]

print sum(check)
