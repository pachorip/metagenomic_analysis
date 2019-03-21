#!/usr/bin/env python3

from plumbum import local
import ssl,os,sys,argparse,logging

#this is the binning script which will run multiple tools

parser = argparse.ArgumentParser()
parser.add_argument("-read1", help="please provide read1 and read2")
parser.add_argument("-read2", help="please provide read1 and read2")
parser.add_argument("-outputdir","-o", help="output directory or sample Name")
parser.add_argument("-v", "--verbose",help = "Verbose", action="store_true")
args = parser.parse_args()
if args.verbose:
    logging.basicConfig(level=logging.INFO)
print("Output directory:" + args.outputdir)
outputdir = args.outputdir
read1 = args.read1
read2 = args.read2

try:
    os.mkdir(outputdir)
except OSError:
    logging.info("Output dir exists!")
    #sys.exit()
else:
    logging.info("Output dir created!")

print ("Starting the Spades assemblies on a range of kmers")
spades=local['spades.py']
(spades['-k',"47,55,59,65,71,77,85",'-1', read1,'-2', read2,'-o', outputdir,'--meta','--only-assembler','--only-assembler'])()
print("spades assemblies finished")


ref=outputdir + "/" + "scaffolds.fasta"
logging.info("Creating the Bowtie2 index")
bowtie_build=local['bowtie2-build']
(bowtie_build[ref,outputdir + "/" + "scaffolds"])()
logging.info("Bowtie2 index created")
RefIndex=outputdir + "/" + "scaffolds"
logging.info("Mapping with bowtie2")
bowtie=local['bowtie2']
samtools=local['samtools']
(bowtie['-x', RefIndex, '-p', "4",'-1', read1, '-2', read2]|samtools['view','-bS']|samtools['sort','-o', outputdir + "/" +"Alignment.sorted.bam"])()
logging.info("Alignment finished")


logging.info("Creating the depth file prior binning")
depth=local["jgi_summarize_bam_contig_depths"]
(depth['--outputDepth',outputdir +"/" +"depth.txt", outputdir + "/" +"Alignment.sorted.bam"])()
logging.info("Depth file created")
logging.info("Metabat2 binning started")

ref=outputdir + "/" + "scaffolds.fasta"
metabat=local['metabat2']
(metabat['-i',ref,'-a',outputdir +"/" +"depth.txt",'-o',outputdir,'-v'])()
logging.info("Binning complete. Output can be found at:{}".format(outputdir))
