"""
********* Euler Problem 15 *********
PROMPT:
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
How many such routes are there through a 20×20 grid?

"""

n = 20
paths = 1

for i in range(0,n):
    paths *= (2*n)-i
    paths /= (i + 1)

print(paths)