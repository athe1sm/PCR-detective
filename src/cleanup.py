#!/usr/bin/env python
from readfile import read_file
from Bio.Seq import Seq
#seq_tuple=readfile
class cleanup:
    def __init__(self,seq_tuple=read_file("/home/athe1sm/hacks/PCR-detective/data/sequence.fasta").readfile(),temptype='DNA',autoclean=0):
        #self.seq_tuple=seq_tuple
        self.seq_zip = zip(seq_tuple[0],seq_tuple[1])
        self.temptype = temptype
        self.autoclean = autoclean 
        print(list(self.seq_zip))
        

    def check_base(self):
        "check the base in the sequences and raise warnings"
        for pairs in self.seq_zip:
            if 'primer' in pairs[0]:
                if 'U' in pairs[1]:
                    raise Exception('Urasils are not expected in DNA primers')
            elif self.temptype == 'DNA' and 'templet' in pairs[0]:
                if 'U' in pairs[1]:
                    raise Exception('Urasils are not expected in DNA templets')
            elif self.temptype == 'RNA' and 'templet' in pairs[0]:
                if 'T' in pairs[1]:
                    raise Exception('Thymines are not expected in RNA templets')

    def change_base(self):
        "change the Ts and Us in the RNA or DNA sequence"
        if self.temptype == 'RNA':
            for pairs in self.seq_zip:
                mutableseq = pairs[1].tomutable()
                if 'primers' in pairs[0]:
                    mutableseq.replace('U','T')
        pass

    def clean_up(self):
        "the main function that returns a dictionary of sequences"
        self.check_base()
        self.change_base()
        return 0

if __name__== '__main__':
    print(cleanup().clean_up())