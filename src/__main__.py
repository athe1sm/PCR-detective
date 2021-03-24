#!/usr/bin/env python

"""
Command line interface to readfile
"""

# Potential code below. Will need to be changed

import argparse
# add import statement for readfile.py
from readfile import read_file

def parse_command_line():
    "parses args for the readfile funtion"

    # init parser and add arguments
    parser = argparse.ArgumentParser()

    # add long args
    parser.add_argument(
        "--clean",
        help="cleans .fasta file",
        action="store_true")

    # add arg to take in file path location

    args = parser.parse_args()


def main():
    "run main function on parsed args"

    # get arguments from command line as a dict-like object
    args = parse_command_line()

    # add if arguments here for read_file()
    if args.clean:
        seq1 = read_file()
        print(seq1.readfile())
        # cleanup(), add when cleanup.py is ready


if __name__ == "__main__":
    seq1 = read_file()
    print(seq1.readfile())

