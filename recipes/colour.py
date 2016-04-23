#!/bin/python3
"""Escape codes for coloured console output."""

purple = '\033[95m'
blue = '\033[94m'
green = '\033[92m'
yellow = '\033[93m'
red = '\033[91m'
end = '\033[0m'

if __name__ == '__main__':
    print("Hello! " + purple + 'This ' + blue + 'is ' + green + 'an ' +
          yellow + 'example ' + red + 'sentence. ' + end + 'Hooray!')
