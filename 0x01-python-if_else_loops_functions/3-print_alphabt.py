#!/usr/bin/python3
for letter in range(97, 123):
    if letter == ord('q') or letter == ord('e'):
        continue
    print("{:c}".format(letter), end='')
