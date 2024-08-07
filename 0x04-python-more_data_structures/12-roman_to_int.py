#!/usr/bin/python3
def roman_to_int(roman_string):
    """Coverts a roman number to an integer.

    """
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
            }

    num = 0
    prev = 0
    for char in roman_string:
        # Check if char is a valid roman numeral
        if char not in roman_dict:
            return 0

        # Get the integer value for the current character
        current = roman_dict[char]

        # Handle the subtractive notation (IV, XL, XC, CD, CM)
        if current > prev:
            num += current - prev # Subtract previous value if larger
            prev = 0 # Reset previous value
        else:
            num += current # Add current value
            prev = current # Update previous value

    return num
