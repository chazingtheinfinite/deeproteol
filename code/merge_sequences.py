#!/usr/bin/python
""" merge_sequences.py
Author: Kevin Dick
Date: 2018-11-23
---
Iterates through all raw_data files, extracts the sequences,
adds them to a list, shuffles their order, and writes them to file.
"""
import os, sys
import random

# Constants:
SEED    = 42
DATADIR = '../data/raw/'
OUTFILE = '../data/aa-seqs/merged_sequences.txt'
SEQ_COL = 5 
VERBOSE = True

# To ensure reproducibility...
random.seed(SEED)

# Assumes all files contain the same column formatting...
raw_files = os.listdir(DATADIR)

seqs = []
for filename in raw_files:
	if '.tab' not in filename: continue
	with open(os.path.join(DATADIR, filename), 'r') as f:
    		next(f) # Skip header...
		for line in f: seqs.append(line.split('\t')[SEQ_COL].strip())
if VERBOSE: print 'Number of Seqs: ' + str(len(seqs))

# To avoid biasing an LSTM model by presenting entire blocks of proteomes from a single organism as a time
# lets shuffle the sequences and then write them out one protein at a time...
if VERBOSE: print 'Shuffling...'
random.shuffle(seqs)

# Write them all out to file...
f = open(OUTFILE, 'w')
f.write('\n'.join(seqs))
f.close()

if VERBOSE: print 'Execution Complete!~ ' + sys.argv[0]
