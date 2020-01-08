"""
********* Euler Problem 4 *********
PROMPT:
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

"""

# Import libraries
import math
import numpy as np 

# Maximum possible number is 999*999
maxn = 999*999
# Minimum possible number is 100*100
minn = 100*100

# Initialize variables
x = maxn
found = False # bool to check if we should keep looking for palindromes
trips = list(range(100,1000))[::-1] # list of all 3 digit numbers

## Find palindromes
# while greater than the lowest product desired and not found yet
while x >= minn and not found:
    # if a palindrome and has at least two factors of triple digits
    if str(x) == str(x)[::-1] and \
    len([i for i, val in enumerate(list(x % q == 0 for q in trips)) if val]) >= 2:
        # find the 3-digit factors of the palindrome
        indices = [i for i, val in enumerate(list(x % q == 0 for q in trips)) if val]
        factors = [trips[i] for i in indices]
        # check if the quotient of x/factor[i] is 3-digits
        if max(x / p >= 100 and x / p <= 999 for p in factors):
            print(x)
            # filter out where x/factor[i] is not 3-digits
            idx = [i for i, val in enumerate(list(x / p >= 100 and x / p <= 999 for p in factors)) if val]
            print([factors[i] for i in idx])
            # break the loop
            found = True
    x -= 1

# Note: had originally considered the easier approach of checking if
# divisible by 990-999 and got the same answer. This approach was more robust.