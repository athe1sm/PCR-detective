# project

### Description of project goal: 

My program will provide a API and (probably) a graphic UI to do nucleic acid analysis before multiplex PCR reactions.

I planned to support conventional PCR and RT-qPCR (stem loop method and traditional method) reactions. My program will verify (and cleanup if required by user) the input of the sequence that will be analysed, and will return a list of issues that might cause trouble in experiments, like distinct Tm difference between primers, complicated seconary stuctures in RNA templetes, and false priming.  

### Description of the code: 

It will have arguments to let user choose what type of analysis they want, and will have one class to accept manually inputted sequences through UI or to read text files including a series of sequences and their lables (primers/templets), and another class will detect the sequence imput for any other characters other than ATCGUs and Ts in RNA or Us in DNA (unless specified by user), and form a complementary trand for templets.
 
If RT-qPCR analysis is chosen, one class will broadly calculates a secondary structure of the imputted RNA sequence, and raise a warning if too many intramolecular base pairing was found. One other class will be adopting cross-comparing primers and templets, and search for unwanted priming, like primer dimers or false priming (I am thinking about using algorithms like FASTA here). 

The last class will take the returned data from other class and formulate a output 

### Description of the data: (e.g., it will analyze CSV data input by the user.)

It will accept manual imputs of sequences from UI, or read .csv, .txt, or .fasta files.

### Description or demonstration of user interaction:

The output will be a .txt file that lists the imputted sequences, the Tm value of primers (and any warnings),  RNA secondary structures, and false priming reagions like
> primer1    5'ATCGGTACTGC3'  15
> 
>                |||||||
>                
> templet2   3'ATGCCATGAGC5'  650
> 
> 
> primer3    5'ATCGGTACT3'    20
> 
>                |||||||
>                
> primer4      3'GCCATGAGC5'  17
