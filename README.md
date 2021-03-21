# PCR detective

## Our Goal:
In this project, we are trying to create a lightweighted and open-sourced tool for scientists to do nucleic acid sequence analysis and cleanup before PCR reactions or during primer designing.
Our tool will support several kinds of PCRs from conventional PCR to multiplex rt-qPCR. Our tool will verify (and clean up if required by the user) the input of the sequence that will be analyzed and will return a list of issues that might cause trouble in experiments, like distinct Tm difference between primers, complicated secondary structures in RNA templates, and false priming.

## Dependency:
`Biopython` version 1.78

### In Devlopment
We have successfully have the readfile module running, and the cleanup module is in development and hopefully will come into being in the near future. To use the readfile module just simply install the biopython package and run the code. You can also from module `readfile` import the `read_file` class, and run the code with

 ```
file = read_file('filepath')
seq_tuple = file.readfile()
```

the input will be fasta or txt files with sequences that can be recognized by Biopython, while the output will be a tuple including a list of ids and another list of sequences.

How to install this tool locally:
```
conda install biopython -c conda-forge ...

git clone https://github.com/athe1sm/PCR-detective.git
cd ./PCR-detective
pip install -e .
```
