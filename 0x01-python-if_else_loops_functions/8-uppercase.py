#!/usr/bin/python3
def uppercase(str):
    for c in str + '\n':
        if ord(c) >= ord('a') and ord(c) <= ord('z'):
            print("{:c}".format(ord(c) - 32), end='')
        else:
            print("{:s}".format(c), end='')
