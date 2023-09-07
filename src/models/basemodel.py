""" This module contains the basemodel used as a benchmark for the project """
import pandas as pd
import numpy as np


def basemodel_predict_proba(df: pd.DataFrame) -> pd.Series:
    """Simple heuristic to predict the probability of a customer to be fraudulent based on the EDA
        findings that fraudulent customers are more likely to be in client_category 51 or have a
        counter_code of 40 or 25.
    Args:
        df (pd.DataFrame): DataFrame containing the invoice data.
    Returns:
        pd.Series: Series containing the probability of churn for each client_id in df.
    """
    y_pred = (df.client_catg == 51) | (df.counter_code.isin([40, 25]))
    # Observation that fraudulent customers have a lower consumption level did not improve the model
    # | ((df.consommation_level_1 <10000)& (df.consommation_level_2 <10000)&
    #  (df.consommation_level_3 <10000)& (df.consommation_level_4 <10000))
    y_proba = pd.Series(np.zeros(len(df)))
    y_proba.index = df.index
    y_proba[y_pred] = 1
    return y_proba
