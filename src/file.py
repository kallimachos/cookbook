#!/bin/python3
"""Read input from command line and write it to a file."""

from os import path, remove


def createfile(file, text):
    """Create a file, write to it, read it."""
    with open(file, "w") as f:
        f.write(text)
    with open(file) as f:
        return f.read()


def test_createfile() -> None:
    """Test createfile method."""
    assert createfile("example.txt", "hi") == "hi"


def test_cleanup() -> None:
    """Remove example.txt file."""
    if path.exists("example.txt"):
        remove("example.txt")
    assert True is True


if __name__ == "__main__":
    text = input("Enter some text: ")
