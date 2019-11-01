# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 14:15:18 2019

@author: dexte
"""

from Raman import * 
import glob 
root_location = "C:/Users/dexte/Box/Kulkarni/Raman/data/Raman_Spectra_Clinical_Samples/Raman_Spectra_Clinical_Samples/"        
folder_list = glob.glob(root_location+"*")
patients = []
for folder_name in folder_list:
    tmp_Folder = Raman_Folder("",folder_name+"/")
    patients.append(tmp_Folder) 
    tmp_Folder.plot_everything()



    
#location = "C:/Users/dexte/Box/Kulkarni/Raman/data/Raman_Spectra_Clinical_Samples/Raman_Spectra_Clinical_Samples/20181115-22/"        
#file_name = "20191015_SebStripe_20181115-22_trypsin_100x_dilution_on_20mM_Cysteamine_Wash_WetState_60X_4mW_SPOT1_2.txt"
#filename_list= [location,file_name]
#filename_string = "".join(filename_list)
#test = Raman_Spot(filename_string)

#testing raman folder class

#root_location = "C:/Users/dexte/Box/Kulkarni/Raman/data/Raman_Spectra_Clinical_Samples/Raman_Spectra_Clinical_Samples/"        
#folder_name = "20181115-22/"

#Folder_test = Raman_Folder(root_location,folder_name)
#Folder_test.plot_everything()

##spot_index = name.find("SPOT",0,len(name))
#print(name[spot_index+4:spot_index+7])