#!/usr/bin/env python3

import argparse
import gff_functions 

# remove this comment later
###------ function to parse the command-line arguments
def get_args():
 ###----------------- accept and parse command line arguments
    # create an argument parser object
    parser = argparse.ArgumentParser(description="Get feature sequences from a GFF file and corresponding genome file")


    # add a positional argument, in this case, the position in the Fibonacci sequence
    parser.add_argument("fasta", help="Name of genome file in FASTA format", type=str)
    parser.add_argument("gff3", help="Name of the GFF3 file", type=str)

    # parse the arguments and return in two steps
    args = parser.parse_args()
    return args


def main():
    genome_sequence = gff_functions.read_fasta(args.fasta)
    gene_sequences = gff_functions.read_gff(args.gff3, genome_sequence)
    gff_functions.write_output(gene_sequences)

###-------- calling get_args() happens out here on its own
args = get_args()

    
# set the environment for this script
# is it main() or is this module being called smt else?
if __name__ == '__main__':
    main()
