
def the_biggest_number(first_number, second_number, third_number):
    the_biggest_one = 'The biggest number is: '
    if first_number > second_number:
        if first_number > third_number:
            return the_biggest_one + str(first_number)
        else:
            return the_biggest_one + str(third_number)
    elif second_number > first_number:
        if second_number > third_number:
            return the_biggest_one + str(second_number)
        else:
            return the_biggest_one + str(third_number)
    else:
        return the_biggest_one + str(third_number)
