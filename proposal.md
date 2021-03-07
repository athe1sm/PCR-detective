# PCR-detective

###  Goals of our project: 

In this project, we are trying to create a lightweighted and open-sourced tool for scientists to do nucleic acid sequence analysis and cleanup before PCR reactions or during primer designing.  
Our tool will support several kinds of PCRs from conventional PCR to multiplex rt-qPCR. Our tool will verify (and clean up if required by the user) the input of the sequence that will be analyzed and will return a list of issues that might cause trouble in experiments, like distinct Tm difference between primers, complicated secondary structures in RNA templates, and false priming.  

### What kinds of data will be supported:

In our tool we will provide an UI that will allow users to select which kind of analysis that they want to do and select files that contains a series of sequences and their lables (primers/templets) or manually input them. The file type could be .txt or .fasta and the format of the sequence should be FASTA.  

### An example of data

```
>primer1_1
ATCGTGAGCAGATC

>primer1_2
GCAGTTGATCCGTAT

>templete1
TGACGTACGTGACGTACGTACGTACGTAGCACTCGGTCAGTCGATGATATACGCAT

>primer2_1
......
```

### How to use this tool:

We will provide an UI for users to interact with. The UI will have a dropdown menu for users to select a kind of analysis (like rt-qPCR) from a series of presets, and there will be an input box and a short description about the expected data.

If you are using an CLI version of this tool you can enter the code like this:
```
# mock example of command line options to a program
PCRdetective -mqPCR -file 'filepath' --sequencecleanup
```

The output will be a .txt file that lists the imputted sequences, the Tm value of primers (and any warnings like huge Tm differance, unexpected characters in the sequences),  RNA secondary structures, and false priming reagions like
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

### Other tools that can do similar jobs:

- RNA structure
  - for structure predicting 
- Oligo
  - primer designing
- Primer Premier
  - primer designing
- BLAST
  - sequence alignment
- FASTA
  - sequence alignment
