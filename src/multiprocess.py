#!/usr/bin/env python3
"""Mulitprocessing example."""

from multiprocessing import Process


def func1() -> None:
    """Do func1."""
    rocket = 0
    while rocket < 100000000:
        rocket += 1


def func2() -> None:
    """Do func2."""
    rocket = 0
    while rocket < 100000000:
        rocket += 1


if __name__ == "__main__":
    p1 = Process(target=func1).start()
    p2 = Process(target=func2).start()
