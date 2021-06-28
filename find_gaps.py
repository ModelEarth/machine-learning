# find_gaps v1.0
# Finds the missing data of a given CSV and generates a CSV with those rows.
# John Andrew Taylor, June 2021

import pandas as pd

# Length of the target NAICS code.
NAICS_length = 6

# The file name and location should be set appropriately.
df = pd.read_csv("Data_2020/13000.csv", dtype = str)
disc = df["industry_code"].loc[(df["disclosure_code"] == "N") & (df["industry_code"].str.len() == NAICS_length)]
print(disc)

# The output name must correspond to the one used in the model training script.
disc.to_csv('missing_13000.csv')