from math import floor
from time import clock

start = clock()
month = 1 # January
day = 0 # Tuesday - Sunday is 5 
year = 1901
end = 2001
sunday = 0

while year < end:
    if day % 7 is 5:
        sunday += 1
    if month in [1,3,5,7,8,10]:
        day += 31
        month += 1
    elif month is 2:
        day += 28
        month += 1
        if year % 4 is 0:
            if year % 100 is not 0:
                day += 1 # Leap year
            elif year % 100 is 0 and year % 400 is 0:
                day += 1 # Leap year
    elif month is 12:
        day += 31
        month = 1
        year += 1
    else: # 30 day months
        day += 30
        month += 1

end = clock()
print "There are",sunday,"Sundays"
print "This computation took",end-start,"seconds"
