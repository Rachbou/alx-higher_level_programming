#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
L = abs(number) % 10
if number < 0:
    L = -(L)
if L > 5:
    print(f"Last digit of {number:d} is {L:d} and is greater than 5")
elif L == 0:
    print(f"Last digit of {number:d} is {L:d} and is 0")
else:
    print(f"Last digit of {number:d} is {L:d} and is less than 6 and not 0")
