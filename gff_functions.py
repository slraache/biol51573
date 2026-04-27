#!/usr/bin/env python3

import csv

def read_fasta(fasta_file):
    # make a variable to store the genome sequence
    seq = ''
    with open(fasta_file, "r") as f:
        for line in f:
            if line.startswith(">"):
                continue 
            else:
                seq += line.rstrip()
    return seq

def read_gff(gff3_file, genome_sequence):
    # dictionary for key = gene name, value = sequence
    gene_sequences = {}

    with open(gff3_file, "r") as g:
        # create a csv reader object
        reader = csv.reader(g, delimiter='\t')

        # read the file line by line
        for line in reader:
            start = int(line[3]) - 1
            end   = int(line[4]) # we don't have to change the end coordinate bc of how Python slices lists
            feature_seq = genome_sequence[start:end]
            # print(start, end, len(feature_seq), atts)

            # all this is to get the gene name
            atts  = line[8]
            # split the attritubes line on ';'
            atts_list = atts.split(';')
            # split the first field on the '=' sign, then the gene name is the end of this list
            a = atts_list[0].split('=')
            gene_name = a[-1]

            # can print on the fly
            # write_output_on_the_fly(gene_name, feature_seq)

            # alternatively, store in a dictionary, where key = gene_name, value = sequence
            if gene_name in gene_sequences:
                gene_name = gene_name + "-2"
                gene_sequences[gene_name] = feature_seq
            else: 
                gene_sequences[gene_name] = feature_seq
        
    return gene_sequences


def write_output_on_the_fly(name, seq):
    print(f">{name}")
    print(seq)


def write_output(gene_dict):
    for name, seq in gene_dict.items():
        print(f">{name}")
        print(seq)

# set the environment for this script
# is it main() or is this module being called smt else?
if __name__ == '__main__':
    main()