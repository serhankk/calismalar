def are_friend_numbers(number1, number2):
    number1_total = 0
    number2_total = 0

    number1_divisors = []
    number2_divisors = []
    for number in range(1, number1):
        if (number1 % number == 0):
            number1_divisors.append(number)
    for divisor in number1_divisors:
        number1_total += divisor

    for number in range(1, number2):
        if (number2 % number == 0):
            number2_divisors.append(number)
    for divisor in number2_divisors:
        number2_total += divisor

    if (number1_total == number2) and (number2_total == number1):
        return 'Friend Number!'
    else:
        return 'Not Friend Number!'
fillchar_len = 100
print(f'''
{'=' * fillchar_len}
ARE FRIEND NUMBERS?
{'=' * fillchar_len}
Friendly numbers are two or more natural numbers 
with a common abundancy index, the ratio between 
the sum of divisors of a number and the number itself.

-> 
{'Enter the numbers'.center(fillchar_len)}''')

while True:
    number1 = int(input('>>>'))
    number2 = int(input('>>>'))

    print(are_friend_numbers(220,284))

    # DEVAM EDECEK