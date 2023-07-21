import numpy as np
from facemap.process import *
import os
import sys



#wd = os.path.relpath(os.getcwd())

#datafolder = "D:\ING71_MEC_230314\AVI"
#datafolder = os.path.join(wd, 'data')


def process_folder(datafolder_global_path, proc_path):
    resultsfolder = os.path.join(datafolder_global_path, 'resultsnpy')
    try:
        os.mkdir(resultsfolder)
    except:
        print("Folder already exists.")

    #Loads the "settings" file for the processing and sets the savepath to be "/.../.../datafolder_global_path/resultsnpy"
    proc = np.load(proc_path, allow_pickle=True).item()
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
        filename_complete = [[os.path.join(datafolder_global_path, filename)]]
        print(filename_complete)
        run(filenames=filename_complete, proc=proc, savepath=1)


def create_procs(resultfolder):
    """Creating proc-objects from resultfolders (which contain npy-files)

    Args:
        resultfolder (_type_): _description_

    Returns:
        procs (dict): Contain all the proc-arrays. The keys are the filenames (without .avi)
        filenames (list): Contain all the filenames that are in the proc. Think this can be dropped as procs.keys() is equivalent. Now removed.
    """
    procs = {}

    files = os.listdir(resultfolder)
    clean_files = []

    #Checks for .avi files and catches exception if filenames are shorter than 4 letters.
    for file in files:
        try:
            if file[-4:] == ".npy":
                clean_files.append(file)
        except:
            print('Invalid file name')
    
    for filename in clean_files:
        filename_complete = os.path.join(resultfolder, filename)
        proc = np.load(filename_complete, allow_pickle=True).item()
        procs[filename[:-4]] = proc 
    
    return procs



if __name__ == '__main__':
    input_foldername = sys.argv[1]
    proc_path = sys.argv[2]

    process_folder(input_foldername)
