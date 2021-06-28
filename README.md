# Imputation Using Machine Learning

## Summary

The goal of this project is to create machine learning regression models which will replace missing employment data of the Bureau of Labor Statistics Quarterly Census of Employment & Wages.

## Data Extraction

Currently, data is extracted using Python's urllib library (see extract_BLS_QCEW.py). This script accesses the BLS data directly through the permanent URL.

- TODO: Make extract_BLS_QCEW.py script more customizable and allow for user input prompts.
- TODO: Write up an alternative method of data extraction using the EPA's flowsa library.

## Model Training

The project is using Python's scikit-learn library. The models being used are [Multi-layer Perceptron Regressors](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPRegressor.html) (neural networks). The most effective solver was the ‘lbfgs’ solver, an optimizer in the family of quasi-Newton methods, due to the small size of the dataset. The maximum iterations are set to 10,000 (this value is more than sufficient). The hidden layers and the activation functions have been left at their default values (100 and 'relu'), though no alternatives have been tested yet.

A separate model is created for each NAICS code. The training and testing sets are built up by randomly dividing the data with a random 90% and 10% split respectively. Note that the size of the dataset will vary since the availability of data on a given NAICS code for each area is not consistent.

Model persistence during development is guaranteed by setting the random state numbers of both the data splitting process and the model training process.

## Model Testing

Using the remaining 10% of the complete data, we evaluate each model using the [R^2](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.r2_score.html) score. Currently, 100 random models are created for each NAICS code to prevent misleading outliers (that either underperform or overperform) and determine whether an imputation process is viable with the provided data for the given NAICS code. It is recommended to continue to improve the models until a median R^2 score of 0.5 is reached.

## Results



## Future Work

These are some goals that would improve the current state of the project:

- Make all scripts very modular and allow user input to tweak them.
- Test out different types of regression models, such as Kernel Ridge Regression and Random Forest Regression.
- Introduce more input data, such as the population of an area, to improve the accuracy of the outputs.
- Consider including more years of data for the model training.
- Research multi-output regressors and determine their utility in this project.
