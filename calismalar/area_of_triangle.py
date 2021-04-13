
def calculate_triangle_area(base, height):
    area = (base * height) / 2
    return f'Area of the triangle: {area}'
fillchar_len = 100
print(f'''
{'=' * fillchar_len}
{'AREA OF A TRIANGLE '.center(fillchar_len)}
{'=' * fillchar_len}
This program calculates the area of a triangle.

->Please enter a number.
->Enter 0 (Zero) to exit.
{'-' * fillchar_len}
{'Enter the Values'.center(fillchar_len, '-')}''')

while True:
    print('Please enter the base of the triangle: ')

    try:
        base = int(input('>>>'))
        if base == 0:
            break
    except:
        print('Please enter a valid number!')
        continue
    print('Please enter the height of the triangle: ')

    try:
        height = int(input('>>>'))
        if height == 0:
            break
    except:
        print('Please enter a valid number!')
        continue
    print(calculate_triangle_area(height, base))
    print('-' * fillchar_len)

exit('Exiting...')