# concat_counties_US.py v1.1
# Concatenates BLS data at a county level
# John Andrew Taylor, September 2021

import pandas as pd
import glob

# Set to NAICS length desired - Manually change from 2 to 6
# NAICS_length = 4
# Note: can be changed to do all length NAICS, but will be slow

# Set to year desired. Must be string.
year = "2021"

# Set to quarter desired. Must be string.
quarter = "Q1"

# Set source files appropriately. TODO: Automate.
files = glob.glob("2021.q1-q2.by_area/2021.q1-q2 *.csv")

print(len(files))

for i in range(2,7): # Generate for 2 to 6
    df = pd.DataFrame()
    for f in files:
        csv = pd.read_csv(f, dtype = str, usecols = ['area_fips', 'industry_code', 'qtrly_estabs_count', 'month3_emplvl', 'total_qtrly_wages'])
        csv = csv[csv["industry_code"].str.len() == i]
        df = df.append(csv)

    df = df.rename(columns={"area_fips": "FIPS", "industry_code": "NAICS", "qtrly_estabs_count": "Establishments", "month3_emplvl": "Employees", "total_qtrly_wages": "Payroll"})

    df.to_csv('country/US-counties-naics'+str(i)+'-'+year+'-'+quarter+'.csv', index = False)