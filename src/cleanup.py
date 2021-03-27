#!/usr/bin/env python
from readfile import read_file
from Bio.Seq import Seq
#seq_tuple=readfile
class cleanup:
    def __init__(self,seq_tuple="/home/athe1sm/hacks/PCR-detective/data/bad_seq.fasta",temptype='DNA',autoclean=0):
        self.seq_tuple= read_file(seq_tuple).readfile()
        self.seq_zip = zip(self.seq_tuple[0],self.seq_tuple[1])
        self.temptype = temptype
        self.autoclean = autoclean 
        #print(list(self.seq_zip))
        self.cleanseqlist=[]
        

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
                seqstr = str(pairs[1])
                if 'primer' in pairs[0]:
                    clnseqstr=seqstr.replace('U','T')
                if 'templet' in pairs[0]:
                    clnseqstr=seqstr.replace('T','U')
                self.cleanseqlist.append(Seq(clnseqstr))
        elif self.temptype == 'DNA':
            for pairs in self.seq_zip:
                seqstr = str(pairs[1])
                if 'primer' in pairs[0]:
                    clnseqstr=seqstr.replace('U','T')
                if 'templet' in pairs[0]:
                    clnseqstr=seqstr.replace('U','T')
                self.cleanseqlist.append(Seq(clnseqstr))              
        self.clean_zip=zip(self.seq_tuple[0],self.cleanseqlist)
        

    def clean_up(self):
        "the main function that returns a dictionary of sequences"
        if self.autoclean==0:
        self.check_base()
        if self.autoclean==1
        self.change_base()
        return self.clean_zip

if __name__== '__main__':
    print(list(cleanup().clean_up()))