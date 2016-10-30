# Note: A 4-digit number multiplied by a 1-digit number produces at least a 1-digit number

checked = [] # All found products - Avoids redundancy
pan = set([1,2,3,4,5,6,7,8,9])
sumPan = 0

for i in range(0,2):
    if i is 0:
        aRange = 10000
        bRange = 10
    elif i is 1:
        aRange = 1000
        bRange = 100
    for a in range(1,aRange):
        for b in range(1,bRange):
            c = a * b
            if len(str(a)) + len(str(b)) + len(str(c)) == 9: 
                A = [int(i) for i in str(a)]
                B = [int(i) for i in str(b)]
                C = [int(i) for i in str(c)]
                out = A + B + C
                if pan == set(out): 
                    if c not in checked:
                        checked.append(c)
                        sumPan += c
                        print c
            else:
                continue

print sumPan

