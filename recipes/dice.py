#!/bin/python

from random import randint


def spread(low, high, reps):
    above = 0
    below = 0
    for x in range(reps):
        num = randint(low, high)
        if num > 10:
            above +=1
        else:
            below +=1
    return(above, below)


if __name__ == '__main__':
    reps = 1000
    # d20
    low = 1
    high = 20
    d20 = spread(low, high, reps)
    print("D20\nAbove: " + str(d20[0]))
    print("D20\nBelow: " + str(d20[1]))
    # d18
    low = 3
    high = 18
    d18 = spread(low, high, reps)
    print("D18\nAbove: " + str(d18[0]))
    print("D18\nBelow: " + str(d18[1]))
