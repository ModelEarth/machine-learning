# add_population_US.py v1.1
# Adds Census population estimates to concatenated files (any level)
# John Andrew Taylor, September 2021

import pandas as pd

# Set to year desired. Must be string.
year = "2021"

# Set to quarter desired. Must be string.
quarter = "Q1"

# Note: can be changed to do all length NAICS, but will be slow for county level data

# Do not change encoding type! Unexpected errors can occur
pop = pd.read_csv("co-est2020.csv", encoding = "ISO-8859-1", dtype = str)

for i in range(2,7): # Generate for 2 to 6

    df = pd.read_csv('country/US-counties-naics'+str(i)+'-'+year+'-'+quarter+'.csv', dtype = str)

    curr_fips = '00000'
    curr_pop = '0'

    for index, row in df.iterrows():

        if row["area_fips"] != curr_fips:
            curr_fips = row["area_fips"]
            try:
                curr_pop = pop.loc[(pop["STATE"] == row["area_fips"][0:2]) & (pop["COUNTY"] == row["FIPS"][2:])]["POPESTIMATE2020"].item()
            except:
                curr_pop = '0'
        df.at[index, "Population"] = curr_pop

    df.to_csv('country/US-counties-naics'+str(i)+'-'+year+'-'+quarter+'.csv', index = False)