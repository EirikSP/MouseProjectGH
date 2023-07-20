import numpy as np
from facemap.process import *
import os
from plotting import *

def process_wo_gui(datafolder, proc):
    """_summary_

    Args:
        datafolder (path): path to folder containing .avi-files (can contain other files as well)
        proc (dict): from saving ROIs using GUI

    Returns:
        _type_: _description_
    """

    resultsfolder = os.path.join(datafolder, 'resultsnpy')
    
    proc['savepath'] = resultsfolder

    # Retrieving the avi-files from the datafolder:
    files = os.listdir(datafolder)
    clean_files = [file for file in files if file[-3:] == 'avi']

    for filename in clean_files[4:]:
        filename_complete = [[os.path.join(datafolder, filename)]]
        run(filenames=filename_complete, proc=proc, savepath=1)
    
    return 0


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
    clean_files = [file for file in files if file[-3:] == 'npy']
    
    for filename in clean_files:
        filename_complete = os.path.join(resultfolder, filename)
        proc = np.load(filename_complete, allow_pickle=True).item()
        procs[filename[:-4]] = proc 
    
    return procs


if __name__=='__main__':

    datafolder = "/Volumes/T7/ING71_MEC_230309/AVI"
    proc = np.load("/Volumes/T7/ING71_MEC_230309/AVI/ING71_MEC_230309_000_Behav_Fr1-9973_proc.npy", allow_pickle=True).item()

    # process_wo_gui(datafolder, proc)

    resultfolder = "/Volumes/T7/ING71_MEC_230309/AVI/resultsnpy"
    procs = create_procs(resultfolder)
    
    # print(filenames)
    # print(np.argmax(procs['ING71_MEC_230309_002_Behav_Fr23897-35844_proc']['pupil'][0]['area']))
    # plot_area(procs['ING71_MEC_230309_002_Behav_Fr23897-35844_proc'])
    


    for filename in procs.keys():
        proc = procs[filename]
        plot_area(proc)


