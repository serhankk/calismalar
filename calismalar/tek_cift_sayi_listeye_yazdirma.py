def seperate_odd_even_numbers(*iterable):
    odd_numbers = []
    even_numbers = []
    for number in iterable:
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            odd_numbers.append(number)
    return f'Odd Numbers:  {odd_numbers}\nEven Numbers: {even_numbers}'