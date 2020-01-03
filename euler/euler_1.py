"""
********* Euler Problem 1 *********
PROMPT:
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.

"""

# import libraries
import math
import numpy as np

# set up variables
count = 1
total = 0

while count < 1000:
    div3 = count % 3
    div5 = count % 5
    if div3 == 0 or div5 == 0:
        total += count
    count += 1

print(total)
