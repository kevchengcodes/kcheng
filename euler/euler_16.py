"""
********* Euler Problem 16 *********
PROMPT:
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?

"""

number = 2**1000
string = str(number)
total = 0
for i in string:
    total += int(i)
print(total)