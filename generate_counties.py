# generate_counties v1.0
# Uses an "All Geographic Areas, One Industry" BLS QCEW data file to generate a list of counties.
# John Andrew Taylor, July 2021

import pandas as pd
import numpy as np

# The file name and location should be set appropriately.
# Note that the datatype must be set to string. If FIPS codes are read as integers, the starting 0 in codes will be dropped.
df = pd.read_csv('10.csv', dtype = str)
counties = df['area_fips'].drop_duplicates()

# Removes all irregular county FIPS, such as territories or combined areas
counties = counties.loc[0 : counties.index[counties=='72000'][0] - 1]

# Note: This will include "Unknown or Undefined" county FIPS, ending in 999
counties.to_csv('FIPS_county.csv', index = False)