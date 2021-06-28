# extract_BLS_QCEW v2.0
# Extracts BLS QCEW data using direct URL
# John Andrew Taylor, June 2021

import pandas as pd
import urllib.request

# A predetermined list of FIPS codes to extract needs to be provided.
# In this case, a list of the 2-digit state FIPS codes is given.
df = pd.read_csv("FIPS_state.csv", dtype = str)
fips_list = df['FIPS'].tolist()

# Year that data will be requested.
# This code uses annual averages, but quarterly data can also be extracted
year = "2020"

for fips in fips_list:
    # This is the direct URL to access the BLS employment data
    url = 'https://data.bls.gov/cew/data/api/'+year+'/a/area/'+fips+'000.csv'
    # File from the URL will be saved in the preexisting local folder
    urllib.request.urlretrieve(url, 'C:/Users/Beetle/Dropbox (Personal)/Internship/Data_'+year+'/'+fips+'000.csv')
    print("Completed "+fips)

print("DONE")