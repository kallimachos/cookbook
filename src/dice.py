#!/bin/python

from random import randint


def spread(low, high, reps):
    above = sum(1 for _ in range(reps) if randint(low, high) > 10)
    below = reps - above
    return above, below


if __name__ == "__main__":
    d20 = spread(1, 20, 1000)
    d18 = spread(3, 18, 1000)
    print(f"d20: {d20[0]} above, {d20[1]} below")
    print(f"d18: {d18[0]} above, {d18[1]} below")
