import numpy as np
#from process.py import process
from facemap.process import *
import os


proc = np.load("sample.npy", allow_pickle=True).item()

files = os.listdir()

clean_files = [file for file in files if file[-2:] == 'vi']

for filename in clean_files:
    filename_complete = [[filename]]
    print(filename_complete)
    run(filenames=filename_complete, proc=proc)

# Lagt til ca under linje 705, under linjen som sier  "sx = proc["sx"]"
#            motSVD = proc['motSVD']
#            movSVD = proc["movSVD"]
