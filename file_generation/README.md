# File Generation

The followng can be moved into a Github Action:

First, download (refresh) the BLS data and the Census data in the Data_[Year] folders. The Census data is already in the repo since it will not change often. Also make sure that your folders are already set up the expected way. In the future, it would probably be easier to have the folders made automatically. Make sure to have ‘FIPS_state.csv’ since it helps automate the file naming. (We could automatically run this refresh quarterly.)

To get the state-level files for the US, run ‘concat_states_US.py’ (it will do all NAICS lengths at once) and then run ‘add_population_US.py’ for each NAICS length (parameter inside code).

To get the county-level files for the states, first run ‘concat_counties_US.py’ for each NAICS length (done individually since length 6 is quite slow) and then run ‘add_population_US.py’ for each NAICS length. Now you will have the county-level data for all the US. Run ‘split_US_data.py’ to have the data split into separate files and organized by state. This will be slow for the NAICS codes of length 6. John is working on optimization tricks to improve the running time.
