#!/bin/python

#===========================================================
# Argparse
#-----------------------------------------------------------
import argparse

parser = argparse.ArgumentParser(description="calculate X to the power of Y")
group = parser.add_mutually_exclusive_group()
group.add_argument("-v", "--verbose", action="store_true")
group.add_argument("-q", "--quiet", action="store_true")
parser.add_argument("x", type=int, help="the base")
parser.add_argument("y", type=int, help="the exponent")
args = parser.parse_args()
answer = args.x**args.y

if args.quiet:
    print(answer)
elif args.verbose:
    print("{0} to the power {1} equals {2}".format(args.x, args.y, answer))
else:
    print("{0}^{1} == {2}".format(args.x, args.y, answer))