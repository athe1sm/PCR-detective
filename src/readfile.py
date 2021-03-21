#!/usr/bin/env python
from Bio import SeqIO
class read_file:

    def __init__(self,file='/home/athe1sm/hacks/PCR-detective/data/sequence.fasta'):
        self.filepath = file

    def checkfiletype(self):
        'check if the file is in required format, which will be '
        filetype=self.filepath.split('.')[-1]
        if filetype=='fasta'or filetype=='txt':
            pass
        else:
            raise Exception("Wrong filetype: Expected '.fasta' or '.txt' file")


    def extract_seq(self):
        seqid_list=[]
        seq_list=[]
        for seq_record in SeqIO.parse("/home/athe1sm/hacks/PCR-detective/data/sequence.fasta", "fasta"):
            seqid_list.append(seq_record.id)
            seq_list.append(seq_record.seq)
        self.seq_tuple=(seqid_list,seq_list)

    def readfile(self):
        'the main function that returns a dictionary of sequences'
        self.checkfiletype()
        self.extract_seq()
        return self.seq_tuple

if __name__=='__main__':
    seq1=read_file()
    print(seq1.readfile())
