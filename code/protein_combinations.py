#!/usr/bin/python3.7
""" protein_combinations.py
Author: Kevin Dick
Date: 2019-01-14
---
Computes the combination of possible reverse translation mappings.
Provides an estimate for the space of possible fractal represenations
for the same protein amino acid sequence.
"""
import mapping_module as mm
import argparse
import random
import os

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', help='The input file/directory to convert AA to nucleotides.')
parser.add_argument('-o', '--output', help='The output file/directory to save the conversion(s).')
parser.add_argument('-v', '--verbose',  help='Increase output verbosity.', action="store_true")
args = parser.parse_args()

# EXAMPLE: ./protein_combinations.py -i ../data/raw/hsapiens.tab -o ../data/sequence-space/hsapiens.tab -v

def count_combinations(sequence):
    """ count_combinations
        Counts the number to total combinations
        possible when converting from AA to DNA.
        Ex: MATY = (1)(4)(4)(2) = 32
    """
    combinations = 1
    for aa in sequence: combinations *= len(mm.AA2DNA[aa])
    return combinations

if os.path.isfile(args.input):
    first = True
    f = open(args.input, 'r')
    g = open(args.output, 'w')
    for line in f:
        if first:
            g.write('Entry\tOrganism\tAA_len\tnum_combinations\n')
            first = False
            continue
        prot = line.split('\t')[0].strip()
        name = line.split('\t')[1].strip()
        AAs  = line.split('\t')[-1].strip()
        comb = count_combinations(AAs)
        g.write(f'{prot}\t{name}\t{len(AAs)}\t{comb}\n')

if args.verbose: print('Execution Complete!~')
