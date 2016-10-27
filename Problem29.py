myList = []

for a in range(2,101):
    for b in range(2,101):
        myList.append(a**b)

mySet = set(myList)
print len(mySet)
