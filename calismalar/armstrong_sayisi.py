
def armstrong_number(number):
    digit = len(number)
    
    total = 0
    for i in range(digit):
        total += int(number[i]) ** digit
    
    if total == int(number):
        return f'{number} is an Armstrong number.'
    else:
        return f'{number} is not an Armstrong number.'
fillchar_len = 100
print(f'''
{'=' * fillchar_len}
{'IS ARMSTRONG?'.center(fillchar_len)}
{'=' * fillchar_len}

This program calculates if given number is an Armstrong number or not.
->Enter one number at a time.
->Enter an integer number.
->Some invalid inputs: [-5, 10.4, -2.5, two, ' '(space)]

->Press "q" to exit.
{'-' * fillchar_len}
Please enter the number:''')
while True:
    try:
        number = (input('>>>'))
        if number == 'q' or number == 'Q':
            break

        elif (number.__contains__('.')) and (number.__contains__('-')):
            print('Please enter a positive integer number!')
            continue

        elif number.__contains__('.'):
            print('Please enter an integer number!')
            continue

        elif number.__contains__('-'):
            print('Please enter a positive number!')

        else:
            print(armstrong_number(number))
    except ValueError:
        print('Please enter a valid number!')
        continue


exit('Exiting...')