"""
********* Euler Problem 12 *********
PROMPT:
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""
n = 999999
count = 1
maxcount = 1
maxn = n
while n > 500000:
    nt = n
    while nt != 1:
        if nt % 2 == 0:
            nt = nt/2
        else:
            nt = 3*nt + 1
        count += 1
    if count > maxcount:
        maxcount = count
        maxn = n
    count = 1
    n -= 1

print(maxcount)
print(maxn)
