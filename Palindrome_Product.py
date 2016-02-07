from time import clock

start = clock()

a = 99
b = 99
found = False

def isPalindrome(num):
    strNum = str(num)
    length = len(strNum)
    if length % 2 == 0:
        start = strNum[:length//2]
        end = strNum[-length//2:]
    else:
        start = strNum[:length//2]
        end = strNum[-length//2+1:]
    end = end[::-1]  # Reverse
    if start == end:
        return True
    else: 
        return False

while (found != True):
    check = a * b;
    if isPalindrome(check):
        print('a =',a,'b =',b,'Product =',check)
        found = True;
    elif (a-1)*b > a*(b-1):
        a = a - 1
    else:
        b = b - 1       

end = clock()
print(end-start)