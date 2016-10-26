maxRep = 0
maxNumber = 0

for num in range(2,1000+1):
    # Numbers that are mod(5) or mod(2) will never repeat
    if num % 2 == 0 or num % 5 == 0:
        continue
    # Emulate long divison
    else:
        mods = []
        reps = 0 # Length
        div = 1  # Divisor
        while div < num:
            div *= 10
        # Do one cycle loop
        mods.append(div % num)
        reps += 1
        div = div % num
        # Repeat
        while div is not 1:
            div *= 10
            reps += 1
            mods.append(div % num)
            div = div % num
        if reps > maxRep:
            maxRep = reps
            maxNumber = num

print maxRep
print maxNumber
