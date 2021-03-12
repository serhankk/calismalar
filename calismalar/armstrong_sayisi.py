
def armstrong_number(number):
    digit = len(number)
    
    total = 0
    for i in range(digit):
        total += int(number[i]) ** digit
    
    if total == int(number):
        return f'{number} is an Armstrong number.'
    else:
        return f'{number} is not an Armstrong number.'
