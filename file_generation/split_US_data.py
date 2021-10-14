# split_US_data.py v1.1
# Splits county level concatenated US file into separate state files
# John Andrew Taylor, September 2021

import pandas as pd
import random

# Set to NAICS length desired
NAICS_length = 2

# Set to year desired. Must be string.
year = "2021"

# Set to quarter desired. Must be string.
quarter = "Q1"

df = pd.read_csv("country/US-"+year+"-"+quarter+"-naics-"+str(NAICS_length)+"-digits.csv", dtype = str)

states = pd.read_csv("FIPS_state.csv", dtype = str)
fips_list = states['FIPS'].tolist()
usps_list = states['USPS'].tolist()

for fips, usps in zip(fips_list, usps_list):
    # print(usps)
    state_df = df[df['FIPS'].str.startswith(fips)]
    state_df.to_csv("states/"+usps+"/US-"+usps+"-"+year+"-"+quarter+"-naics-"+str(NAICS_length)+"-digits.csv", index = False)
