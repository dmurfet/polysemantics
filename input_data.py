# Copyright 2016 Daniel Murfet

"""Functions for translating output of Singular to numpy data"""

import os
import numpy

# http://stackoverflow.com/questions/379906/parse-string-to-float-or-int
# we can read a string and just call int( ) on each of the strings to read out
# then we conver to a numpy array

# so we just need to read a string from a file
#https://github.com/tensorflow/tensorflow/blob/r0.7/tensorflow/examples/tutorials/mnist/input_data.py

def extract_data(filename):
  """Extract the data into a numpy array."""
  print('Extracting', filename)

    data = numpy.frombuffer(buf, dtype=numpy.uint8)
    data = data.reshape(num_images, rows, cols, 1)
    return data