#!/bin/python3
"""Read input from command line and write it to a file."""

readme = input("Enter some text: ")
with open('example.txt', 'w') as f:
    f.write(readme)
