#!/usr/bin/env python
from Bio import SeqIO
class read_file:
    def __init__(self, file="/home/athe1sm/hacks/PCR-detective/data/sequence.fasta"):
        self.filepath = file
        
        # updated class object by storing outputs in init
        self.seqid_list = []
        self.seq_list = []
        self.seq_tuple = ""  # add placeholder to store output

    def checkfiletype(self):
        "check if the file is in required format, which will be "
        filetype = self.filepath.split(".")[-1]
        if filetype == "fasta" or filetype == "txt":
            pass
        else:
            raise Exception("Wrong filetype: Expected '.fasta' or '.txt' file")

    def extract_seq(self):
        for seq_record in SeqIO.parse(
            "/home/athe1sm/hacks/PCR-detective/data/sequence.fasta", "fasta"
        ):
            self.seqid_list.append(seq_record.id)
            self.seq_list.append(seq_record.seq)
        self.seq_tuple = (self.seqid_list, self.seq_list)
        print(self.seq_tuple)
        # return self.seq_tuple, return statement not working

    def readfile(self):
        "the main function that returns a dictionary of sequences"
        self.checkfiletype()
        self.extract_seq()

if __name__ == "__main__":
    seq1 = read_file()
    seq1.readfile()
