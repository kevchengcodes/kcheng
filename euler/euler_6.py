"""
********* Euler Problem 6 *********
PROMPT:
Find the difference between the sum of the squares of the 
first one hundred natural numbers and the square of the sum.

"""

hundo = list(range(1,101))

sums = sum(hundo)

sqsum = sums**2

sumsq = sum(x**2 for x in hundo)

answer = sqsum-sumsq

print(answer)