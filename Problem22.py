from time import clock

# Note: ord() converts char into ASCII numbers, which are 64 above the desires char -> num values (ie. A -> 65, not 1)

start = clock()
names = []
score = []
index = 0

with open('Problem22txt.txt') as inputFile:
    for line in inputFile:
        names = line.strip(' " ').split('","')

names.sort() # Alphabetic Order
for name in names:
    index += 1
    score.append(index*sum([ord(num)-64 for num in list(name)]))
    # Debugging Print Statements
    print name
    print [ord(num)-64 for num in list(name)]
    print score[index-1]
end = clock()

print "The sum of name scores is",sum(score)
print "This computation took",end-start,"seconds"
