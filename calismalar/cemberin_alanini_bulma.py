from math import pi
def area_of_circle(radius):
    area = pi * (radius ** 2)
    return f'Area of the circle: {area} cm²'

fillchar_len = 100
print(f'''
{'=' * fillchar_len}
{'AREA OF A CIRCLE'.center(fillchar_len)}
{'=' * fillchar_len}
This program calculates area of a circle by given the radius value.

->Please enter a number.
->Type 0 (Zero) to exit.
{'-' * fillchar_len}
Enter the radius value: ''')
while True:
    try:
        radius = float(input('>>>'))
        if radius == 0:
            break
    except ValueError:
        print('Please enter a number!')
        continue

    print(area_of_circle(radius))
print('=' * fillchar_len)
exit('Exiting...')