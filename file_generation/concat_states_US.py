# concat_states_US.py v2.0
# Concatenates BLS data at a state level
# John Andrew Taylor, October 2021

import pandas as pd
import glob

# Do not change, will generate NAICS lengths 2, 4, and 6
NAICS_length = 0

# Set to year desired. Must be string.
year = "2021"

# Set to quarter desired. Must be string.
quarter = "Q1"

# Set source files appropriately. TODO: Automate.
files = glob.glob("2021.q1-q1.by_area/*Statewide.csv")

print("Number of state files found: "+ str(len(files)))

for i in range(1,4):
	NAICS_length = 2*i
	df = pd.DataFrame()
	for f in files:
	    csv = pd.read_csv(f, dtype = str, usecols = ['area_fips', 'industry_code', 'qtrly_estabs_count', 'month3_emplvl', 'total_qtrly_wages'])
	    csv = csv[csv["industry_code"].str.len() == NAICS_length]
	    df = df.append(csv)

	df = df.rename(columns={"area_fips": "FIPS", "industry_code": "NAICS", "qtrly_estabs_count": "Establishments", "month3_emplvl": "Employees", "total_qtrly_wages": "Payroll"})

	df.to_csv('country/US-'+year+'-'+quarter+'-naics-'+str(NAICS_length)+'-digits.csv', index = False)