# concat_counties_US.py v1.1
# Concatenates BLS data at a county level
# John Andrew Taylor, September 2021

import pandas as pd
import glob

# Set to NAICS length desired
NAICS_length = 2
# Note: can be changed to do all length NAICS, but will be slow

# Set to year desired. Must be string.
year = "2021"

# Set to quarter desired. Must be string.
quarter = "Q1"

# Set source files appropriately. TODO: Automate.
files = glob.glob("2021.q1-q1.by_area/2021.q1-q1 *.csv")

print(len(files))

df = pd.DataFrame()
for f in files:
    csv = pd.read_csv(f, dtype = str, usecols = ['area_fips', 'industry_code', 'qtrly_estabs_count', 'month3_emplvl', 'total_qtrly_wages'])
    csv = csv[csv["industry_code"].str.len() == NAICS_length]
    df = df.append(csv)

df.to_csv('country/US-'+year+'-'+quarter+'-naics-'+str(NAICS_length)+'-digits.csv', index = False)