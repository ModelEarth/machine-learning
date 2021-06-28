# model_test_single v1.2
# Trains random MLP models for a single NAICS code and outputs statistics.
# John Andrew Taylor, June 2021

import numpy as np
import pandas as pd
from sklearn.neural_network import MLPRegressor
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
import statistics

# NAICS code for which model is being made
NAICS = "562211"
# Years to draw data from (local storage)
years = ["2020", "2019"]

# A list of the 2-digit state FIPS codes is given to import extracted BLS data.
# (see extract_BLS_QCEW_v2.py)
df = pd.read_csv("FIPS_state.csv", dtype = str)
fips_list = df['FIPS'].tolist()

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
			if df.iloc[0]["annual_avg_emplvl"] != 0 or df.iloc[0]["annual_avg_estabs"] == 0:
				X.append([df.iloc[0]["annual_avg_estabs"]])
				y.append(df.iloc[0]["annual_avg_emplvl"])
		except IndexError:
			print("Missing NAICS code "+NAICS+" in "+year+" data of "+fips+"000.csv")

print("Dataset size: " + str(len(X)))

score_list = []

# Testing 100 random models. The random states are being set to provide persistence
for i in range(0, 100):
	X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=i, test_size = 0.10)

	regr = MLPRegressor(solver = 'lbfgs', random_state=i, max_iter=10000).fit(X_train, y_train)
	predictions = regr.predict(X_test)
	#print(regr.score(X_test, y_test))
	score_list.append(regr.score(X_test, y_test))

print("Median: "+ str(statistics.median(score_list)))
print("Average: "+ str(statistics.mean(score_list)))
print("Max: "+ str(max(score_list)))
