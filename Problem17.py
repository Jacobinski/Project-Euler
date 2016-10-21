from time import clock


def numLen(integer):
    output = 0
    array = [int(i) for i in str(integer)]
    length = len(array) 
    if length is 1:
        dict = { 0:0 ,1:3 ,2:3 , 3:5, 4:4, 5:4, 6:3, 7:5, 8:5, 9:4 }
        output += dict[integer]
    elif length is 2:
        if integer < 20: # 10-19
            dict = { 10:3, 11:6, 12:6, 13:8, 14:8 , 15:7, 16:7, 17:9, 18:8, 19:8 }
            output += dict[integer]
        elif integer < 30: # 20-29
            output += 6 + numLen(integer-20)
        elif integer < 40: # 30-39
            output += 6 + numLen(integer-30)
        elif integer < 50: # 40-49
            output += 5 + numLen(integer-40)
        elif integer < 60: # 50-59
            output += 5 + numLen(integer-50)
        elif integer < 70: # 60-69
            output += 5 + numLen(integer-60)
        elif integer < 80: # 70-79
            output += 7 + numLen(integer-70)
        elif integer < 90: # 80-89
            output += 6 + numLen(integer-80)
        else:                # 90-99
            output += 6 + numLen(integer-90)
    elif length is 3:
        if integer % 100 is not 0:
            output += 3 # Add an "and"
        if integer < 200:
            output += 3 + 7 + numLen(integer-100)
        elif integer < 300:
            output += 3 + 7 + numLen(integer-200)
        elif integer < 400:
            output += 5 + 7 + numLen(integer-300)
        elif integer < 500:
            output += 4 + 7 + numLen(integer-400)
        elif integer < 600:
            output += 4 + 7 + numLen(integer-500)
        elif integer < 700:
            output += 3 + 7 + numLen(integer-600)
        elif integer < 800:
            output += 5 + 7 + numLen(integer-700)
        elif integer < 900:
            output += 5 + 7 + numLen(integer-800)
        elif integer < 1000:
            output += 4 + 7 + numLen(integer-900)
    elif length is 4:
        output += 3 + 8

    print array,"has",output,"numbers"
    return output

start = clock()
sum = 0
for i in range(1001):
    sum += numLen(i)
end = clock()

print "The result is", sum
print "This computation took",end-start,"seconds"
