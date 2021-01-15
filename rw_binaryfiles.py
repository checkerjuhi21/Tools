'''
Following code will allow you to read and write into a binary file
'''

# To open a binary file
import numpy as np
# Here the input is in 1-D array so we need to convert it into our required dimensions
T = np.fromfile('file_name.bin',  dtype=np.float32)
# To change 1-D into the required dimension
T= T.reshape(row,col)

# To write into a binary file
# Reshape the array into 1-D again
T = T.reshape(-1)
# Open the binary file you want to write in 
f = open("file_name.bin", "bw")
# finally write into the file using .tofile from numpy library
T.tofile(f)
