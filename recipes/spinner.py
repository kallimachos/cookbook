#!/bin/python3
# -*- coding: utf-8 -*-
"""Example usage of the yaspin module."""

from time import sleep

from yaspin import yaspin

if __name__ == '__main__':
    with yaspin(text="Iterating", color="green") as spinner:
        sleep(5)
    spinner.ok()
