#!/bin/python3
"""Print unicode characters safely. This may only be relevant to Python 2."""

import codecs
import os
import sys


def safe_print(text):
    """
    Print text to the terminal, regardless of the OS.

    Uses sys.stdout plus the codecs module to enforce UTF-8.
    """
    if os.name == 'nt':     # Windows
        codec = codecs.lookup('cp437')
    else:                   # Mac / Linux
        codec = codecs.lookup('utf8')
    wrapped_stdout = codec.streamwriter(sys.stdout, errors='replace')
    wrapped_stdout.write(text)
    wrapped_stdout.write('\n')


def test_safe_print():
    """Unicode test cases to ensure that safe_print works on your platform."""
    safe_print(u'☂☀♠')
