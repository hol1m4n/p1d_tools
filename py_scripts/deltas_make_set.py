import os
import os.path
import sys
import glob
import numpy as np
import scipy.optimize    as op
import matplotlib.pyplot as plt
import urllib.request
from astropy.io import fits 
from astropy.table import Table
import pandas as pd
import shutil


path = os.getcwd()

set_folder = '/set_fP1D/'


if (os.path.exists(path+set_folder) == True):
    print('Folder for deltas set already created \n')
else:
    print('Folder for deltas set created (set_fP1D) \n')
    os.mkdir(path+set_folder)
    
    
D_folders = ['/A/Delta/','/B/Delta/','/C/Delta/']
fst = ['_A','_B','_C']

final_list = 0

for x in range(len(fst)):
    
    list_raw = os.listdir(path+D_folders[x])
    
    files = []
    
    for a in range(len(list_raw)):
        if (str(list_raw[a][0:6])=="delta-"):
            files.append(list_raw[a])
        
    labeled = 0
    not_label = 0
    
    print(f'Copying relabeled files to: {path+set_folder}')

    for b in range(len(files)):
        if (len(str(files[b]))==15):
            new_name = str(files[b])[0:7] + fst[x] +".fits.gz"
            shutil.copyfile(path+D_folders[x]+files[b],path+set_folder+new_name)
            labeled = labeled + 1
        if (len(str(files[b]))==16):
            new_name = str(files[b])[0:8] + fst[x] +".fits.gz"
            shutil.copyfile(path+D_folders[x]+files[b],path+set_folder+new_name)
            labeled = labeled + 1
        if (len(str(files[b]))==17):
            new_name = str(files[b])[0:9] + fst[x] +".fits.gz"
            shutil.copyfile(path+D_folders[x]+files[b],path+set_folder+new_name)
            labeled = labeled + 1
    
    final_list = labeled + final_list

    
    print(f'Files relabeled for {fst[x][1:3]}: {labeled} \n')
    


print(f'Final list moved:{final_list}')

final_list = os.listdir(path+set_folder)

print(f'Final list evaluated on folder:{len(final_list)}')