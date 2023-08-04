import numpy as np 
import matplotlib.pyplot as plt 
import os
import sys 
import scipy as sp

from collections import OrderedDict
from sklearn.preprocessing import minmax_scale 

#Should we have a class for proc as well or are we only really interested in the area? I guess we found out that there wasnt that much else interesting to look at in proc...


class H_Plotter:
    def __init__(self) -> None:
        pass

    def plot_area(self, area):
        pass

    def plot_area_with_behav(self, area, behav):
        pass 


class Area_analysis:
    def __init__(self, folder_path):
        # Currently uncertain which folder it should take in (depends on runwise vs seperate)
        self.folder_path = folder_path
        self.area = None

        #Should perhaps create a base (to extract )

    def load_area_data(self, area_smooth=True):
        #This could return runwise or one for each avi-file
            #The pros with returning per avi-file is that it is easy to compare with the gui afterwards. (Depends on whether)
            #When combining with behavioral data it has to be runwise 
        #What should area be? A dictionary with eg '000' as a key? Think indexing is out of the question as we have parallelization. self.area could also be an array; then we have to give a run_idx! I think it is best to keep it as an dictionary so that we dont end up with lots of objects. Should perhaps then have loops going through the dictionary. NB! Remember to organize it! Should perhaps call it self.areas
        #If we have runwise as a argument and we use runwise=False we could end up with some nasty error msg if the rest of the class is taylored to runwise (might need a lot of try/except)
            #Perhaps we could have a own method for loading non-runwise (?) I think that is a good idea! 
        #Should we load area or area_smooth (?). Could take it in as an argument and save it in self so that we can see afterwards 

        # self.area_smooth = area_smooth
        # areas_sorted = OrderedDict(sorted(areas.items()))

        pass

    def load_gui_wise(self, area_smooth=True):
        #Its own function for returning areas corresponding to those in the gui (have to assume some things about the file structure (or take folder as an argument))
        #It could also make self.area to be gui_wise (overwrite)
        #Perhaps this should also be a dictionary. Could have run and frames as keys?
        pass 

    def select_areas(self):
        #A method for choosing which areas to further explore. Could overwrite self.areas (?) or create a self.selected_areas. 
            #If we overwrite we could make sure that it will be possible to "undo" without having to create a new object 
                #(could call load_area_data)
        pass

    # Preprocessing: 
    def remove_outliers(self):
        pass 

    def smooth(self):
        pass 

    
    # FFT 
    def FFT_area(self):
        pass 

    
    # Possible simple plotting included in this class: 
    def plot_area(self):
        plotter = H_Plotter()
        plotter.plot_area(self.area) #NB! Here we have assumed that area is an array!




class Behav_analysis(Area_analysis):
    def __init__(self, folder_path):
        super().__init__(folder_path)
        self.behav = None

    def load_behva_data(self, behav_folder):
        pass 

    def downsample(self):
        #Use self.area, NB here it is important that area is runwise!
        pass 

    # Possible simple plotting included in this class: 
    def plot_area_with_behav(self):
        plotter = H_Plotter()
        plotter.plot_area_with_behav(self.area, self.behav)

