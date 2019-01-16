#!/usr/bin/python3.6
""" plot_sequence_combinations.py
Author: Kevin Dick
Date: 2019-01-14
---
Plots a 2D represenation of the AA sequence size and the
combinations of possible sequences.
"""
import os
import argparse
import pandas as pd
import numpy as np
import mapping_module as mm
import matplotlib
matplotlib.use('Agg')
from matplotlib import gridspec
import matplotlib.pyplot as plt
#plt.rc('text', usetex=True)
import math

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', help='The input file/directory to convert AA to nucleotides.')
parser.add_argument('-o', '--output', help='The output file/directory to save the conversion(s).')
parser.add_argument('-v', '--verbose',  help='Increase output verbosity.', action="store_true")
args = parser.parse_args()

# EXAMPLE: python plot_sequence_combinations.py -i ../data/sequence-space/ -o ../figures/proteome_combinations.pdf -v

# list all files in the directory
inputs = os.listdir(args.input)


#gs.tight_layout(fig, rect=[0, 0, 1, 0.97])

i = 0
fig = plt.figure(figsize=(12,7))
gs  = gridspec.GridSpec(1,len(inputs))
axs = []
for datum in inputs:
    organism  = datum.split('.')[0]

    if i == 0:  
        axs.append(fig.add_subplot(gs[i]))
        plt.ylabel('Number of Possible Sequence Combinations')
        plt.xlabel('AA Sequence Length')
    else: 
        axs.append(fig.add_subplot(gs[i], sharey=axs[0]))
        plt.setp(axs[i].get_yticklabels(), visible=False)
        plt.xlabel('AA Sequence Length')
    plt.setp(axs[i], title=organism[0].upper() + '. ' + organism[1:])
    axs[i].grid(True)
    df = pd.read_csv(os.path.join(args.input, datum), sep='\t')
    x = df['AA_len']
    y = [int(val) for val in df['num_combinations']]
    y = [math.log(val, 10) for val in y]
    
    less_than_uni = [1 for val in y if val <= 86]
    print(organism + ' ' + str(len(less_than_uni) / len(y)))

    plt.scatter(x=x, y=y, color=mm.colour_map[organism], alpha=0.18)
    plt.axhline(y=86, color='r', linestyle='--')
    i += 1

# Set the cutom labels - Blank First label for the bottom line
axs[0].set_yticklabels(["", r"$10^{0}$", r"$10^{2,500}$", r"$10^{5,000}$", r"$10^{7,500}$", r"$10^{10,000}$", r"$10^{12,500}$", r"$10^{15,000}$", r"$10^{17,500}$"])

fig.suptitle('Reverse Translation Sequence Combination Space', size=15)
gs.tight_layout(fig, rect=[0, 0, 1, 0.95])

plt.savefig(args.output)
plt.savefig(args.output.replace('.pdf', '.svg'))
