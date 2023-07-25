import numpy as np


import os
import sys
sys.path.append(os.path.join(os.getcwd(), '..'))
from facemap.process import *
from facemap_tools.combine_runs import combine_results_folder




def process_folder(datafolder_global_path, proc_path=None):
    """
    Args:
        datafolder_global_path - The global path of the folder that contains the video files.
        proc_path - Optional global path for the file that contains the settings for the processing of the video files. Defaults to "datafolder_global_path/{Name for mouse and day: first 16 letters of video files}_sample.npy"
    """
    resultsfolder = os.path.join(datafolder_global_path, 'resultsnpy')
    try:
        os.mkdir(resultsfolder)
    except:
        print("Folder already exists.")

    #Loads the "settings" file for the processing and sets the savepath to be "/.../.../datafolder_global_path/resultsnpy"

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
    
    if(proc_path is not None):
        proc = np.load(proc_path, allow_pickle=True).item()
    else:
        #Gets the sample file from a file similar to "/.../.../datafolder_global_path/ING....2309010_sample.npy"
        proc = np.load(os.path.join(datafolder_global_path, clean_files[0][:16] + '_sample.npy'), allow_pickle=True).item()
    proc['savepath'] = resultsfolder

    #Formats filename and processes avi file, saving the resulting file in the "resultsnpy" folder in the same location.
    for filename in clean_files:
        filename_complete = [[os.path.join(datafolder_global_path, filename)]]
        print(filename_complete)
        run(filenames=filename_complete, proc=proc, savepath=1)



def process_folder_combine_runs(datafolder_global_path, proc_path=None):
    """
    Runs process_folder and then runs combine_results_folder.
    Processes all video files to npy files and then extracts the area and area_smooth values from the segmented experiment runs and concatenates them into one arrays for a singular run. Then saves the combined runs in "datafolder_global_path/resultsnpy/run_based"

    Args:
        datafolder_global_path - The global path of the folder that contains the video files.
        proc_path - Optional global path for the file that contains the settings for the processing of the video files. Defaults to "datafolder_global_path/{Name for mouse and day: first 16 letters of video files}_sample.npy"
    """
    process_folder(datafolder_global_path, proc_path=proc_path)
    results_folder = os.path.join(datafolder_global_path, 'resultsnpy')
    combine_results_folder(results_folder)






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


def create_areas(resultfolder):
    """NB, the returned dictionaries are not necessarily sorted. Parallelization<3

    Args:
        resultfolder (_type_): _description_

    Returns:
        _type_: _description_
    """
    areas = {}
    areas_smooth = {}

    files = os.listdir(resultfolder)
    area_files = []
    area_smooth_files = []

    for file in files:
        try:
            if file[-8:] == "area.npy":
                area_files.append(file)
            elif file[-10:] == "smooth.npy":
                area_smooth_files.append(file)
        except:
            print(f"{file} is an invalid file name")

    for filename in area_files:
        filename_complete = os.path.join(resultfolder, filename)
        area = np.load(filename_complete, allow_pickle=True)
        areas[filename[17:20]] = area 

    for filename in area_smooth_files:
        filename_complete = os.path.join(resultfolder, filename)
        area_smooth = np.load(filename_complete, allow_pickle=True)
        areas_smooth[filename[17:20]] = area_smooth 

    return areas, areas_smooth



if __name__ == '__main__':
    input_foldername = sys.argv[1]
    try:
        proc_path = sys.argv[2]
        process_folder_combine_runs(input_foldername, proc_path=proc_path)
    except:
        process_folder_combine_runs(input_foldername)


