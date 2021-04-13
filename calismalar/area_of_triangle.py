
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
{'=' * fillchar_len}
{'Enter the Numbers'.center(fillchar_len)}
{'-' * fillchar_len}''')
while True:
    print('Please enter the base of the triangle: ')
    base = int(input('>>>'))

    print('Please enter the height of the triangle: ')
    height = int(input('>>>'))

    if base == 0 or height == 0:
        break
    print(calculate_triangle_area(height, base))

exit('Exiting...')