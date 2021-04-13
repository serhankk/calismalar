#!/usr/bin/python3

def greatest_common_divisor(first_number, second_number):
    if first_number >= second_number:
        the_biggest_number = first_number
    else:
        the_biggest_number = second_number

    common_divisors = []
    for number in range(1, the_biggest_number):
        if (first_number % number == 0) and (second_number % number == 0):
            common_divisors.append(number)
    max_common_divisor = max(common_divisors)
    return max_common_divisor
fillchar_len = 100

print(f'''
{'=' * fillchar_len}
{'GREATEST COMMON DIVISOR CALCULATOR'.center(fillchar_len)}
{'=' * fillchar_len}
This program calculates the GCD of a given two number.

->Please enter only numbers.
->Type 0 (Zero) to exit.
{'-' * fillchar_len}''')
while True:
    try:
        print('Enter the first number:')
        first_int = int(input('>>>'))
        if first_int == 0:
            exit('Exiting...')
        print('Enter the second number:')
        second_int = int(input('>>>'))
        if second_int == 0:
            exit('Exiting...')
        print(greatest_common_divisor(first_int, second_int))
    except ValueError:
        print('Please enter a valid number!')
