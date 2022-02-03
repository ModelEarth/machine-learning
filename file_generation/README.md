# File Generation

The followng can be moved into a Github Action:

First, [download (refresh) BLS data](https://www.bls.gov/cew/downloadable-data-files.htm) and the Census data in the Data_[Year] folders. The <!-- BLS -->files are large, so we exclude them from the repo.


On the BLS page:
https://www.bls.gov/cew/downloadable-data-files.htm

Download the By Area > Quarterly > 2021 file.
https://data.bls.gov/cew/data/files/2021/csv/2021_qtrly_by_area.zip

Unzip the folder here:  
2021.q1-q2.by_area  

Changed q1-q1 to q1-q2 in three place.  
Note that the q1-q2 will become q1-q3 within the next few months.  

In add_population_US.py, renamed row["FIPS"] to row["area_fips"] in three places.  


The Census data is already in the repo since it will not change often. Also make sure that your folders are already set up the expected way. In the future, it would probably be easier to have the folders made automatically. Make sure to have ‘FIPS_state.csv’ since it helps automate the file naming. (We could automatically run this refresh quarterly.)


Initiate a virtual environment folder called env (optional)

	python3 -m venv env
	source env/bin/activate

Get wheel and panda. (This may be required each time if your computer enforces virtual environments)  

	pip install wheel
	pip install pandas

To get the state-level files for the US. (This will fetch all NAICS lengths at once)

Don't need to run this yet, 2021 is not yet available.
	python3 extract_BLS_QCEW.py

	cd file_generation
	python3 concat_states_US.py

Then run ‘add_population_US.py’ for each NAICS length (set parameter inside code)

	python3 add_population_US.py

To get the county-level files for the states, first run ‘concat_counties_US.py’ for each NAICS length (done individually since length 6 is quite slow).

TO DO: Add a loop from 2 to 6. Clear file_generation/country before testing.

	python3 concat_states_US.py

Then run ‘add_population_US.py’ for each NAICS length (change length manually from 2 to 6 in file)

add_population_US.py


Now you will have the county-level data for all the US. Run ‘split_US_data.py’ to have the data split into separate files and organized by state. This will be slow for the NAICS codes of length 6.<!--John is working on optimization tricks to improve the running time.-->  

