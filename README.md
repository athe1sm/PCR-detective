# PCR detective

## Our Goal:
In this project, we are trying to create a lightweighted and open-sourced tool for scientists to do nucleic acid sequence analysis and cleanup before PCR reactions or during primer designing.
Our tool will support several kinds of PCRs from conventional PCR to multiplex rt-qPCR. Our tool will verify (and clean up if required by the user) the input of the sequence that will be analyzed and will return a list of issues that might cause trouble in experiments, like distinct Tm difference between primers, complicated secondary structures in RNA templates, and false priming.

## Dependency:
`Biopython` version 1.78  
`numpy` 1.18.1  
`gcc` 4.8.5 or above  
`python`3  

### Stuecture  
```
.
├── Makefile
├── README.md
├── bin
│   ├── linearfold_c
│   └── linearfold_v
├── data
│   ├── bad_seq.fasta
│   ├── sequence.fasta
│   └── sequence_rna.fasta
├── output
│   ├── DNAcheck.txt
│   └── RNAcheck.txt
├── paired-programming.md
├── proposal.md
├── setup.py
├── src
│   ├── LinearFold.cpp
│   ├── LinearFold.h
│   ├── LinearFoldEval.cpp
│   ├── SmithWaterman.py
│   ├── Utils
│   │   ├── energy_parameter.h
│   │   ├── feature_weight.h
│   │   ├── intl11.h
│   │   ├── intl21.h
│   │   ├── intl22.h
│   │   ├── utility.h
│   │   └── utility_v.h
│   ├── __init__.py
│   ├── __main__.py
│   ├── cleanup.py
│   ├── linearfold
│   ├── linearfold.py
│   ├── matchmaker.py
│   ├── readfile.py
│   ├── scripts
│       └── gen_latex_script.py
└── testseq
```
----------------------------------------

### How to compile the C++ source code  
```
make
```
### How to install this tool locally:
```
conda install [dependencies] -c conda-forge ...

git clone https://github.com/athe1sm/PCR-detective.git
cd ./PCR-detective
pip install -e .
```
----------------------------------------------------------------------------------------
### Update Log 2021/04/21  
We are adding many more features to this package.  

The first thing is that the python API AND the command line features are both available now. You can make the max use of this tool by using it as a whole or calling modules from the package.  

The second Thing that might be interesting is the epiphany of the DNA pairing system. Now all the sequences, after proper treatments, will be converted to DNA version, and then subject to DNA base-pairing alignment based on SmithWaterman algorithm, which will return the local best solution of the alignment.  

This part will generate a result somehow like this:
```
comptemplate2 + primer2_1

GTGTGCTAGGTGGGGCTAAT 118
CACACGATCCACCCCGATTA 

TAGCTGGGG 126
ATCCACCCC 

GCTGCCCCT 80
CCACCCCGA 

GTCTGG-AGCTGC 54
CACACGATCCACC 
```
The upper line is the sequence of the templates and the number tells you the position of the last base, while the lower line is the primer (at least for now).

The result was arranged in significance order, which means top results shows a better base-pairing and will more likely to cause trouble if it wasn't designed like that.

The way to call the CLI tool is pretty much the same. with all other annoying params hardcoded in the functions

------------------------------------------------------------------------------------------
### Update Log 2021/04/14  
We are finally pushing the first CLI tool of PCR-detective!  
The Python API is temporarily disabled to fit the command line usage  
You may use this tool by typing in the command line like:  
```
PCR_detective [input path] [template type] [output file name] --clean
```
The output will be under the `./output` directory and the name will be your `[output file name].txt`  
We also included the source file of the linearfold algorithm, that can be compiled by users.  
Example output 
```
PCR-detective Result for sequence_rna.fasta

Caution: the sequences have been automated cleaned up

primer1_1
AGCTAGCTAGCTTAGCTA

primer1_2
TGCATGCTAACGGGGTAGTACTACGT

template1
UGCUAGCAUGCUUGUAGUCAUCUAGCUUGUAGCUGUGCUAGUCGAUCGUGUAGCUGAAUGCGACAUCAUGUAGUCACUA
.(((((((((((...(((......)))...))).)))))))).....................................
```
-----------------------------------------------
### In Devlopment
We have successfully have the readfile module running, and the cleanup module is in development and hopefully will come into being in the near future. To use the readfile module just simply install the biopython package and run the code. You can also from module `readfile` import the `read_file` class, and run the code with

```
file = read_file('filepath')
seq_tuple = file.readfile()
```

the input will be fasta or txt files with sequences that can be recognized by Biopython, while the output will be a tuple including a list of ids and another list of sequences.   
