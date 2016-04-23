#!/bin/python3
"""Example usage of the tqdm module to create a progressbar."""

from time import sleep
from tqdm import tqdm

for i in tqdm(range(500)):
    sleep(0.005)
