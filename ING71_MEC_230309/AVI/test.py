import numpy as np

from facemap.process import *
import os
import sys



#wd = os.path.relpath(os.getcwd())

datafolder = "D:\ING71_MEC_230314\AVI"
#datafolder = os.path.join(wd, 'data')

input_foldername = sys.argv[1]



def process_folder(datafolder_global_path):
    resultsfolder = os.path.join(datafolder_global_path, 'resultsnpy')
    try:
        os.mkdir(resultsfolder)
    except:
        print("Folder already exists.")

    #Loads the "settings" file for the processing and sets the savepath to be "/.../.../datafolder_global_path/resultsnpy"
    proc = np.load("sample.npy", allow_pickle=True).item()
    proc['savepath'] = resultsfolder

    #Finds all elements in datafolder.
    files = os.listdir(datafolder_global_path)
    clean_files = []

    #Checks for .avi files and catches exception if filenames are shorter than 4 letters.
    for file in files:
        try:
            if file[-4:] == ".avi":
                clean_files.append(file)
        except:
            print('Invalid file name')

    #Formats filename and processes avi file, saving the resulting file in the "resultsnpy" folder in the same location.
    for filename in clean_files:
        filename_complete = [[os.path.join(datafolder, filename)]]
        print(filename_complete)
        run(filenames=filename_complete, proc=proc, savepath=1)

# Lagt til ca under linje 705, under linjen som sier  "sx = proc["sx"]"
#            motSVD = proc['motSVD']
#            movSVD = proc["movSVD"]

process_folder(input_foldername)