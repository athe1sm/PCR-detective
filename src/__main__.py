#!/usr/bin/env python

"""
Command line interface to readfile
"""

# Potential code below. Will need to be changed

import argparse

def parse_command_line():
    "parses args for the readfile funtion"

    # init parser and add arguments
    parser = argparse.ArgumentParser()

    # add long args
    parser.add_argument(
        "--clean",
        help="cleans .fasta file",
        action="store_true")


def main():
    "run main function on parsed args"

    # get arguments from command line as a dict-like object
    args = parse_command_line()

    # add if arguments
