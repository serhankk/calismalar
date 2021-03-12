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
    return stdev, average