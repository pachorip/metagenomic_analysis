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
  
