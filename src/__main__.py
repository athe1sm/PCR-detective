#!/usr/bin/env python3

"""
Command line interface to run PCR-detective
"""

# Potential code below. Will need to be changed

import argparse
# add import statement for readfile.py
from src.readfile import Read_file
from src.cleanup import Cleanup
from src.SmithWaterman import match, Scoring
from src.matchmaker import Matchmaker
import os

def parse_command_line():
    "parses args for the readfile funtion"

    # init parser and add arguments
    parser = argparse.ArgumentParser()

    parser.add_argument(
        'filepath',
        type=str,
        help='specify the path of the sequence file'
    )

    parser.add_argument(
        'temptype',
        type=str,
        help='input DNA or RNA for the template type'
    )

    parser.add_argument(
        'output',
        type=str,
        help='name the output filename'
    )
    # add long args
    parser.add_argument(
        "--clean",
        help="autocleans .fasta file",
        action="store_true")

    

    # add arg to take in file path location

    args = parser.parse_args()
    return args


def main():
    "run main function on parsed args"

    # get arguments from command line as a dict-like object
    args = parse_command_line()

    # add if arguments here for read_file()


    outputpath = os.getcwd()+'/output'
    if not os.path.exists(outputpath):
        os.makedirs(outputpath)
    doutput = outputpath + '/' + args.output + '.txt'
    if os.path.isfile(doutput):
        n=0
        while 1:
            n += 1
            noutput = doutput[:-4] + "(" + str(n) + ").txt"
            if not os.path.isfile(noutput):
                break
        fp = noutput
    else:
        fp = doutput
    
    res = Cleanup(seq_tuple=args.filepath,
        temptype=args.temptype,
        output=fp,
        autoclean=args.clean).clean_up()

    file = open(fp,'a')
    
    file.write(Matchmaker(list(res)).run())
    file.close
    
    
    
    print(list(res))
        # cleanup(), add when cleanup.py is ready


