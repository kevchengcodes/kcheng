"""
********* Euler Problem 7 *********
PROMPT:
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
we can see that the 6th prime is 13.

What is the 10 001st prime number?

"""

import math

# Initialize set of prime numbers
primes = (2,3,5,7,11)
n = 13 # start with the next prime

while len(primes) < 10001:
    # primes up to this scale will have a remainder of 1 or 5 when divided by 6
    r = n % 6
    if (r == 1 or r == 5):
        # only need to look up to the sq root of n
        nsq = math.sqrt(n)
        sqprimes = [t for t in primes if t <= nsq]
        # if not divisible by any of the primes < sqrt(n), then add to tuple
        if not max(n % x == 0 for x in sqprimes):
            primes += (n,)
    n+=2

print(primes[len(primes)-1])