# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 11:42:32 2019

@author: dexte
"""
import pandas as pd 
import matplotlib.pyplot as plt

class Raman :
    """An class to store SERS data and analyze it """
    files_location = "C:/Users/dexte/Box/Kulkarni/Raman/data/Raman_Spectra_Clinical_Samples/Raman_Spectra_Clinical_Samples/20181115-22/" 
    def __init__(self, filename):
        self.data_dict = {}
        self.wavelength_list = []
        self.intensity_list= []
        self.filename = filename 
        filename_list= [self.files_location,self.filename]
        filename_string = "".join(filename_list)
        File_object = open(filename_string,"r")
        lines = File_object.readlines()
        self.metadata_values = {}
        on_metadata = True 
        #this code is for processing the metadata and storing it in a dictionary 
        self.wavelength_dict = {}
        run_number = 1 
        for line in lines:
            if(line=="\n"):
                on_metadata = False 
                continue 
            if(on_metadata):
                data_name = []
                data_values = []
                colon_encountered = False 
                iterline = iter(line)
                for c in iterline: 
                    if(not colon_encountered and c==":"):
                        colon_encountered = True  
                        c = next(iterline) 
                        while(c==" "):
                            c = next(iterline) #iterates through all whitespace between key and date 
                            
                    if (not colon_encountered): #if you are iterating through the key 
                        data_name.append(c)
                    else:
                        if(c=="\n"): #skip newline characters 
                            continue 
                        data_values.append(c)
                    
                self.metadata_values["".join(data_name)]="".join(data_values)
            #processing numerical data 
            splt_line = line.split("	")
            if(len(splt_line) != 3):
                continue 
            wavelength = float(splt_line[0])
            intensity = float(splt_line[1])
            
            if(len(self.wavelength_list)!=0 and wavelength<self.wavelength_list[-1]): #if the wavelengths go back to the start point, restart things 
                self.data_dict[run_number] = (self.wavelength_list,self.intensity_list)
                run_number += 1 
                self.wavelength_list = []
                self.intensity_list = []
                #break 
            #[wavelength,intensity] = line.split("	")
            self.wavelength_list.append(wavelength)
            self.intensity_list.append(intensity)
            
            
            #self.wavelength_dict[wavelength]=intensity 
                       
        
      
test = Raman("20191015_SebStripe_20181115-22_trypsin_100x_dilution_on_20mM_Cysteamine_Wash_WetState_60X_4mW_SPOT1_2.txt")
plt.figure(num=None, figsize=(20, 15), dpi=80, facecolor='w', edgecolor='k')
d = test.data_dict
for k in d.keys():
    xy = d[k]
    x = xy[0]
    y = xy[1]
    plt.plot(x,y,'-')

#plt.plot(test.wavelength_list,test.intensity_list,'-')
#for i in range(0,len())