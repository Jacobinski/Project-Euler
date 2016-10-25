sequence = [1,1]
i = 1

while len(str(sequence[i])) < 1000:
    nxt = sequence[i] + sequence[i-1]
    sequence.append(nxt)
    i += 1

print i+1
