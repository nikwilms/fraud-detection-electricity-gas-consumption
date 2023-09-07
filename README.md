
# Fraud Detection in Electricity and Gas Consumption Challenge
This project is a part of the [neuefische GmbH Data Science Bootcamp](https://www.neuefische.de/bootcamp/data-science).

#### -- Project Status: Completed

## Contributors
[Marius Bosch](https://www.linkedin.com/in/marius-bosch-435158126/), [Felix Geyer](https://www.linkedin.com/in/felix-geyer-a273bb12a/), [Daniel Marques Rodrigues](https://www.linkedin.com/in/daniel-marques-rodrigues-581b55127/), 
[Nikita Wilms](https://www.linkedin.com/in/nikita-wilms/)

## Project Objective
Using the client’s billing history, the aim of the challenge is to detect and recognize clients involved in fraudulent activities.

The solution will enhance the company’s revenues and reduce the losses caused by such fraudulent activities.

#### [Project Link](https://zindi.africa/competitions/fraud-detection-in-electricity-and-gas-consumption-challenge)
### Methods Used
* Feature engineering
* Data Visualization
* Exploratory Data Analysis
* Machine Learning

### Tech Stack
* Pandas, jupyter
* Python
* NumPy
* Matplotlib
* Seaborn
* scikit-learn (sklearn)
* Imbalanced-Learn (imblearn)
* Various Scikit-Learn Machine Learning Algorithms
* Various Preprocessing Tools
* Custom Preprocessing Functions

## Project Overview
The goal of this project is to develop a machine learning model to detect fraudulent electricity and gas consumption in Tunisia. The data provided by STEG includes client information and billing history from 2005 to 2019. The challenge is to identify the clients who are likely to be involved in fraudulent activities, such as tampering with their meters or using unauthorized connections.

## Data Sources
The data for this project is provided by STEG and can be downloaded from the Zindi platform. The data is composed of two files:
* `Client_train.csv`: This file contains information about the clients, such as their district, category, region, and creation date.
* `Invoice_train.csv`: This file contains information about the clients' billing history, such as the date of the invoice, the type of tax, the counter number, and the consumption levels.

## Questions and Hypotheses

* What are the factors that are most likely to be associated with fraudulent electricity and gas consumption?
* Can we develop a machine learning model that can accurately identify fraudulent clients?
* How can we improve the accuracy of our model?

## Blockers and Challenges
* The data is imbalanced, meaning that there are more non-fraudulent clients than fraudulent clients.
* Every client has multiple invoices
* Feature engineering, to give the model better information to predict


## Generated Project Contents

```
├── .venv                                      <- environment definition for ensuring consistent setup across environments
├── archive                                    <- notebooks for testing data
├── data                                       <- files for challenge
│   ├── test                                   <- test dataset
│   ├── train                                  <- train dataset
│   ├── data_ready_for_models_smart_agg.pkl    <- aggregated dataset, saved as pickle
│   ├── data_test.pkl                          <- for testing
│   └── SampleSubmission.csv                   <- sample for submission
│
├── images                                     <-how to setup a kanban board
├── models                                     <- models to train
│   ├── decision_tree                          <- decision tree model
│   │   ├── dectree_raw_smart.pkl              <- decision tree train and test prediction, saved as pickle file 
│   ├── xgboost                                <- xgboost model
│   │   ├── xgboost_grid_raw_smart_agg.pkl     <- xgboost train and test prediction on aggregated dataset, after grid search, saved as pickle file
│   │   ├── xgboost_grid_raw.pkl               <- xgboost train and test prediction on raw dataset, after grid search, saved as pickle file
│   │   ├── xgboost_grid_raw_smote.pkl         <- xgboost train and test prediction with SMOTE, after grid search, saved as pickle file
│   └── log_regression_DMR.pynb                <- decision tree model
│
├── notebooks                                  <- notebooks for feature engineering and modelling
│   ├── Feature_engineering_consumption        <- aggregate and sum up the consumption columns for each customer
│   ├── grid_search_xgboost_smart_agg          <- xgboost prediction and result with aggregated dataset
│   ├── grid_search_xgboost_smote              <- xgboost prediction and result with SMOTE
│   ├── grid_search_xgboost                    <- xgboost prediction and result
│   └── predict_competition                    <- prediction for challenge submission
│
├── extras                                     <- comparing MSE
│   ├── feature_engineering.py                 <- transform altitude, drop columns and check for missing values
│   ├── predict.py                             <- MSE for test
│   └── train.py                               <- MSE for train
│ 
├── src                                        <- code for use in this project
│   ├── evaluation                             <- evaluating the models output
│   │   └── evaluation_metrics.py              <- evaluation metrics
│   ├── basemodel                              <- model to beat prediction
│   │   └──basemodel.py                        <- prediction for basemodel
│   └── preprocessing                          <- preprocessing the data
│       ├── agg_invoice.py                     <- aggregate the invoice dataset with monthly weighting
│       └── cleaning.py                        <- rename columns and convert datatype
│ 
├── Fraud_detection_invoice_report_minimal     <- EDA report
├── Fraud_detection_ML_team_smart_agg          <- EDA and modeling
├── Fraud_detection_ML_team                    <- EDA and modeling
├── Fraud_Detection_Starter                    <- starter notebook for challenge
├── how_to_pickle                              <- pickle how-to
├── Makefile                                   <- install requirements
├── Presentation Slided Fraud Detection in Electricity and Gas Consumption Challenge
├── LICENSE
├── README.md
└── requirements.txt                           <- The requirements file for reproducing the analysis environment, e.g.
```
## Requirements and Environment

Requirements:
- pyenv with Python: 3.11.3

Environment: 

For installing the virtual environment you can either use the Makefile and run `make setup` or install it manually with the following commands: 

```Bash
pyenv local 3.11.3
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```


