""" Module to provide cleaning functions for the data."""

import pandas as pd

def convert_dtype_cat_date(df: pd.DataFrame) -> pd.DataFrame:
    df_new = df.copy()
    convert_to_category = [
        "disrict",
        "region",
        "client_catg",
        "tarif_type",
        "counter_statue",
        "counter_code",
        "reading_remarque",
        "counter_type",
    ]
    convert_to_datetime = ["creation_date", "invoice_date"]
    for category in convert_to_category:
        df_new[category] = df_new[category].astype("category")

    df_new = df_new.rename(columns={"disrict": "district"})

    '''outlier_col = [
        "consommation_level_1",
        "consommation_level_2",
        "consommation_level_3",
        "consommation_level_4",
    ]

    # handle outliers with sdt above 3
    for col in outlier_col:
        threshold = 3 * df_new[col].std()
        mask_outliers = df_new[col] > df_new[col].mean() + threshold
        df_new = df_new[~mask_outliers]'''
        
    return df_new