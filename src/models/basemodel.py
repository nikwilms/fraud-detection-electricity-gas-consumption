import pandas as pd
import numpy as np

def basemodel_predict_proba(df:pd.DataFrame)->pd.Series:
    y_pred = (df.client_catg == 51)  | (df.counter_code.isin([40,25])) #| ((df.consommation_level_1 <10000)& (df.consommation_level_2 <10000)& (df.consommation_level_3 <10000)& (df.consommation_level_4 <10000))
    y_proba = pd.Series(np.zeros(len(df)))
    y_proba.index = df.index
    y_proba[y_pred] = 1
    return y_proba

