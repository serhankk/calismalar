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
