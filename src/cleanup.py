#!/usr/bin/env python
from src.readfile import Read_file
from Bio.Seq import Seq
import os
from src.linearfold import linearfold

#seq_tuple=readfile
class Cleanup:
    """
    This class object recieves a tuple w/ sequences and their IDs from Read_file module, and either check
    if there are any inappropriate bases or automatically cleanup the sequence. The output will be a zipped
    object which will be passed to matchmaker module. This is also where the output file will be made.
    """
    def __init__(self,seq_tuple="/home/athe1sm/hacks/PCR-detective/data/sequence.fasta",temptype='DNA',output='',autoclean=0):
        """
        Initialization of instance
        """
        self.fileheader=seq_tuple.split('/')[-1]
        self.seq_tuple= Read_file(seq_tuple).readfile()
        self.seq_zip = zip(self.seq_tuple[0],self.seq_tuple[1])
        self.temptype = temptype
        self.autoclean = autoclean 
        #print(list(self.seq_zip))
        self.cleanseqlist=[]
        self.outputname=output

    def makeoutput(self):
        """
        make a .txt file accodrding to the input
        """
        self.file = open(self.outputname,'w')
        self.file.write(f'PCR-detective Result for {self.fileheader}\n\n')

    def check_base(self):
        """
        check the base in the sequences and raise warnings
        """
        self.file.write('These sequences have been checked\n\nSequence input\n')
        for pairs in self.seq_zip:
            if 'primer' in pairs[0]:
                if 'U' in pairs[1]:
                    raise Exception('Urasils are not expected in DNA primers')
                self.cleanseqlist.append(pairs[1]) 
            elif self.temptype == 'DNA' and 'template' in pairs[0]:
                if 'U' in pairs[1]:
                    raise Exception('Urasils are not expected in DNA templets')
                self.cleanseqlist.append(pairs[1]) 
            elif self.temptype == 'RNA' and 'template' in pairs[0]:
                if 'T' in pairs[1]:
                    raise Exception('Thymines are not expected in RNA templets')
                self.cleanseqlist.append(pairs[1].back_transcribe())    
            self.file.write('\n'+ str(pairs[0])+'\n'+str(pairs[1]) + '\n')
            
            if self.temptype == 'RNA':
                if 'template' in pairs[0]:
                    self.file.write(linearfold(str(pairs[1])).run()+'\n\n')
                    
        self.clean_zip = zip(self.seq_tuple[0],self.cleanseqlist) 
        print(self.cleanseqlist)

    def change_base(self):
        """
        change the Ts and Us in the RNA or DNA sequence
        """
        self.file.write('\nCaution: these sequences have been automatically cleaned up\n\nSequence input\n\n')
        if self.temptype == 'RNA':
            for pairs in self.seq_zip:
                seqstr = str(pairs[1])
                if 'primer' in pairs[0]:
                    clnseqstr=seqstr.replace('U','T')
                    self.file.write('\n' + pairs[0]+'\n'+clnseqstr + '\n')
                if 'template' in pairs[0]:
                    clnseqstr=seqstr.replace('T','U')
                    self.file.write('\n' + pairs[0]+'\n'+clnseqstr + '\n')
                    self.file.write(linearfold(clnseqstr).run())
                    clnseqstr=str(Seq(clnseqstr).back_transcribe())
                self.cleanseqlist.append(Seq(clnseqstr))

        elif self.temptype == 'DNA':
            for pairs in self.seq_zip:
                seqstr = str(pairs[1])
                if 'primer' in pairs[0]:
                    clnseqstr=seqstr.replace('U','T')
                if 'templet' in pairs[0]:
                    clnseqstr=seqstr.replace('U','T')
                self.cleanseqlist.append(Seq(clnseqstr)) 
                self.file.write('\n' + pairs[0] + '\n' + clnseqstr + '\n')             
        self.clean_zip=zip(self.seq_tuple[0],self.cleanseqlist)
        
        
    def clean_up(self):
        """
        the main function that runs the class and returns a dictionary of sequences
        """
        self.makeoutput()
        if self.autoclean==0:
            self.check_base()
        if self.autoclean==1:
            self.change_base()
        self.file.close()
        return self.clean_zip

if __name__== '__main__':
    print(list(Cleanup().clean_up()))