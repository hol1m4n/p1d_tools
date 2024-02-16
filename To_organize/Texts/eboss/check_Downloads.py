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

direc = os.getcwd()
print("List of spectra on disk:")


list_raw = os.listdir(os.getcwd())
list_raw = np.array(list_raw)
finder = np.char.find(list_raw, "spclist_fc", start=0, end=None)

BOOL = [True if x >= 0 else False for x in finder]

LIST = list_raw[BOOL]

for x in range(len(LIST)):
    print(f'[{x}].{LIST[x]}\n')




file= int(input("Choose the file to be evaluated:"))
local_file = os.path.join(direc,LIST[file])
df = pd.read_csv(local_file,delim_whitespace=True, skiprows=0,dtype = {'id':str})
catlist = df['id']

print(f"Files on list: {len(catlist)}")

direc = str(os.getcwd())+'/'

si_list = []
no_list = []

for a in range(len(catlist)):
    if (os.path.isfile(direc+catlist[a]) == True):
        si_list.append(direc+catlist[a])
    else:
        no_list.append(direc+catlist[a])


print(f"Files on disk: {len(si_list)}")


np.savetxt(str(direc)+'/['+str(file)+']_found.txt',si_list, fmt='%s', delimiter=',')
np.savetxt(str(direc)+'/['+str(file)+']_notfound.txt',no_list, fmt='%s', delimiter=',')


