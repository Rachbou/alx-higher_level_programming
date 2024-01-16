#!/usr/bin/python3
def fizzbuzz():
    for number in range(1, 101):
        fizz = number % 3
        buzz = number % 5
        if fizz == 0:
            print("Fizz", end='')
        if buzz == 0:
            print("Buzz", end='')
        if fizz != 0 and buzz != 0:
            print(number, end='')
        print(' ', end='')
