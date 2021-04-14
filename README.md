# PCR detective

## Our Goal:
In this project, we are trying to create a lightweighted and open-sourced tool for scientists to do nucleic acid sequence analysis and cleanup before PCR reactions or during primer designing.
Our tool will support several kinds of PCRs from conventional PCR to multiplex rt-qPCR. Our tool will verify (and clean up if required by the user) the input of the sequence that will be analyzed and will return a list of issues that might cause trouble in experiments, like distinct Tm difference between primers, complicated secondary structures in RNA templates, and false priming.

## Dependency:
`Biopython` version 1.78  
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
│   ├── CLISEQDNA.txt
│   └── CLISEQRNA.txt
├── paired-programming.md
├── proposal.md
├── setup.py
├── src
│   ├── LinearFold.cpp
│   ├── LinearFold.h
│   ├── LinearFoldEval.cpp
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
│   ├── readfile.py
│   ├── scripts
│       └── gen_latex_script.py
└── testseq
```

### In Devlopment
We have successfully have the readfile module running, and the cleanup module is in development and hopefully will come into being in the near future. To use the readfile module just simply install the biopython package and run the code. You can also from module `readfile` import the `read_file` class, and run the code with

 ```
file = read_file('filepath')
seq_tuple = file.readfile()
```

the input will be fasta or txt files with sequences that can be recognized by Biopython, while the output will be a tuple including a list of ids and another list of sequences.

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
### How to compile the C++ source file  
```
make
```
### How to install this tool locally:
```
conda install biopython -c conda-forge ...

git clone https://github.com/athe1sm/PCR-detective.git
cd ./PCR-detective
pip install -e .
```
