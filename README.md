#identify_duplicate_fastq_seq.py

The script takes multiple fastq files and run like below:

python3 identify_duplicate_fastq_seq.py one.fq two.fq three.fq four.fq

The output of this script is all the files tab delimited with a matrix of duplicate ids, where the duplicate id isn't found, it just prints a "-"

# metagenomic_analysis
metagenomic_assembly_and_binning.py is a python wrapper to run Spades assemblies on a range of k-mers, alignment of reads back to the assembly and binning the assembled contigs.

Please make sure you have Python3, plumbum (pip install plumbum), latest version of Spades, Bowtie2, samtools and metabat2  installed on your machine.

python3 metagenomic_assembly_and_binning.py -h

usage: metagenomic_assembly_and_binning.py [-h] [-read1 READ1] [-read2 READ2]
                                           [-outputdir OUTPUTDIR] [-v]

optional arguments:
  -h, --help            show this help message and exit
  -read1 READ1          please provide read1 and read2
  -read2 READ2          please provide read1 and read2
  -outputdir OUTPUTDIR, -o OUTPUTDIR
                        output directory or sample Name
  -v, --verbose         Verbose
  
