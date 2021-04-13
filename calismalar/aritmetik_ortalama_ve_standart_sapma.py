from math import sqrt
def get_stdev(iterable):
    total = 0
    count = 0
    for i in iterable:
        total += i
        count += 1
    average = total / count

    total = 0
    for i in iterable:
        total += (i - average) ** 2
    stdev = sqrt(total / (count - 1))
    return f'Standard Deviation: {stdev} | Average: {average}'

def intro(title):
    fillchar_len = 75
    print('=' * fillchar_len)
    print(str(title).center(fillchar_len).upper())
    print('=' * fillchar_len)
    description = '''This program calculates the standard deviation and average of given numbers.
You should only enter numbers. 
    
->Enter 1 number at a time.
->Press "q" to end the entering number.'''
    print(description)
    print('=' * fillchar_len)
    print('Enter the numbers'.center(fillchar_len))
    print('-' * fillchar_len)


numbers_list = []
result = 0

intro('Standard Deviation Calculator')
while True:
    numbers = input('>>>')
    if numbers == 'q':
        break
    else:
        try:
            if numbers.__contains__('.'):
                numbers_list.append(float(numbers))
            else:
                numbers_list.append(int(numbers))
        except:
            print('Please enter a valid number.')
            continue


standard_deviation = get_stdev(numbers_list)
print(f'Entered numbers: {numbers_list}')
print(standard_deviation)