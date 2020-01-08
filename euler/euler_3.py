"""
********* Euler Problem 3 *********
PROMPT:
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

"""
# Import libraries
import math

# Set variables
x = 600851475143
xsq = math.floor(math.sqrt(x))
primes = (3,) # initialize tuple of prime factors

# Loop and find all prime factors
n = 5
while n < xsq:
    if x % n == 0 and not max(n % x == 0 for x in primes):
        # if n is a factor of x, and is not divisible by a smaller prime number:
        primes += (n,) # store all prime factors in a tuple
    n += 2 # only need to look at odd numbers

print(max(primes))  
