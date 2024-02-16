# Importing libraries 
import os
import sys
import glob
import numpy as np
import scipy.optimize as op
import matplotlib.pyplot as plt
import urllib.request
from astropy.io import fits
from astropy.table import Table
from astropy.table import vstack
from astropy.io import fits
import urllib.request
import requests
import time


#Getting the individual coadded files names

local_dir = "/work1/holman7/spc_DESIedrS/" #path to the catalogs
pn_sv1 = "https://data.desi.lbl.gov/public/edr/spectro/redux/fuji/healpix/sv1/dark/" # File database link for sv1
pn_sv3 = "https://data.desi.lbl.gov/public/edr/spectro/redux/fuji/healpix/sv3/dark/" # File database link for sv3

EDR_qsolist = [] # List of spectra of interest from DESI EDR

print("\n")
print("---------------------------------------------")
print("\n")

file1 = "QSO_cat_fuji_sv1_dark_bal_mask_v1.0.fits" # Name of the first catalog (sv1)
lc_sv1 = os.path.join(local_dir,file1) # lc_sv1 = Local file sv1
fc_sv1 = fits.open(lc_sv1) # fc_sv1 = Open .fits catalog file of sv1
SV1 = Table.read(fc_sv1) # SV1 = Reading the file of SV1 as a BinTable 
q_sv1 = (SV1['Z']>=2.1) & (SV1['PROGRAM']=='dark') # q_sv1 = Query from main catalog (filtering)
catfil_sv1 = SV1[q_sv1] # catfil_sv1 = Filtered catalog sv1
catfil_sv1_hpix = catfil_sv1.group_by("HPXPIXEL") # catfil_sv1 = Grouping filtered catalog by HEALPIX criteria
HPX_sv1 = catfil_sv1_hpix["HPXPIXEL"]/100 # HPX_sv1 = Getting the healpix ID for path on database

print("Number of spectra in SV1: ",len(catfil_sv1)) # Showing the number of targets on screen
for p,m in zip(HPX_sv1,catfil_sv1_hpix["HPXPIXEL"]): # Adding selected Targets to the list
    EDR_qsolist.append(pn_sv1+str(int(p))+"/"+str(m)+"/coadd-sv1-dark-"+str(m)+".fits")
fc_sv1.close()

file2 = "QSO_cat_fuji_sv3_dark_bal_mask_v1.0.fits" # Name of the first catalog (sv3)
lc_sv3 = os.path.join(local_dir,file2) # lc_sv3 = Local file sv3
fc_sv3 = fits.open(lc_sv3) # fc_sv3 = Open .fits catalog file of sv3
SV3 = Table.read(fc_sv3) # SV3 = Reading the file of SV3 as a BinTable
q_sv3 = (SV3['Z']>=2.1) & (SV3['PROGRAM']=='dark') # q_sv3 = Query from main catalog (filtering)
catfil_sv3 = SV3[q_sv3] # catfil_sv3 = Filtered catalog sv3
catfil_sv3_hpix = catfil_sv3.group_by("HPXPIXEL") # catfil_sv3 = Grouping filtered catalog by HEALPIX criteria
HPX_sv3 = catfil_sv3_hpix["HPXPIXEL"]/100 # HPX_sv3 = Getting the healpix ID for path on database

print("Number of spectra in SV3: ",len(catfil_sv3))
for p,m in zip(HPX_sv3,catfil_sv3_hpix["HPXPIXEL"]): # Adding selected Targets to the list
    EDR_qsolist.append(pn_sv3+str(int(p))+"/"+str(m)+"/coadd-sv3-dark-"+str(m)+".fits")
fc_sv3.close()


EDRcat_stk = vstack(([catfil_sv1_hpix,catfil_sv3_hpix])) # EDR filtered catalogs stacked for both surveys and sorted
EDRcat_stk.sort(['SURVEY','HPXPIXEL'])


print("Total number of DESI EDR spectra (SV1 & SV3) to be used: ",len(EDR_qsolist))

# Creating the list containing the number of files on database grouped by HEALPIX 

web_list = np.unique(EDR_qsolist) # List of web links to be tested (sorted) 
#web_list.sort()

nf_coadd = [] # nf_coadd = Name of files on folder related to the coadded names
survey = [] # survey = Number of the survey to refolder the data

for b in range(len(web_list)):
    if (len(str(web_list[b])) == 105):
        nf_coadd.append(str(web_list[b][81:105]))
        survey.append(str(web_list[b][87:90])+'/dark/')
    if (len(str(web_list[b])) == 108):
        nf_coadd.append(str(web_list[b][83:108]))
        survey.append(str(web_list[b][89:92])+'/dark/')
        
survey = np.array(survey)        

print("List of files to be downloaded and/or modified: ",len(web_list))

print("\n")
print("---------------------------------------------")
print("\n")



# Checking if the files exist on the directory

df_list = os.listdir(local_dir) # df_list = Downloaded files (Excluding catalogs)
df_list.sort()
df_list = np.array(df_list)
file_list = len(df_list)

fi_f = np.char.find(df_list, "coadd", start=0, end=None) ## fi_f = File (coadded) identification on folder

y = 0 # part of the list
n = 0 # not part of the list

for i in range(file_list):
    if ( fi_f[i] == (-1) ):
        n = n + 1
    elif(fi_f[i]==(0)):
        y = y + 1
print("---------------------------------------------")
print("\n")
print(f"Coadded files on folder: {y}/{len(web_list)}")
print(f"To be downloaded: {len(web_list)-(y)}/{len(web_list)}")
print("\n")
print("---------------------------------------------")
print("\n")

coadd_list = np.delete(df_list,np.char.find(df_list, "coadd", start=0, end=None) == (-1))


ls = []
for x in range(len(nf_coadd)):
    ls.append(len(nf_coadd[x]))
ls = np.array(ls)


hpix_code = []

for i in range(len(coadd_list)):
    if (ls[i] == 25):
        hpix_code.append(coadd_list[i][15:20])
    if (ls[i] == 24):
        hpix_code.append(coadd_list[i][15:19])
        
path = str(local_dir)    
hpix_code = np.array(hpix_code)


for F in range(len(coadd_list)):
    PATH = path + str(survey[F])+ str(int(int(hpix_code[F])/100)) + '/'
    print(f'Main Folder to this file ({nf_coadd[F]}) : {PATH}')
    if (os.path.exists(PATH) == True):
        new_path = PATH + hpix_code[F]
        if (os.path.exists(new_path) == True):
            print(f'Subfolder to locate the file: {new_path}')
            os.rename(path+nf_coadd[F],new_path+'/'+nf_coadd[F])
        else: 
            print(f'Subfolder to locate the file: {new_path}')
            os.mkdir(new_path)
            os.rename(path+nf_coadd[F],new_path+'/'+nf_coadd[F])
    else:
        os.makedirs(PATH)
        new_path = PATH + hpix_code[F]
        if (os.path.exists(new_path) == True):
            print(f'Subfolder to locate the file: {new_path}')
            os.rename(path+nf_coadd[F],new_path+'/'+nf_coadd[F])
        else: 
            print(f'Subfolder to locate the file: {new_path}')
            os.mkdir(new_path)
            os.rename(path+nf_coadd[F],new_path+'/'+nf_coadd[F])
        
    print('\n')


print('Files refolding... DONE!!')
print('\n')

df_list = os.listdir(local_dir) # df_list = Downloaded files (Excluding catalogs)
df_list.sort()
df_list = np.array(df_list)
file_list = len(df_list)

F_R = np.delete(df_list,np.char.find(df_list, "report", start=0, end=None) == (-1)) ## F_R = File Reports

for B in range(len(F_R)):
    REPORTS = path + "REPORTS"
    if (os.path.exists(REPORTS) == True):
        os.rename(path+F_R[B],REPORTS+'/'+F_R[B])
    else:
        os.mkdir(REPORTS)
        os.rename(path+F_R[B],REPORTS+'/'+F_R[B])

print('Reports refolding... DONE!!')
print('\n')
