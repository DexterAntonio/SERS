# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 11:42:32 2019

@author: dexte
"""
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np    
import glob as glob 

class Raman_Spot:
    """An class to store SERS data and analyze it """
    def __init__(self, filename): #initalizes a Raman object from a text file 
        #initilize atributes 
        self.files_location = "C:/Users/dexte/Box/Kulkarni/Raman/data/Raman_Spectra_Clinical_Samples/Raman_Spectra_Clinical_Samples/20181115-22/" 
        self.metadata_values = {}
        self.data_list = []
        self.filename_string = filename 
        self.average_spectra = np.zeros((1024,2),dtype=float)        
        
        with open(filename_string) as infile:
            self.metadata_values = self.get_metadata(infile)
            self.data_list = self.get_file_spectra(infile)
       
        self.average_spectra = self.get_average()
        
    def get_metadata(self,file_iterator):
        metadata_values = {} #creates dictionary to return 
        for line in file_iterator:
            if(line=="\n"): #determines when metadata ends and spectra data begins 
                return metadata_values
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
                    continue 
                else:
                    if(c=="\n"): #skip newline characters 
                        continue 
                    data_values.append(c)
                    continue 
                
            metadata_values["".join(data_name)]="".join(data_values) #adds name and value to a dictionary 
        print("something is wrong with get_metadata")
        return metadata_values  
    
    def get_file_spectra(self,file_iterator):
        i =0 
        data_list = []
        data_array = np.zeros((1024,2),dtype=float) #this is for storing the data 

        for line in file_iterator: 
            if(line=="\n"): #skips new line characters at the begining of the file 
                continue 
            splt_line = line.split("	")
            if(len(splt_line) != 3): #skips nondata 
                print("I am called")
                print(line)
                continue 
            #if you go through one whole dataset  if(len(wavelength_list)!=0 and wavelength<wavelength_list[-1]): #if the wavelengths go back to the start point, restart things 
            if(i>=1024):
                data_list.append(data_array)
                data_array = np.zeros((1024,2),dtype=float) #clears data array for next round 
                i = 0 
            wavelength = float(splt_line[0])
            intensity = float(splt_line[1])
            data_array[i,0] = wavelength
            data_array[i,1] = intensity
         
            i += 1
        return data_list 
    def get_average(self):
        average_data_array = np.zeros((1024,2),dtype=float)
        for arr in self.data_list:
            average_data_array += arr 
        average_data_array = average_data_array/len(self.data_list)
        return average_data_array
    def plot_average(self,fig_number=1):
        plt.figure(num=fig_number, figsize=(10, 7.5), dpi=80, facecolor='w', edgecolor='k')
        x = self.average_spectra[:,0]
        y = self.average_spectra[:,1]
        plt.plot(x,y,'-',linewidth=2.0,color='k')
    def plot_all(self):
        plt.figure(num=2, figsize=(10, 7.5), dpi=80, facecolor='w', edgecolor='k')
        x = self.average_spectra[:,0]
        y = self.average_spectra[:,1]
        i = 0 
        for d in test.data_list:
           i += 1 
           plt.plot(d[:,0],d[:,1],label=i)
        plt.plot(x,y,'-',linewidth=7.0,color='k',label="average")
        plt.legend()

class Raman_Folder:
    def __init__(self,root_location,folder_name):
        glob_cmd = root_location+folder_name+"*.txt"
        self.file_list = glob.glob(glob_cmd)
        self.raman_spot_dict = {}
        for filename in self.file_list:
            spot_index = filename.find("SPOT",0,len(name))
            key = filename[spot_index+4:spot_index+7]
            self.raman_spot_dict[key] = Raman_Spot(filename)
    def plot_everything(self):
        avearge_list = []
        name_list = []
        plt.figure(num=2, figsize=(10, 7.5), dpi=80, facecolor='w', edgecolor='k')
        for key, raman_spot in self.raman_spot_dict.items():
            avearge_list.append(raman_spot.get_average())
            name_list.append(key)
        i = 0
        for avg in avearge_list:
            plt.plot(avg[:,0],avg[:,1]+i*100,'-',label=name_list[i])
            print(i)
            i+= 1
        plt.legend()
    def plot_specific_spot(self,f)
        #print(file_list)
 
       
location = "C:/Users/dexte/Box/Kulkarni/Raman/data/Raman_Spectra_Clinical_Samples/Raman_Spectra_Clinical_Samples/20181115-22/"        
file_name = "20191015_SebStripe_20181115-22_trypsin_100x_dilution_on_20mM_Cysteamine_Wash_WetState_60X_4mW_SPOT1_2.txt"
filename_list= [location,file_name]
filename_string = "".join(filename_list)
#test = Raman_Spot(filename_string)

#testing raman folder class

root_location = location = "C:/Users/dexte/Box/Kulkarni/Raman/data/Raman_Spectra_Clinical_Samples/Raman_Spectra_Clinical_Samples/"        
folder_name = "20181115-22/"

Folder_test = Raman_Folder(root_location,folder_name)
Folder_test.plot_everything()

##spot_index = name.find("SPOT",0,len(name))
#print(name[spot_index+4:spot_index+7])
#test = Raman_Spot(name)

#plt.figure(num=2, figsize=(10, 7.5), dpi=80, facecolor='w', edgecolor='k')
#avgxy = test.get_average()
#i = 0 
#for d in test.data_list:
#   i += 1 
#   plt.plot(d[:,0],d[:,1],label=i)
#plt.legend()
#plt.plot(avgxy[:,0],avgxy[:,1],'-',linewidth=7.0,color='k')
#
#    

#plt.plot(test.wavelength_list,test.intensity_list,'-')
#for i in range(0,len())