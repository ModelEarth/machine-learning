# impute_data v1.1
# Creates CSV files with the missing data replaced.
# John Andrew Taylor, June 2021

import numpy as np
import pandas as pd
from sklearn.neural_network import MLPRegressor
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split

# To remove convergence warnings
import warnings
from sklearn.exceptions import ConvergenceWarning

warnings.filterwarnings(action='ignore', category=ConvergenceWarning)

# Years to draw data from (local storage).
years = ["2020", "2019"]
# FIPS number of the state being targeted.
state = "13"
# Desired length of the NAICS codes.
NAICS_length = 6
# Columns to predict
pred_cols = ["annual_avg_emplvl", "total_annual_wages"]

# A list of the 2-digit state FIPS codes is given to import extracted BLS data.
# (see extract_BLS_QCEW_v2.py)
df = pd.read_csv("FIPS_state.csv", dtype = str)
fips_list = df['FIPS'].tolist()

# List of missing NAICS data need to be precomputed
df = pd.read_csv("missing_"+state+"000.csv", dtype = str)
naics_list = df['industry_code'].tolist()

imp_data = pd.read_csv("Data_2020/"+state+"000.csv", usecols = ["area_fips", "industry_code", "annual_avg_estabs", "annual_avg_emplvl", "total_annual_wages"])
imp_data = imp_data.loc[imp_data["industry_code"].str.len() == NAICS_length]
imp_data.insert(loc = 5, column = "Score", value = 0)

#naics_list = ["541611"]

for NAICS in naics_list:
	for pred_col in pred_cols:
		# Build X and y sets
		X = []
		y = []

		# Iterates through each Data_XXXX folder
		for year in years:
			# Iterates through each FIPS XXXXX.csv file
			for fips in fips_list:
				df = pd.read_csv("Data_"+year+"/"+fips+"000.csv", usecols = ["industry_code", "annual_avg_estabs", "annual_avg_emplvl", "total_annual_wages"])
				# Try-except block needed in case NAICS code is not present in a CSV file
				try:
					df = df.loc[df["industry_code"] == NAICS]
					if df.iloc[0][pred_col] != 0 or df.iloc[0]["annual_avg_estabs"] == 0:
						X.append([df.iloc[0]["annual_avg_estabs"]])
						y.append(df.iloc[0][pred_col])
				except IndexError:
					continue

		if len(X) < 20:
			print("Skipped "+NAICS+" due to lacking data.")

		max_score = 0.0
		best_random_state = -1
		best_regr = None

		# Testing 100 random models. The random states are being set to provide persistence
		for i in range(0, 100):
			X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=i, test_size = 0.10)

			regr = MLPRegressor(solver = 'lbfgs', random_state=i, max_iter=10000).fit(X_train, y_train)
			predictions = regr.predict(X_test)
			score = regr.score(X_test, y_test)
			if score > max_score:
				max_score = score
				best_random_state = i
				best_regr = regr
			if score > 0.9:
				break

		df = imp_data.loc[imp_data["industry_code"] == NAICS]
		prediction = regr.predict([[df.iloc[0]["annual_avg_estabs"]]])
		imp_data.at[imp_data.index[imp_data["industry_code"] == NAICS][0], pred_col] = int(prediction[0])
		imp_data.at[imp_data.index[imp_data["industry_code"] == NAICS][0], "Score"] += int(max_score*100)
	print("Completed: "+NAICS)

imp_data = imp_data.rename(columns = {'area_fips':'Fips', 'industry_code':'Naics', 'annual_avg_estabs':'Firms', 'annual_avg_emplvl':'Employees', 'total_annual_wages':'Wages'})
imp_data.to_csv(path_or_buf = 'Data_2020_imp/'+state+'000i.csv', index = False)
print("Done!")
