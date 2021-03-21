#!/usr/bin/env python
from readfile import read_file
import Bio
#seq_tuple=readfile
class cleanup:
    def __init__(self,seq_tuple=read_file().readfile(),temptype='DNA',autoclean=0):
        #self.seq_tuple=seq_tuple
        self.seq_zip = zip(seq_tuple[0],seq_tuple[1])
        self.temptype = temptype
        

    def check_base(self):
        "check the base in the sequences and raise warnings"
        #for pairs in self.seq_zip:

        pass

    def change_base(self):
        "change the Ts and Us in the RNA or DNA sequence"
        pass

    def clean_up(self):
        "the main function that returns a dictionary of sequences"
        self.check_base()
        self.change_base()
        return 0

if __name__== '__main__':
    print(cleanup().clean_up())