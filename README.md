# NAICS Imputation Using Machine Learning

As of 2017, the US Census inserts estimates (perturbs cells) for small employment counts. Therefore, fpeckert does not impute data from 2017 forward since there are no missing cells in the data.

Related documentation: [https://model.earth/data-pipeline/research](https://model.earth/data-pipeline/research)

## Summary

The goal of this project is to create machine learning regression models which will estimate (impute) missing employment data within the Bureau of Labor Statistics Quarterly Census of Employment & Wages.

[Steps for generating files without gaps](file_generation)  
[Our pipeline for static NAICS file output](https://model.earth/community-data/process/python/bea/)  

For comparison: [Imputing Missing Values in the US Census Bureau's County Business Patterns](http://www.fpeckert.me/cbp/)

## Data Extraction

Currently, data is extracted using Python's urllib library (see extract_BLS_QCEW.py). This script accesses the BLS data directly through the permanent URL.

- TODO: Make extract_BLS_QCEW.py script more customizable and allow for user input prompts.
- TODO: Figure out if we should pull from our [pre-processed FIPS and ZTCA annual files](http://model.earth/community-data/process/python/bea). -- [View annual output](https://github.com/ModelEarth/community-data/tree/master/industries/naics/US/counties)
- TODO: Document how we could use ML processes with the [EPA's Flowsa library](https://github.com/USEPA/flowsa).

### Bureau of Labor Statistics - QCEW Open Data Access: Sample Code

The BLS has provided sample code in multiple languages to show how QCEW data can be extracted from their database. More information [here](https://data.bls.gov/cew/doc/access/data_access_examples.htm).

## Model Training

The project is using Python's scikit-learn library. The models being used are [Multi-layer Perceptron Regressors](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPRegressor.html) (neural networks). The most effective solver was the ‘lbfgs’ solver, an optimizer in the family of quasi-Newton methods, due to the small size of the dataset. The maximum iterations are set to 10,000 (this value is more than sufficient). The hidden layers and the activation functions have been left at their default values (100 and 'relu'), though no alternatives have been tested yet.

A separate model is created for each NAICS code. The training and testing sets are built up by randomly dividing the data with a random 90% and 10% split respectively. Note that the size of the dataset will vary since the availability of data on a given NAICS code for each area is not consistent.

Model persistence during development is guaranteed by setting the random state numbers of both the data splitting process and the model training process.

Note: Currently, the model_test_single.py script will only create models for predicting employment level or wages, not both at the same time. The models only use existing data as the X and y sets, but more information, such as population size and average wage of the FIPS code might be added.

## Model Testing

Using the remaining 10% of the complete data, we evaluate each model using the [R^2](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.r2_score.html) score. Currently, 100 random models are created for each NAICS code to prevent misleading outliers (that either underperform or overperform) and determine whether an imputation process is viable with the provided data for the given NAICS code. It is recommended to continue to improve the models until a median R^2 score of 0.5 is reached.

## Results

Initial tests proved that imputation using machine learning regression was viable. Four NAICS codes were randomly selected to assess the median R^2 score of 100 random models predicting employment levels.

- Results for 541611: Dataset size of 34. Median r^2 score of 0.6126 and a maximum of 0.9992. Promising initial results.
- Results for 811310: Dataset size of 38. Median r^2 score of 0.8927 and a maximum of 0.9882. Very promising initial results.
- Results for 452319: Dataset size of 27. Median r^2 score of 0.9129 and a maximum of 0.9911. Very promising initial results.
- Results for 562211: Dataset size of 30. Median r^2 score of -0.0359 and a maximum of 0.9895. Mixed initial results, could indicate presence of outlier models and a general lack of relationship.

Adding more years of data seems to improve the performance of the models. For example, using only the 2020 annual average data, the median R^2 score of the models predicting the employemnt level of NAICS code 562211 was -0.0359, indicating that the median model would be constant and therefore useless. When the 2019 data was included, increasing the dataset size to 61, the median R^2 score increased to 0.4855, indicating a moderate correlation between the input and outputs.

## Future Work

These are some goals that would improve the current state of the project:

- Make all scripts modular and parameters to allow user input to tweak them.
- Test different types of regression models, such as Kernel Ridge Regression and Random Forest Regression.
- Introduce more input data, such as the population of an area, to improve the accuracy of the outputs.
- Consider including more years of data for the model training.
- Research multi-output regressors and determine their utility in this project.
- Compare the results of independent regression models for wages with models using the predicted employee numbers as inputs.

Looks interesting: [Flyte.org - Workflow Automation for Machine Learning](https://flyte.org/) used by Skype and Spotify

---


# Using Machine Learning to Estimate Census Business Patterns

**Data sources**  
Bureau of Labor Statistics (BLS) Quarterly Census of Employment & Wages - [Output](/localsite/info/#state=GA), [Dev](/localsite/info/naics)  
Census Business Patterns (CBP)  
[Zip Codes Business Patterns (ZBP)](https://www.census.gov/data/developers/data-sets/cbp-nonemp-zbp/zbp-api.html)

<!--#### By Loren K. Heyns, John A. Taylor, Benjamin Liu-->

## Using Machine Learning to Fill Gaps

When a county's 6-digit industry naics is missing employee and payroll data, its parent categories (5, 4, 3 or 2-digit naics) will also omit the data. This occurs when there are only a couple firms in a county to protect the privacy of individual firms. (Sometimes when there are over 15 establishments in a county, the employment data is also null.)

A very rough estimate for local industry employee counts and payroll can be generated by averaging values from other counties in the state, however in some states over 80 of 380+ industries do not include employment and payroll data.

We'll be comparing results from our [Machine Learning scripts](https://github.com/modelearth/machine-learning) to the [Eckert CBP data](https://github.com/modelearth/cbp_database_public) generated by linear objective functions.  

<!--
We're updating our NAICS Imputation Using ML to work with our new NAICS county and zip output.

https://github.com/modelearth/machine-learning

The imputation ML was prepared by GaTech PHD student John Taylor.
He's offered to assist with any questions that arise.

We'll compare the results with the 2021 Eckert study linked at the bottom here:
https://model.earth/data-pipeline/research

We will also use in Random Forest ML for forecasting, which we're documenting here:
https://model.earth/data-pipeline/timelines/prep/all/

Our NAICS county output (used by both the imputation and forecasting) is documented here:
https://model.earth/community-data/process/python/bea/
-->

## 2006 Early Efforts to Fill Gaps

Isserman, A.M.; Westervelt, J. [1.5 million missing numbers: Overcoming employment suppression in County Business Patterns data](https://journals.sagepub.com/doi/10.1177/0160017606290359). International Regional Science Review, 29(3), pp.311-335. **2006**<!-- Seems not to work, probably need do institutional login first. https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.1015.6155&rep=rep1&type=pdf -->

## 2017 NAICS Data without Gaps

As of 2017, the US Census inserts estimates (perturbs cells) for small employment counts. Therefore, [fpeckert](http://www.fpeckert.me/cbp/) does not impute data from 2017 forward since there are no missing cells in the data.

[Imputed County Business Patterns (CBP) dataset](http://www.fpeckert.me/cbp/) by [Fabian Eckert, et al.](http://fpeckert.me/cbp/efsy.pdf) - The Fabian Eckert (2021) work extends Isserman and Westervelt (2006), but uses a linear objective function for faster computation with exact results. The authors are planning to apply to zip codes. "After 1994, the CBP files contain tabulations at the zip code level. We plan to apply our imputation method to this geographic unit in a future draft." - GitHub Fork: [cbp\_database\_public](https://github.com/modelearth/cbp_database_public) and 2018 output: [efsy_panel_naics_2018.csv](https://github.com/modelearth/community-data/tree/master/process/naics/source) - number of employees but not firms. 

<!--
The content of our cbp repo resides in an "env" folder, so .gitignore excludes it.  
Also, output has not been successfully generated yet.
	[2018 data from Eckert](https://github.com/modelearth/community-data/tree/master/process/cbp) and our 
-->


Eckert, F.; Fort, T.C.; Schott, P.K.; Yang, N.J. [Imputing Missing Values in the US Census Bureau's County Business Patterns](https://www.nber.org/system/files/working_papers/w26632/w26632.pdf). National Bureau of Economic Research. **2021**


