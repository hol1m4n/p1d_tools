# Importing libraries 
import os
import numpy as np
import urllib.request
from astropy.io import fits
from astropy.table import Table
from astropy.table import vstack
import urllib.request
import requests

# Some useful functions to be used ahead

def check_link(path): # Function that takes care of seeing if the file exists on the web or not
    r = requests.head(path)
    status = r.status_code == requests.codes.ok
    if (status == True):
        return True
    else:
        return False
    


#Getting the individual coadded files names

local_dir = "/work1/holman7/spc_DESIedr/" #path to the catalogs
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

for b in range(len(web_list)):
    if (len(str(web_list[b])) == 105):
        nf_coadd.append(str(web_list[b][81:105]))
    if (len(str(web_list[b])) == 108):
        nf_coadd.append(str(web_list[b][83:108]))
    
print("List of files to be downloaded and/or modified: ",len(web_list))

print("\n")
print("---------------------------------------------")
print("\n")


# Checking if the files exist on tthe web

print("Checking files on the web... may take a while")

#chw_list = [] # chw_list = Check web list

#for i in range(len(web_list)):
   # chw_list.append(check_link(web_list[i]))
    
#chw_list = np.array(chw_list)

print("---------------------------------------------")
print("\n")

#print("Number of links working on database: ",np.count_nonzero(chw_list == True))
#print("Links not found: ",np.count_nonzero(chw_list == False))

print("\n")
print("---------------------------------------------")
print("\n")


# Checking if the files exist on the directory

df_list = os.listdir(local_dir) # df_list = Downloaded files (Excluding catalogs)
df_list.sort()
df_list = np.array(df_list)

fi_f = np.char.find(df_list, "coadd", start=0, end=None) ## fi_f = File (coadded) identification on folder

y = 0 # part of the list
n = 0 # not part of the list

for i in range(len(df_list)):
    if (fi_f[i]==(-1)):
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
print("---------------------------------------------")
print("\n")

print(f"DOWNLOADING AND MODIFYING COADD FILES")

print("\n")
print("---------------------------------------------")
print("\n")


for f in range(len(web_list)):
    f_tbm = os.path.join(local_dir,nf_coadd[f]) # f_tbm = Path to the file to be modified
    
    f_r = nf_coadd[f].replace('.fits', '.txt')# Changing .fits for .txt
    f_r = f_r.replace('coadd', 'report_codd')# Changing coadd for report
    f_r = os.path.join(local_dir,f_r) # f_r = File report in txt generated after the download, this in order to avoid downloading issues
    
    # To make the download it is necessary that the file fits or the download report is not present
    
    if not (os.path.exists(f_tbm) and os.path.exists(f_r)):
        print(f"({f+1}/{len(web_list)}) Downloading {nf_coadd[f]} ...")
        download = urllib.request.urlretrieve(web_list[f], f_tbm) # Downloading files
        
        if (len(str(nf_coadd[f])) == 25): # Extracting HPXPIXEL and SURVEY value on list
            sv = nf_coadd[f][6:9]
            hpix = nf_coadd[f][15:20]
        elif(len(str(nf_coadd[f])) == 24):
            hpix = nf_coadd[f][15:19]
            sv = nf_coadd[f][6:9]
            
        hpx_query = (EDRcat_stk['HPXPIXEL'] == int(hpix)) & (EDRcat_stk['SURVEY'] == str(sv)) # hpx_query = HEALPIX and SV Query on stacked catalog
        tmp_cat = EDRcat_stk[hpx_query] # Temporary catalog restricted to a specific value of HEALPIX
        
        jdf = Table.read(f_tbm) # jdf = (Just Downloaded file ) Open file just downloaded to match with stacked catalog

        selected = [] # Targets selected to be extracted
        for x in range(len(tmp_cat)):
            selected.append(tmp_cat["TARGETID"][x])

        chosen_ini = np.array(selected)
        chosen_bool = np.isin(jdf["TARGETID"],chosen_ini)
        chosen_ibool = np.invert(chosen_bool)

        idx = np.where(chosen_ibool)
        print(f"Targets on cat: {len(chosen_ini)} , Total in coadded: {len(chosen_bool)} , Rejected: {len(idx[0])}")
        
        # Modifying the file to get the selected spectra
        
        with fits.open(f_tbm , mode='update') as hdul:
            
            HDUnames = ['PRIMARY','FIBERMAP','EXP_FIBERMAP', \
                       "B_WAVELENGTH","B_FLUX","B_IVAR","B_MASK","B_RESOLUTION", \
                       "R_WAVELENGTH","R_FLUX","R_IVAR","R_MASK","R_RESOLUTION", \
                       "Z_WAVELENGTH","Z_FLUX","Z_IVAR","Z_MASK","Z_RESOLUTION", \
                       "SCORES"]
            #First: BinaryTable (catalog)
            T1 = Table.read(hdul[1])
            T1.remove_rows(idx)
            hdu_f = fits.BinTableHDU(T1, name = HDUnames[1]) #First hdu
            hdul[1] = hdu_f

            #Image HDU arrays (spectra) 12 (4-7,9-12,14-17)

            for i in range(15):
                c = i+3 #counter
                if ((c != 3) and (c != 8) and (c != 13)):
                            hdu_temp = hdul[c].data
                            hdu_temp = np.delete(hdu_temp,np.invert(chosen_bool),0)
                            hdu_ff = fits.ImageHDU(hdu_temp,name = HDUnames[c]) #hdu for file
                            hdul[c] = hdu_ff

            #Last: BinaryTable (scores)
            T2 = Table.read(hdul[18])
            T2.remove_rows(idx)
            hdu_l = fits.BinTableHDU(T2, name = HDUnames[18]) #Last hdu
            hdul[18] = hdu_l

            hdul.flush()
            hdul.close()
        
        # Making the report as .txt
        with open(f_r, 'w') as report:
            report.write(f"File: {nf_coadd[f]} \n")
            report.write(f"Targets on cat: {len(chosen_ini)} , Total in coadded: {len(chosen_bool)} , Rejected: {len(idx[0])} \n")
            report.write("\n")
            report.write("---------------------------------------------")
            report.write("\n")

            for z in range(len(selected)):
                report.write(f" {selected[z]} \n")

            report.write("\n")
            report.write("---------------------------------------------")
            report.write("\n")   
            report.write("FILE on folder and modified!! \n")
            report.close()
        
        
        print ("FILE on folder and modified!! \n")
    else:
        print(f"({f+1}/{len(web_list)}) {nf_coadd[f]} ON DISK!! \n")
            

print("\n")
print("---------------------------------------------")
print("\n")

print(f"All Done!!!")

print("\n")
print("---------------------------------------------")
print("\n")
        









