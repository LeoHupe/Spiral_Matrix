import numpy as np

size = int(input("Size of matrix ? "))
Spiral = [0] * size**2

# Initial value for instructions
instructions  = [1] * (size - 1) 
instructions += [size] * (size - 1) 
instructions += [-1] * (size - 1)

options = np.array([-size, 1])

for multiplier in range(size - 2, 0, -1):
    for i in range(2):
        instructions += [options[i]] * multiplier
    options *= -1

# Adding 0 so it doesn't change instructions but list length equals size^2
instructions += [0]

b 
for num, instruction in zip(range(1, size**2 + 1), instructions):

    Spiral[index] = num
 

Output = ""
for x in range(size**2):

    # Adds a new line so a square is printed
    if x % size == 0:
        Output += "\n" 

    Number = f"{size**2}" # Biggest number in spiral

    Digits = len(Number) # Number of digits in biggest number

    # Fills left of number with 0s, so every number in spiral has equal length
    Output += f"{Spiral[x]}".zfill(Digits)
    Output += " "
    
print(Output)

"""
How algorithm works

Spiral of size 4:

 1  2  3  4
12 13 14  5
11 16 15  6
10  9  8  7

Looking at indexes in order:

0 1 2 3 7 11 15 14 13 12 8 4 5 6 10 9

Looking at how indexes change:
+1 +1 +1 +4 +4 +4 -1 -1 -1 -4 -4 +1 +1 +4 -1

Organizing the pattern of how indexes change for implementation:

3 x 1
3 x 4
3 x -1

2 x -4
2 x 1

1 x 4
1 x -1

"""
