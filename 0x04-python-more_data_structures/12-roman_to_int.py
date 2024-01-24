#!/usr/bin/python3
def roman_to_int(roman_string):
    if (not roman_string) or (not isinstance(roman_string, str)):
        return (0)
    roman_numbers = {'I': 1,
                     'V': 5,
                     'X': 10,
                     'L': 50,
                     'C': 100,
                     'D': 500,
                     'M': 1000}
    roman_number = 0
    for i in range(len(roman_string)-1):
        if roman_numbers[roman_string[i]] < roman_numbers[roman_string[i + 1]]:
            roman_number -= roman_numbers[roman_string[i]]
        else:
            roman_number += roman_numbers[roman_string[i]]
    roman_number += roman_numbers[roman_string[len(roman_string)-1]]
    return (roman_number)
