"""
********* Euler Problem 10 *********
PROMPT:
Find the sum of all the primes below two million.

"""

# Use Sieve of Eratosthenes

# Create list of bools up to n
n = 2000000
primes = [True for i in range(n)]
total = 0 
p = 2 # start at the first prime number, 2

# Iterate up to the square root of n
while p * p < n:
    # if the bool for that number is True, it is a prime
    if primes[p] == True:
        # eliminate all multiples of the prime up to n
        for i in range(p*p,n,p):
            primes[i] = False
    p+=1

# from 2 to n, if the bool for that number is True, add to total
for p in range(2,n):
    if primes[p]:
        total += p

print(total)