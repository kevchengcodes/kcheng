"""
********* Euler Problem 17 *********
PROMPT:
If the numbers 1 to 5 are written out in words:
one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in
words, how many letters would be used?


NOTE: Do not count spaces or hyphens.
For example, 342 (three hundred and forty-two) contains 23 letters and
115 (one hundred and fifteen) contains 20 letters.
The use of "and" when writing out numbers is in compliance with British usage.

"""

# Create function that maps an integer to its number of letters 
# using a dictionary.
def numtostr(x, n):
    if n == 1:  # 1-19
        switcher = {
            0: 0,
            1: 3,
            2: 3,
            3: 5,
            4: 4,
            5: 4,
            6: 3,
            7: 5,
            8: 5,
            9: 4,
            10: 3,
            11: 6,
            12: 6,
            13: 8,
            14: 8,
            15: 7,
            16: 7,
            17: 9,
            18: 8,
            19: 8
        }
        return switcher.get(x, "not a number bruv")
    else: # number of letters for "twenty", "thirty", etc.
        switcher = {
            2: 6,
            3: 6,
            4: 5,
            5: 5,
            6: 5,
            7: 7,
            8: 6,
            9: 6
        }
        return switcher.get(int(str(x)[0]), "not a number bruv")

# Loop through each number and use numtostr
total = 0
for i in range(1,1000):
    # 1-20 are unique numbers
    if i < 20:
        num = numtostr(i, 1)
    # 21 - 99 use a prefix such as ninety, then a 1-9 # following it
    elif i < 100:
        num = numtostr(i, 2)+numtostr(int(str(i)[1]), 1)
    # 100-999 contains a "x" hundred, with a potential "and"
    else:
        # trail = the last two digits of the number
        trail = int(str(i)[1:])
        # Calculate an interim number for the trail using identical process
        # as above (1-20 vs 21-99)
        if trail < 20:
            inum = numtostr(trail, 1)
        else:
            inum = numtostr(trail, 2)+numtostr(int(str(trail)[1]), 1)
        # if trail = 0, it means it is a multiple of 100
        # multiples of 100 will not have an "and". "hundred" is 7 letters
        if trail == 0:
            prep = 7
        else:
            prep = 10
        # sum up the first digit numtostr with prep and the trail numtostr
        num = numtostr(int(str(i)[0]), 1) + prep + inum
    total += num
total += 11 # one thousand = 11 letters

print(total)
