from time import clock

start = clock()
inArray = []
triangleSize = 0
with open('Problem18txt.txt') as inputfile:
    for line in inputfile:
        triangleSize += 1
        inArray.append([int(i) for i in line.strip().split(' ')])
print inArray
# We will go from the bottom to the top of the triangle, adding the larger of the two
# splits in the 'path' to reverse engineer the largest
for h in range(triangleSize): # The -1 is to avoid the top row
    y = triangleSize - (h + 1)
    print "y=",y
    for b in range(y): # The -1 is to avoid going to the end of the row
        print "x=",b
        x = b
        if inArray[y][x] > inArray[y][x+1]:
            inArray[y-1][x] += inArray[y][x]
        else:
            inArray[y-1][x] += inArray[y][x+1]

maxPath = inArray[0][0] # The top of the triangle is the max path
end = clock()

print "The max summation is",maxPath
print "This computation took",end-start,"seconds"
