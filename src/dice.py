#!/bin/python

from random import randint


def spread(low, high, reps):
    above = 0
    below = 0
    for _x in range(reps):
        num = randint(low, high)
        if num > 10:
            above += 1
        else:
            below += 1
    return (above, below)


if __name__ == "__main__":
    reps = 1000
    # d20
    low = 1
    high = 20
    d20 = spread(low, high, reps)
    # d18
    low = 3
    high = 18
    d18 = spread(low, high, reps)
