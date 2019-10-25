# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 11:42:32 2019

@author: dexte
"""
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np 

class Raman :
    """An class to store SERS data and analyze it """
    files_location = "C:/Users/dexte/Box/Kulkarni/Raman/data/Raman_Spectra_Clinical_Samples/Raman_Spectra_Clinical_Samples/20181115-22/" 
    def __init__(self, filename):
        #initilize atributes 
        self.metadata_values = {}
        self.data_dict = {}
        self.data_list = []
        self.filename = filename 
        
        #build filename strings 
        filename_list= [self.files_location,self.filename]
        filename_string = "".join(filename_list)
        
        File_object = open(filename_string,"r") #load file 
        lines = File_object.readlines() #build iterator
        
        #these lists are for storing the data into dictionaries 
        wavelength_list = []
        intensity_list= []
        
        data_array = np.zeros((1024,2),dtype=float)
        #intensity_array = np.zeros((1024,),dtype=float)

        
        on_metadata = True 
        #this code is for processing the metadata and storing it in a dictionary 
        run_number = 1 
        filename_list= [self.files_location,self.filename]
        filename_string = "".join(filename_list)
        File_object = open(filename_string,"r")
        lines = File_object.readlines()
        i = 0 
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
            if(len(wavelength_list)!=0 and wavelength<wavelength_list[-1]): #if the wavelengths go back to the start point, restart things 
                print(i)
                self.data_dict[run_number] = (wavelength_list,intensity_list)
                self.data_list.append(data_array)
                data_array = np.zeros((1024,2),dtype=float)
                run_number += 1 
                wavelength_list = []
                intensity_list = []
                i = 0 

                #break 
            #[wavelength,intensity] = line.split("	")
            wavelength_list.append(wavelength)
            intensity_list.append(intensity)
            data_array[i,0] = wavelength
            data_array[i,1] = intensity
            i += 1 

            #self.wavelength_dict[wavelength]=intensity 
                    
      
test = Raman("20191015_SebStripe_20181115-22_trypsin_100x_dilution_on_20mM_Cysteamine_Wash_WetState_60X_4mW_SPOT1_2.txt")
plt.figure(num=2, figsize=(20, 15), dpi=80, facecolor='w', edgecolor='k')
d = test.data_dict
#for k in d.keys():
i = 0 
for d in test.data_list:
    i += 1 
    #xy = d[k]
    #x = xy[0]
    #y = xy[1]
    #plt.plot(x,y,'-')
    plt.plot(d[:,0],d[:,1],label=i)
plt.legend()
    

#plt.plot(test.wavelength_list,test.intensity_list,'-')
#for i in range(0,len())