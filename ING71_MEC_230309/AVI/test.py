import numpy as np

from facemap.process import *
import os



wd = os.path.relpath(os.getcwd())
print(wd)
datafolder = os.path.join(wd, 'data')
print(datafolder)

resultsfolder = os.path.join(datafolder, 'resultsnpy')

proc = np.load("sample.npy", allow_pickle=True).item()

proc['savepath'] = resultsfolder

files = os.listdir(datafolder)

clean_files = [file for file in files if file[-3:] == 'avi']

for filename in clean_files[:4]:
    filename_complete = [[os.path.join(datafolder, filename)]]
    print(filename_complete)
    run(filenames=filename_complete, proc=proc, savepath=1)

# Lagt til ca under linje 705, under linjen som sier  "sx = proc["sx"]"
#            motSVD = proc['motSVD']
#            movSVD = proc["movSVD"]