#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastd = number % 10 if number >= 0 else (abs(number) % 10) * -1
if lastd > 5:
    result = "and is greater than 5"
elif lastd == 0:
    result = "and is 0"
elif lastd < 6:
    result = "and is less than 6 and not 0"
print("Last digit of {:d} is {:d}".format(number, lastd), result)
