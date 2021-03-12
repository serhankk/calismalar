
def perfect_numbers(number):
    divisors = []
    for i in range(1, number):
        if number % i == 0:
            divisors.append(i)
    if sum(divisors) == number:
        return f'{number} is a perfect number.'
    else:
        return f'{number} is not a perfect number.'
