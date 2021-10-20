# extract_BLS_QCEW v2.0
# Extracts BLS QCEW data using direct URL
# John Andrew Taylor, June 2021

import pandas as pd
import urllib.request
import os

# A predetermined list of FIPS codes to extract needs to be provided.
# In this case, a list of the 2-digit state FIPS codes is given.
df = pd.read_csv("FIPS_state.csv", dtype = str)
fips_list = df['FIPS'].tolist()

# Year that data will be requested.
# This code uses annual averages, but quarterly data can also be extracted.
#year = "2020"
year = "2021" # Not yet available on Oct 20, 2021

#currentRoot = 'C:/Users/Beetle/Dropbox (Personal)/Internship'
currentRoot = '/Users/helix/Library/Data/machine-learning'
yearFolder = 'Data_'+year
folderPath = currentRoot + '/' + yearFolder

if not os.path.isdir(folderPath):
       os.makedirs(folderPath)

# directories would need to be an array
#directories = currentRoot + '/' + yearFolder
# Add folder(s)
#for i in directories:
#   if not os.path.isdir(i):
#       os.makedirs(i)

for fips in fips_list:
    # This is the direct URL to access the BLS employment data.
    url = 'https://data.bls.gov/cew/data/api/'+year+'/a/area/'+fips+'000.csv'
    # File from the URL will be saved in the preexisting local folder.
    print("url: " + url)
    print("save at: " + currentRoot + '/' + yearFolder + '/' + fips+'000.csv')
    urllib.request.urlretrieve(url, currentRoot + '/' + yearFolder + '/' + fips+'000.csv')
    # urllib.request.urlretrieve(url, 'Data_'+year+'/'+fips+'000.csv')
    print("Completed "+fips)

print("DONE")
