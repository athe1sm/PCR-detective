#!/usr/bin/env python
from Bio import SeqIO
class Read_file:
    """
    This class object reads the sample file or the file provided by the user, and returns a tuple of
    sequences. 
    """
    def __init__(self, file="/home/athe1sm/hacks/PCR-detective/data/sequence.fasta"):
        """
        initiate the class instance and takes the filepath
        """
        self.filepath = file
        
        # updated class object by storing outputs in init
        self.seqid_list = []
        self.seq_list = []
        #self.seq_tuple = ""  # add placeholder to store output

    def checkfiletype(self):
        """
        check the extension of the file that will be read to avoid unsupported filetype.
        """
        filetype = self.filepath.split(".")[-1]
        if filetype == "fasta" or filetype == "txt":
            pass
        else:
            raise Exception("Wrong filetype: Expected '.fasta' or '.txt' file")

    def extract_seq(self):
        """
        call SeqIO.parse from Biopython to extract the sequences contained in the file.
        """
        for seq_record in SeqIO.parse(
            self.filepath, "fasta"
        ):
            self.seqid_list.append(seq_record.id)
            self.seq_list.append(seq_record.seq)
        self.seq_tuple = (self.seqid_list, self.seq_list)
        

    def readfile(self):
        """
        the main function that returns a tuple of ids and sequences
        """
        self.checkfiletype()
        self.extract_seq()
        return self.seq_tuple

if __name__ == "__main__":
    seq1 = Read_file()
    print(seq1.readfile())