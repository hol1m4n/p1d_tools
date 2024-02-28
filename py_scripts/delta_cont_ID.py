import os
import numpy as np
import fitsio
from astropy.io import fits as fits
from astropy.table import Table, vstack, join
from astropy.convolution import convolve, Gaussian1DKernel
import matplotlib
import matplotlib.pyplot as plt
import sys
import glob
import  scipy.optimize    as op
import urllib.request
from astropy.table import Table



delta_folder = '/work1/holman7/DESI/D1/Delta/'

lista = os.listdir(delta_folder)

print(lista)


ID = str(39633282643528010)

file = 'File: '

for a in range(len(lista)):

    S = fits.open(delta_folder+lista[a])
    print(delta_folder+lista[a])

    for b in range(len(S)):

        HDUs = str(S[b].name)

        if (HDUs == ID):
            file = file + str(delta_folder+lista[a])
            #break
print(file)













