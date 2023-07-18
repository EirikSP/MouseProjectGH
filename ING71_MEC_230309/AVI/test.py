import numpy as np
#from process.py import process
from facemap.process import *
import os


proc = np.load("ING71_MEC_230309\AVI\sample.npy", allow_pickle=True).item()


files = os.listdir('ING71_MEC_230309\AVI')

clean_files = [file for file in files if file[-2:] == 'vi']


for filename in clean_files:
    filename_complete = [[".\ING71_MEC_230309\AVI\\" + filename]]
    print(filename_complete)
    run(filenames=filename_complete, proc=proc)

# Lagt til ca under linje 705, under linjen som sier  "sx = proc["sx"]"
#            motSVD = proc['motSVD']
#            movSVD = proc["movSVD"]