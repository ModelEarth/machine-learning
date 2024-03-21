# USEEIO matrix files

Developed by Honglin, 2024.

Uses USEEIO matrix files from:

/io/build/api
/OpenFootprint/impacts

[Network Graph Charts](/community/start/charts/) - [Sankey](/io/charts/sankey/) - [Chord](/io/charts/chord)

## Run Jupyter

Run in your webroot so you can access files in the io repo.
Creates a virtual environment and installs libraries.

	python3 -m venv env &&
	source env/bin/activate &&
	pip install pandas &&
	pip install tqdm &&
	pip install scikit-learn &&
	pip install matplotlib &&
	pip install numpy &&
	pip install notebook &&
	pip install --upgrade nbconvert &&
	jupyter-notebook
