#! /usr/bin/env python3
import subprocess
import sys
import os
import io
from io import TextIOWrapper

class linearfold:
    def __init__(self, seq='AAAACGGUCCUUAUCAGGACCAAACA', beamsize='100', linearfoldpath='./bin/linearfold_c'):
        self.seq=seq.encode("utf-8")
        self.b=beamsize
        self.path=linearfoldpath        
    def runLF(self):
        cmd = [self.path, self.b, '0', '0', '0', '0']
        self.proc = subprocess.run(cmd, input=self.seq, shell=0,stdout=subprocess.PIPE)
        self.res=self.proc.stdout.decode().split('\n')[1][0:-7]

    def run(self):
        self.runLF()
        return self.res

if __name__=='__main__':
    print(linearfold().run())
 