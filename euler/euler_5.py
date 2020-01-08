"""
********* Euler Problem 5 *********
PROMPT:
2520 is the smallest number that can be divided by each of the numbers from 
1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible 
by all of the numbers from 1 to 20?

"""

# Initialize variables
n = 2520 # start at the given smallest number
# only need to check the largest multiples of 2 or prime numbers
# for EX: if divisible by 16, it's divisible by 4 and 8
mults = [11,12,13,14,16,17,18,19,20] # [1,2,3,4,5,6,7,8,9,10]
found = False

# Iterate up by 20 until found
while not found and n < 10e8:
    if all(n % x == 0 for x in mults):
        print(n)
        found = True
    n += 20