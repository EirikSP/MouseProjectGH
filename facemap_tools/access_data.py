import numpy as np
import os 


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
