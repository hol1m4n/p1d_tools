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
import time

def time_convert(sec):
  mins = sec // 60
  sec = sec % 60
  hours = mins // 60
  mins = mins % 60
  print("Time Lapsed = {0}:{1}:{2}".format(int(hours),int(mins),sec))

def redshift(loc):
    z = fits.open(loc)
    val = z[2].data
    z.close()
    return val['Z'][0]

def qso_ident(loc):
    ID = fits.open(loc)
    val = ID[2].data
    ID.close()
    return val['THING_ID'][0]

local_dir="/work1/holman7/spc_fulldr14"
file="SNRinlistDR14.txt"
local_file = os.path.join(local_dir,file)
df = pd.read_csv(local_file,delim_whitespace=True, skiprows=0,dtype = {'id':str})
catlist = df['id']

print(catlist)

direc = "/work1/holman7/spc_fulldr14/"
si_list = []
no_list = []

for a in range(len(catlist)):
    if (os.path.isfile(direc+catlist[a]) == True):
        si_list.append(direc+catlist[a])
    else:
        no_list.append(direc+catlist[a])

np.savetxt('/work1/holman7/spc_fulldr14/DR14found.txt',si_list, fmt='%s', delimiter=',')
np.savetxt('/work1/holman7/spc_fulldr14/DR14not_found.txt',no_list, fmt='%s', delimiter=',')

print("Found spectra: ",len(si_list)," Not found spectra: ",len(no_list))

start_time = time.time()

limits = [1050, 1093.3, 1136.6, 1180] # (Three forest subdivisions) 
lya = 1215.67 # Lyman-a line
pxlon = [0,0,0] # Forest longitude in pixels
snr = [0,0,0] # Mean SNR value for each subforest
z_for = [0,0,0] # Mean z value for each subforest 
SNR_F = []

SNR_F.append("ID"+" plate mjd fiber" + " z_qso"+" z_fst(A)" +\
    " z_fst(B)" + " z_fst(C)"+ " SNR_fst(A)"+\
    " SNR_fst(B)" + " SNR_fst(C)"+" pxlon(A)" + " pxlon(B)"+ " pxlon(C)") 

print("Espectra to be used - ",len(si_list))
for a in range(len(si_list)):
#for a in range(100):
    file = fits.open(si_list[a])
    spectra = file[1].data
    for b in range(3):
        wave_cut=((10**spectra['loglam'])>(1. + redshift(si_list[a])) * limits[b]) \
        & ((10**spectra['loglam'])<(1. + redshift(si_list[a])) * limits[b+1])
        
        forest = spectra[wave_cut]
        
        pxlon[b] = len(forest) 
        
        if (pxlon[b]>0):
            
            raw_snr = forest['flux'] * np.sqrt(forest['ivar'])
            snr[b] = np.mean(raw_snr)
            raw_z = ((10**forest['loglam'])/lya)-1
            z_for[b] = np.mean(raw_z)
        
        else:
            
            snr[b] = None
            z_for[b] = None
                           
    file.close()   
    SNR_F.append(str(qso_ident(si_list[a]))+" "+si_list[a][38:42]+" "+si_list[a][43:48]+" "+si_list[a][49:53]+" " \
    +str(redshift(si_list[a]))+" " \
    +str(z_for[0])+" "+str(z_for[1])+" "+str(z_for[2]) \
    +" "+str(snr[0])+" "+str(snr[1])+" "+str(snr[2]) \
    +" "+str(pxlon[0])+" "+str(pxlon[1])+" "+str(pxlon[2]))
    
    snr = [0,0,0]
    z_for = [0,0,0]
    pxlon = [0,0,0]

    
np.savetxt('/work1/holman7/spc_fulldr14/SNR_fstExtraction14.txt',SNR_F, fmt='%s', delimiter=',')

SNR_process = pd.read_csv('/work1/holman7/spc_fulldr14/SNR_fstExtraction14.txt',delim_whitespace=True, \
skiprows=1, names=['ID','plate','mjd','fiber','z_qso','z_fst(A)','z_fst(B)','z_fst(C)','SNR_fst(A)',\
'SNR_fst(B)','SNR_fst(C)','pxlon(A)','pxlon(B)','pxlon(C)'])
    
TABLA = Table.from_pandas(SNR_process)
TABLA.write("/work1/holman7/spc_fulldr14/SNRForestExctDR14.fits", overwrite = True)
  
end_time = time.time() 
time_lapsed = end_time - start_time
time_convert(time_lapsed)
print('DONE-DR14')


