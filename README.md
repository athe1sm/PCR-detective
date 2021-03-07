# PCR detective

## Our Goal:
In this project, we are trying to create a lightweighted and open-sourced tool for scientists to do nucleic acid sequence analysis and cleanup before PCR reactions or during primer designing.
Our tool will support several kinds of PCRs from conventional PCR to multiplex rt-qPCR. Our tool will verify (and clean up if required by the user) the input of the sequence that will be analyzed and will return a list of issues that might cause trouble in experiments, like distinct Tm difference between primers, complicated secondary structures in RNA templates, and false priming.

### In Devlopment
How to install this tool locally
```
conda install [list dependencies here...] -c conda-forge ...

git clone https://github.com/athe1sm/project.git
cd ./project
pip install -e .
```
