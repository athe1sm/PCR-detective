#! usr/bin/env python
import numpy as np
def match(base):
    """
    A light function that digitalize the base chr and ease the culculation
    """
    if base == 'A':
        return 3
    elif base == 'C' or base == 'G':
        return 2
    elif base == 'T':
        return 1
    else:
        raise Exception('only DNA seq can be matched')

class Scoring():
    """
    The scoring class object that takes two sequences and align them using SW dinamic programming algorithm.
    The scoring parameters are hardcoded to avoid excessive arguments.
    """
    def __init__(self,seq1,seq2):
        """
        Initialize the instance
        """
        self.seq1=seq1
        self.seq2=seq2

    def localalign(self,mismatch,gap):
        """
        The local alignment algorithm based on Numpy.
        The nacktracking algorithms that formulate a str for output
        """
        self.mismatch=mismatch
        self.gap=gap
        j=1
        x=len(self.seq1)+1
        y=len(self.seq2)+1
        self.scoringMatrix=np.zeros((y,x))  #Define a scoring matrix
        self.peakdic={}
        #print('0',self.seq1)
        res=''
        while j < y:
            i=1
            while i < x:           #the dnamic programming in the scoring matrix
                self.scoringMatrix[j,i] = max(
                    self.scoringMatrix[j,i-1] + self.gap,
                    self.scoringMatrix[j-1,i] + self.gap,
                    self.scoringMatrix[j-1,i-1] + (1 if match(self.seq1[i-1]) + match(self.seq2[j-1]) == 4 else self.mismatch), #looking for base pairing
                    0) # Three sources of the score in each cell, which is up, left, and upperleft.
                if self.scoringMatrix[j,i]>4 and self.scoringMatrix[j,i]>max(
                    self.scoringMatrix[j-1,i],
                    self.scoringMatrix[j,i-1],
                    self.scoringMatrix[j-1,i-1]
                ):
                    self.peakdic[(j,i)]=self.scoringMatrix[j,i] # looking for candidate local maximum 
                i+=1
            j+=1
       
        #print(self.peakdic)
        while 1: # The backtracking algo.
            if self.peakdic=={}:
                break
            self.peaklist = sorted(self.peakdic.items(), key=lambda d: d[1], reverse=1)
            j,i=self.peaklist[0][0][0],self.peaklist[0][0][1] # Starting the backtracking from the endpoint with highest score
            align_1,align_2='',''

            while (i > 0 or j > 0) and self.scoringMatrix[j,i] > 0:

                if (j,i) in self.peakdic.keys():
                    del self.peakdic[(j,i)] # Dropped the item on the path to avoid redundancy
                #below is the actual backtracking algo
                if i > 0 and j > 0 and match(self.seq1[i - 1]) + match(self.seq2[j - 1])==4:
                    align_1 = self.seq1[i - 1] + align_1
                    align_2 = self.seq2[j - 1] + align_2
                    i = i - 1
                    j = j - 1
         
                elif i > 0 and (self.scoringMatrix[j,i] == self.scoringMatrix[j,i-1] + self.mismatch or self.scoringMatrix[j,i] == self.scoringMatrix[j,i-1] + self.gap):
                    align_1 =  self.seq1[i - 1] + align_1
                    align_2 = "-" + align_2
                    i = i - 1
             
                else:
                    align_1 = "-" + align_1
                    align_2 = self.seq2[j - 1] + align_2
                    j = j - 1

                if (j,i) in self.peakdic.keys():
                    del self.peakdic[(j,i)]

            res += (f'\n{align_1} {i+len(align_1)}\n{align_2}\n')               
        #print(res)
        return res

if __name__=='__main__':
    Scoring('GAATTCAATACTCCACTTTCCAT','GAATTATACTCCACTTTCCAATGTGTA').localalign(-2,-2)
