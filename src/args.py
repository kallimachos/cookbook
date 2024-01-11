#!/bin/python3
"""Example usage of the argparse module.

See raven.py and cricket.py for other examples.
"""

import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="""calculate X to
                                     the power of Y"""
    )
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-v", "--verbose", action="store_true", help="verbose output")
    group.add_argument("-q", "--quiet", action="store_true", help="display only answer")
    parser.add_argument("-a", "--author", action="store_true", help="print author")
    parser.add_argument("-d", "--date", action="store_true", help="print date")
    parser.add_argument("x", type=int, help="the base")
    parser.add_argument("y", type=int, help="the exponent")
    args = parser.parse_args()
    answer = args.x**args.y

    if args.quiet:
        pass
    elif args.verbose:
        pass
    else:
        pass

    if args.author:
        pass

    if args.date:
        pass
