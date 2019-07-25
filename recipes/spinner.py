#!/bin/python3
# -*- coding: utf-8 -*-
"""Example usage of the yaspin module."""

import logging
from time import sleep

from yaspin import yaspin

if __name__ == "__main__":
    with yaspin(text="Iterating", color="green") as spinner:
        sleep(2)
        spinner.write("A message of great importance")
        spinner.hide()
        logging.error("hi, this is an error")
        spinner.show()
        spinner.text = "Still iterating"
        sleep(2)
    spinner.ok()
