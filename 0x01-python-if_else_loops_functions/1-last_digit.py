#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    m = ((number * - 1) % 10) * -1
else:
    m = (number % 10)

if m > 5:
    print(f"Last digit of {number:d} is {m:d} and is greater than 5")
elif m == 0:
    print(f"Last digit of {number:d} is {m:d} and is 0")
else:
    print(f"Last digit of {number:d} is {m:d} and is less than 6 and not 0")
