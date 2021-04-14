#!/usr/bin/env python
from .readfile import Read_file
from Bio.Seq import Seq
import os
from .linearfold import linearfold

#seq_tuple=readfile
class Cleanup:
    def __init__(self,seq_tuple="/home/athe1sm/hacks/PCR-detective/data/bad_seq.fasta",temptype='DNA',output='new output',autoclean=1):
        self.fileheader=seq_tuple.split('/')[-1]
        self.seq_tuple= Read_file(seq_tuple).readfile()
        self.seq_zip = zip(self.seq_tuple[0],self.seq_tuple[1])
        self.temptype = temptype
        self.autoclean = autoclean 
        #print(list(self.seq_zip))
        self.cleanseqlist=[]
        self.outputname=output

    def makeoutput(self):
        outputpath = os.getcwd()+'/output'
        if not os.path.exists(outputpath):
            os.makedirs(outputpath)
        doutput = outputpath + '/' + self.outputname + '.txt'
        if os.path.isfile(doutput):
            n=0
            while 1:
                n += 1
                noutput = doutput[:-4] + "(" + str(n) + ").txt"
                if not os.path.isfile(noutput):
                    break
            self.file = open(noutput,'w')
        else:
            self.file = open(doutput,'w')
        self.file.write(f'PCR-detective Result for {self.fileheader}\n')

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
            self.file.write(pairs[0]+'\n'+pairs[1] + '\n')
            if self.temptype == 'RNA':
                if 'template' in pairs[0]:
                    self.file.write(linearfold(pairs[1]).run()+'\n')

    def change_base(self):
        "change the Ts and Us in the RNA or DNA sequence"
        self.file.write('\nCaution: the sequences have been automated cleaned up\n')
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
        "the main function that returns a dictionary of sequences"
        self.makeoutput()
        if self.autoclean==0:
            self.check_base()
        if self.autoclean==1:
            self.change_base()
        self.file.close()
        return self.clean_zip

if __name__== '__main__':
    print(list(Cleanup().clean_up()))