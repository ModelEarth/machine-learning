# concat_states_US.py v2.0
# Concatenates BLS data at a state level in "country" folder
# John Andrew Taylor, October 2021

import pandas as pd
import glob
import os

# Set to year desired. Must be string.
year = "2021"

# Set to quarter desired. Must be string.
quarter = "Q1"

# Set source files appropriately. TODO: Automate.
files = glob.glob("2021.q1-q2.by_area/*Statewide.csv")

print("Number of state files found: "+ str(len(files)))

folderPath = 'country'
if not os.path.isdir(folderPath):
       os.makedirs(folderPath)

for i in range(2,7): # Generate for 2 to 6
	#NAICS_length = 2*i
	df = pd.DataFrame()
	for f in files:
	    csv = pd.read_csv(f, dtype = str, usecols = ['area_fips', 'industry_code', 'qtrly_estabs_count', 'month3_emplvl', 'total_qtrly_wages'])
	    csv = csv[csv["industry_code"].str.len() == i]
	    df = df.append(csv)

	df = df.rename(columns={"area_fips": "FIPS", "industry_code": "NAICS", "qtrly_estabs_count": "Establishments", "month3_emplvl": "Employees", "total_qtrly_wages": "Payroll"})

	df.to_csv('country/US-states-naics'+str(i)+'-'+year+'-'+quarter+'.csv', index = False)