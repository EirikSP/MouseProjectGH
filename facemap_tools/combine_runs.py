import os
import numpy as np
import sys
import scipy as sp

def combine(exp_names, base_path):

    complete_area = []
    complete_area_smooth = []

    experiment_base = exp_names[0][:20]
    behaviour_base = "D:\\mec-lec-por-data"

    num_points = len(np.load(os.path.join(behaviour_base, experiment_base + '_negative.npy'), allow_pickle=True))
    print('\nFolder order check: ')
    print(exp_names)
    print('\n')

    for name in exp_names:
        #print(name)
        full_name = os.path.join(base_path, name)
        proc = np.load(full_name, allow_pickle=True).item()
        complete_area.extend(proc['pupil'][0]['area'])
        complete_area_smooth.extend(proc['pupil'][0]['area_smooth'])
    
    complete_area = sp.signal.resample(complete_area, num_points)
    complete_area_smooth = sp.signal.resample(complete_area_smooth, num_points)

    return complete_area, complete_area_smooth

        




def combine_results_folder(base):

    save_base = os.path.join(base, 'run_based')

    print(base)

    try:
        os.mkdir(save_base)
    except:
        print("Folder already exists.")

    files = os.listdir(base)
    files.remove('run_based')
    files = sorted(files, key=len)


    while len(files)>0:
        experiment_base = files[0][:20]
        exp_filenames = [file for file in files if file[:20] == experiment_base]

        complete_area, complete_area_smooth = combine(exp_filenames, base)

        
        save_path_area = os.path.join(save_base, experiment_base + '_area.npy')
        save_path_area_smooth = os.path.join(save_base, experiment_base + '_area_smooth.npy')

        print(save_path_area)
        print(save_path_area_smooth)

        np.save(save_path_area, complete_area)
        np.save(save_path_area_smooth, complete_area_smooth)

        files = [file for file in files if file[:20] != experiment_base]



if __name__=='__main__':
    combine_results_folder(sys.argv[1])

    
