#!/usr/bin/env python3
import numpy
from Bio.Seq import Seq
from src.SmithWaterman import match, Scoring

class Matchmaker:
    """
    This Class objects recieves a zipped object containing sequenceID and sequence, and group them by the 
    tags in the seqID, generating a corresponding comparing pattern, and pass the to-be-compared sequences
    to SmithWaterman.py module for sequence alignment.
    """
    def __init__(self, clean_zip,output='new output'):
        """
        initialize the instance
        """
        self.clean_zip = clean_zip
        self.groups = 0
        n = int(0)
        for pairs in self.clean_zip:
            if 'template' in pairs[0]:
                n = max(n,int(pairs[0][-1]))
        self.groups = n
    
    def grouping(self):
        """
        Grouping sequences by the features in their seqID
        """
        counter = int(0)
        self.groupeddict={}
        while counter < self.groups:
            counter += 1
            seqlist=[]
            for pairs in self.clean_zip:
                if f'template{counter}' in pairs[0]:
                    seqlist.append(pairs)
                    seqlist.append(('comp'+pairs[0],pairs[1].reverse_complement()))
                if f'primer{counter}' in pairs[0]:
                    seqlist.append(pairs)
            self.groupeddict[counter]=tuple(seqlist)
        print(self.groupeddict)



    def in_group_mm(self):
        """
        Iterate the groups and send all the template/primer combinations to aligment algorithm.
        """
        self.res=''
        for n in range(1,len(self.groupeddict)+1):
            self.res += f'\n\nIn-group alignment check for Group{n}\n\n'
            groups = self.groupeddict[n]
            for tpairs in groups:
                if 'template'in tpairs[0]:
                    tempname = tpairs[0]
                    tempseq = tpairs[1]
                    for ppairs in groups:
                        if 'primer' in ppairs[0]: #to align each template against each primer
                            primername = ppairs[0]
                            primerseq = ppairs[1]
                            res = Scoring(str(tempseq),str(primerseq[::-1])).localalign(-5,-5) #calls the local alignment function
                            if res == '':
                                self.res += '\nno hit'
                            else:    
                                self.res += (f'\n{tempname} + {primername}\n' + res) #formulate the result tring
    
    def cross_mm(self):
        """
        TBC
        """
        pass
            

    def run(self):
        """
        The main func. that runs the whole class instance.
        """
        self.grouping()
        self.in_group_mm()
        return self.res



if __name__=='__main__':
    testzip=[('template1', Seq('AGCTAGCTAGCTTAGCTA')),
    ('template2', Seq('AGCTAGCTAGCTTAGCTA')),
    ('primer1_2', Seq('AGCTAGCTAGCTTAGCTA')),
    ('primer1_1', Seq('AGCTAGCTAGCTTAGCTA')),
    ('primer2_1', Seq('AGCTAGCTAGCTTAGCTA')),
    ('primer3_1', Seq('TGCATGCTAACGGGGTAGTACTACGT')), 
    ('template3', Seq('TGCAGCATGTTTTAGTCATCTAGCTGTAGCTGTGCTAGTCGATCGTGTAGCTTGATA'))]
    print(Matchmaker(testzip).run())