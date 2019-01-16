#!/usr/bin/python3.7
""" reverse_translate
Author: Kevin Dick
Date: 2019-01-14
---
Reverse translates an amino-acid sequence to its
nucleotide counter-part. While there is no concensus
sequence for this process (a single amino acid may result
from many nucleotide combinations) for our purposes, it is
sufficient to randomly select each tri-nucleotide with a uniform
probability.
"""
import mapping_module as mm
import argparse
import random
import os

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', help='The input file/directory to convert AA to nucleotides.')
parser.add_argument('-o', '--output', help='The output file/directory to save the conversion(s).')
parser.add_argument('-s', '--seed', help='Seed to set for replicability.', type=int, required=False, default=42)
parser.add_argument('-v', '--verbose',  help='Increase output verbosity.', action="store_true")
args = parser.parse_args()

# EXAMPLE: ./reverse_translate.py -i ../data/raw/hsapiens.tab -o ../data/dna-seqs/hsapiens.tab -v

# Set seed for 
random.seed(args.seed)

def convert_AA2DNA(sequence):
    """ convert_AA2DNA
        Converts an amino acid sequence by randomly
        selecting a tri-nuclotide codon with uniform
        probability.
    """
    conversion = ''
    for aa in sequence:
        conversion += random.choice(mm.AA2DNA[aa.upper()])
    if args.verbose: print(f'Len AA: {len(sequence)}\tLen DNA: {len(conversion)}')
    return conversion

if os.path.isfile(args.input): 
    first = True
    f = open(args.input, 'r')
    g = open(args.output, 'w')
    for line in f:
        if first: 
            g.write(line)
            first = False
            continue
        data = '\t'.join(line.split('\t')[:-2])
        AAs  = line.split('\t')[-1].strip()
        ntds = convert_AA2DNA(AAs)
        g.write(f'{data}\t{len(ntds)}\t{ntds}\n')

if args.verbose: print('Execution Complete!~')
