from fractions import Fraction

topMultiply = 1
botMultiply = 1

for bot in range(1,100):
    for top in range(1,bot): # Ensure top/bot < 1
        topSet = set([int(i) for i in str(top)])
        botSet = set([int(i) for i in str(bot)])
        common = topSet & botSet
        if len(common) is 1: # One matching element
            topNum = topSet - common
            botNum = botSet - common
            # Note: The copy function is used as we want to avoid popping topNum & common together
            if len(topNum) is 0:
                topNum = common.copy() # In case we have 44/49 -> 0/9
            if len(botNum) is 0:
                botNum = common.copy()
            # Assume 1 element in topNum & botNum
            topNum = topNum.pop()
            botNum = botNum.pop()
            common = common.pop()
            if botNum != 0 and topNum != 0 and common != 0 and (float(topNum)/float(botNum) == float(top)/float(bot)):
                topMultiply *= top
                botMultiply *= bot

print "The answer is",Fraction(topMultiply,botMultiply)
