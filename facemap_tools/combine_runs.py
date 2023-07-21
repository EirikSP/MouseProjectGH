import os
import numpy as np
import sys
import scipy as sp

def combine(exp_names, results_folder, behaviour_base="D:\\mec-lec-por-data"):
    """
    Extracts the area and area_smooth arrays from the files in the exp_names list and concatenates them.

    Args:
        exp_names - List of names of processed experiment files to be combined.\n
        results_folder - A global path to the folder containing the processed experiment files.\n
        behaviour_base - The global path to the folder containing the behaviour data.\n
    
    Returns:
        complete_area - Concatenated list of all area arrays from files given in exp_names.\n
        complete_area_smooth - Concatenated list of all area_smooth arrays from files given in exp_names.
    
    """

    complete_area = []
    complete_area_smooth = []

    experiment_base = exp_names[0][:20]

    num_points = len(np.load(os.path.join(behaviour_base, experiment_base + '_negative.npy'), allow_pickle=True))
    print('\Run concatenation order check: ')
    print(exp_names)
    print('\n')

    for name in exp_names:
        full_name = os.path.join(results_folder, name)
        proc = np.load(full_name, allow_pickle=True).item()
        complete_area.extend(proc['pupil'][0]['area'])
        complete_area_smooth.extend(proc['pupil'][0]['area_smooth'])
    
    complete_area = sp.signal.resample(complete_area, num_points)
    complete_area_smooth = sp.signal.resample(complete_area_smooth, num_points)

    return complete_area, complete_area_smooth

        




def combine_results_folder(results_folder):
    """
    Takes a folder of processed experiment files(.npy) and extracts the area and area_smooth arrays from all files. Concatenates the arrays that are from the same run and saves them at "results_folder/run_based/{experiment_run_name: Typically like "ING7...230915_003"}_area.npy"\n
    
    Args:
        results_folder - A global path to a folder containing processed experiment files(.npy)
    """

    save_run_based = os.path.join(results_folder, 'run_based')


    try:
        os.mkdir(save_run_based)
    except:
        print("Folder already exists.")

    files = os.listdir(results_folder)
    files.remove('run_based')
    files = sorted(files, key=len)


    while len(files)>0:
        experiment_base = files[0][:20]
        exp_filenames = [file for file in files if file[:20] == experiment_base]

        complete_area, complete_area_smooth = combine(exp_filenames, results_folder)

        
        save_path_area = os.path.join(save_run_based, experiment_base + '_area.npy')
        save_path_area_smooth = os.path.join(save_run_based, experiment_base + '_area_smooth.npy')

        print(save_path_area)
        print(save_path_area_smooth)

        np.save(save_path_area, complete_area)
        np.save(save_path_area_smooth, complete_area_smooth)

        files = [file for file in files if file[:20] != experiment_base]



if __name__=='__main__':
    combine_results_folder(sys.argv[1])

    
