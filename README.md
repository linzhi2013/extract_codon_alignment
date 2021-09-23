# extract-codon-alignment

## 1 Introduction

`extract-codon-alignment`  (https://github.com/linzhi2013/extract_codon_alignment) is a tool to extract some codon positions (1st, 2nd, 3rd) from a CDS alignment with `Biopython` (http://www.biopython.org/)

## 2 Installation

    $ pip install extract-codon-alignment
    # or with Bioconda
    conda install extract-codon-alignment

There will be a command `extract_codon_alignment` created under the same directory as your `pip` command.

## 3 Usage

    $ extract_codon_alignment
    usage: extract_codon_alignment [-h] --alignedCDS <file>
                                   [--aln_format <format>]
                                   [--codonPoses {1,2,3,12,13,23}] --outAln <file>

    To extract some codon positions (1st, 2nd, 3rd) from a CDS alignment.

    optional arguments:
      -h, --help            show this help message and exit
      --alignedCDS <file>   The CDS alignment.
      --aln_format <format>
                            the file format for the CDS alignment. Anything
                            accepted by BioPython is fine [fasta]
      --codonPoses {1,2,3,12,13,23}
                            Codon position(s) to be extracted [12]
      --outAln <file>       output file name

## Author
Guanliang MENG

## Citation
Currently I have no plan to publish `extract-codon-alignment`. **However, if you use this program in your analysis, or you "steal" the idea/codes of this program into your script, I should be one of the co-authors in your publication!!!**

Besides, since `extract-codon-alignment` makes use of `Biopython`, you should cite it if you use `extract-codon-alignment` in your work:

    Peter J. A. Cock, Tiago Antao, Jeffrey T. Chang, Brad A. Chapman, Cymon J. Cox, Andrew Dalke, Iddo Friedberg, Thomas Hamelryck, Frank Kauff, Bartek Wilczynski, Michiel J. L. de Hoon: “Biopython: freely available Python tools for computational molecular biology and bioinformatics”. Bioinformatics 25 (11), 1422–1423 (2009). https://doi.org/10.1093/bioinformatics/btp163

Please go to `http://www.biopython.org/` for more details.






