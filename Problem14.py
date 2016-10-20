from time import clock

start = clock()
check = 1000001*[False]
best_chain = 0
best_number = 0

# Automatically set 0 & 1 to be checked
check[0] = True
check[1] = True

for number in range(1000000):
    if check[number] is False:
        chain = 0
        temp = number # This number holds the manipulated original number
        while temp is not 1:
            if temp <= 1000000 and check[temp] is False:
                check[temp] = True   # Avoids falling onto the same chains letter
            chain += 1
            if temp % 2 is 0:
                temp = temp / 2
            else:
                temp = 3 * temp + 1
        if chain > best_chain:
            best_number = number
            best_chain = chain

end = clock()

print "This computation took" , end-start, "seconds."
print "The longest chain was", best_chain,"numbers."
print "This chain started on",best_number
