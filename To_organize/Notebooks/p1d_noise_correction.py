import os
import sys
import glob
import numpy as np
import scipy.optimize    as op
import matplotlib.pyplot as plt
import urllib.request
from astropy.io import fits
from astropy.table import Table
from scipy.interpolate import make_interp_spline
import fitsio


# ---- Function to modify the Pk1D- files

def noise_calc_fits(folder,file,c1,c2): # c1 & c2 are counters
    path = os.path.join(folder,str(file)) # Path to a given file
    fits_file = fits.open(path) # Open .fits file to retrieve HDUs 
    
    with fits.open(path, mode='update') as hdus:
        for i in range(len(fits_file)): # Loop for number of HDUs in the P1D file
            if (i>0): # Skip PrimaryHDU 
                mean_z = fits_file[i].header['MEANZ'] # Retrieving the MEANZ value for this chunk
                if (mean_z <= 2.7): # Considering only the first three redshift bins
                    T = Table.read(hdus[i])
                    T['PK_DIFF'] = T["PK_DIFF"]*0.95 # Applying Beta correction
                    up_hdu = fits.BinTableHDU(data = T, header = fits_file[i].header) #updated BinTableHDU
                    hdus[i] = up_hdu # Adding to the original HDU
                else:
                    pass
            else:
                pass
        hdus.flush() # Saving the update
    print(f"{str(file)} noise correction updated : file {c1}/{c2}")




# ---- Function looping for all files

def p1d_noise_set(folder, name_list):
    n_f =  len(name_list) #n_f = Number of files on folder
    for b in range(n_f):
        noise_calc_fits(folder,name_list[b],b+1,n_f) # Applying the correction for all files
    print(f"Done for all files({n_f})")



# ---- List of files to be modified

folder = "/home/colgoat/PSChab/run5_n"
list_raw = os.listdir(folder)
list_raw.sort()
name_list = np.array(list_raw)
ff = np.char.find(name_list, ("Pk1D-" and ".fits"), start=0, end=None) ## ff = Names' flaws finder
for i in range(len(list_raw)):
    if (ff[i]==(-1)):
        name_list = np.delete(name_list,i) # Removing files that are not Pk1D-(A,B,C).fits
print(name_list, len(name_list)) # Final list



p1d_noise_set(folder,name_list) # Calling functions