#!/usr/bin/python
""" proteoLSTM.py
Author: Kevin Dick
Date: 2018-11-24
---
Creating a basic LSTM to generate protein amino acid sequences.
"""
import numpy
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import LSTM
from keras.callbacks import ModelCheckpoint
from keras.utils import np_utils
import os, sys

# Constants
SEQ_LENGTH = 100
CKPT_DIR   = './checkpoints/'

# Load protein amino acids and covert to lowercase
filename = "../data/aa-seqs/merged_sequences.txt"
raw_text = open(filename).read().lower()

# Create mapping from unique Amino Acid character to integer
chars = sorted(list(set(raw_text)))
char_to_int = dict((c, i) for i, c in enumerate(chars))

# summarize the loaded data
n_chars = len(raw_text)
n_vocab = len(chars)
print "Total Characters: ", n_chars
print "Total Vocab: ", n_vocab
sys.exit(0)

# prepare the dataset of input to output pairs encoded as integers
dataX = []
dataY = []
for i in range(0, n_chars - SEQ_LENGTH, 1):
    seq_in = raw_text[i:i + SEQ_LENGTH]
    seq_out = raw_text[i + SEQ_LENGTH]
    dataX.append([char_to_int[char] for char in seq_in])
    dataY.append(char_to_int[seq_out])
n_patterns = len(dataX)
print "Total Patterns: ", n_patterns

# reshape X to be [samples, time steps, features]
X = numpy.reshape(dataX, (n_patterns, SEQ_LENGTH, 1))

# normalize
X = X / float(n_vocab)

# one hot encode the output variable
y = np_utils.to_categorical(dataY)

# define the LSTM model
model = Sequential()
model.add(LSTM(256, input_shape=(X.shape[1], X.shape[2]), return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(256))
model.add(Dropout(0.2))
model.add(Dense(y.shape[1], activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam')
# define the checkpoint
filepath = os.path.join(CKPT_DIR, "weights-improvement-{epoch:02d}-{loss:.4f}-bigger.hdf5")
checkpoint = ModelCheckpoint(filepath, monitor='loss', verbose=1, save_best_only=True, mode='min')
callbacks_list = [checkpoint]
# fit the model
model.fit(X, y, epochs=50, batch_size=64, callbacks=callbacks_list)

print 'Execution Complete!~'
