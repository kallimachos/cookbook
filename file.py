#!/bin/python3

# gets input and writes it to a file

readme = input("Enter some text: ")
with open('example.txt', 'w') as f:
    f.write(readme)
