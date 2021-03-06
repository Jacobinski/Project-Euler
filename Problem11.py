# This is the 11th problem for Project Euler
# We need to find the largest product of 4 adjacent (diagonal/vertical/horizontal) numbers
# in the array given below. Indices will be 1-indexed if we attempt to look at the 
# position from the 'index1' 'index2' variables. 

from time import clock
start = clock()

M = []
M.append("08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08")
M.append("49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00")
M.append("81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65")
M.append("52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91")
M.append("22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80")
M.append("24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50")
M.append("32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70")
M.append("67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21")
M.append("24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72")
M.append("21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95")
M.append("78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92")
M.append("16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57")
M.append("86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58")
M.append("19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40")
M.append("04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66")
M.append("88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69")
M.append("04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36")
M.append("20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16")
M.append("20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54")
M.append("01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48")

# Modify the array to get individual elements
size = len(M)
for i in range(size):
    M[i] =[int(n) for n in M[i].split()]

# Get variables
sum = 0 # The current largest product
direction = '' # The current direction. right, down, diag right, diag left
index1 = 0 # First matrix index
index2 = 0 # Second matrix index

for i in range(size):
    for j in range(size):
       # Compute the right product
       if i < 17:
           r = M[i][j] * M[i+1][j] * M[i+2][j] * M[i+3][j] # Right product
           if r > sum:
               sum = r
               direction = 'r'
               index1 = i+1
               index2 = j+1
       # Compute the down product
       if j < 17:
           d = M[i][j] * M[i][j+1] * M[i][j+2] * M[i][j+3] # Down product
           if d > sum:
               sum = d
               direction = 'd'
               index1 = i+1
               index2 = j+1
       # Compute the diagonal right / product
       if i < 17 and j < 17:
           dr = M[i][j] * M[i+1][j+1] * M[i+2][j+2] * M[i+3][j+3] # Diagonal product
           if dr > sum:
               sum = dr
               direction = 'dr'
               index1 = i+1
               index2 = j+1
       # Compute the diagonal left \ product
       if i > 4 and j < 17:
           dl = M[i][j] * M[i-1][j+1] * M[i-2][j+2] * M[i-3][j+3]
           if dl > sum:
               sum = dl
               direction = 'dl'
               index1 = i+1
               index2 = j+1

end = clock()

print('The largest sum is {}'.format(sum))
print('This computation took {} seconds'.format(end-start))
