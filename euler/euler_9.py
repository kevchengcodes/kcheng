"""
********* Euler Problem 9 *********
PROMPT:
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

"""

# Use Euclid's formula to find a, b, and c
# a = k * (m^2-n^2)
# b = k * (2mn)
# c = k * (m^2+n^2)
# where m > n > 0 and are integers

# start with smallest possible Pythagorean triple: a=3,b=4,c=5
n = 1
m = 2
# keep k at 1, since 3+4+5=12, and is not a factor of 1000

found = False
# Iterate through n and m by 1 until a+b+c = 1000 is found
while n < 100 and not found:
    m = n+1
    while m < 100 and not found:
        a = m**2-n**2
        b = 2*m*n
        c = m**2+n**2
        if a+b+c == 1000:
            print([a,b,c])
            print([n,m])
            print(a*b*c)
            found = True
        m += 1
    n += 1
