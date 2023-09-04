""" Module to aggregate invoice data by client_id."""

import pandas as pd
import numpy as np


def agg_invoice_num_mode_no_monthly_weighting(
        df_invoice,
        cols_to_agg_num=["consommation_level_1", "consommation_level_2",
                         "consommation_level_3", "consommation_level_4",
                         "counter_coefficient", "months_number",
                         "invoice_date"
                         ],
        cols_to_agg_mode=["tarif_type", "counter_statue",
                          "counter_code", "reading_remarque",
                          "counter_type"],
        num_agg="mean"):
    """ Aggregate invoice data by client_id, using the mean for numerical features in
        cols_to_agg_num, and the mode for categorical features in cols_to_agg_mode.
    Args:
        df_invoice (pd.DataFrame): invoice data
        cols_to_agg_num (list, optional): Numerical features to aggregate using the mean.
            Defaults to ["consommation_level_1","consommation_level_2", "consommation_level_3",
            "consommation_level_4", "counter_coefficient", "months_number", "invoice_date"].
        cols_to_agg_mode (list, optional): Categorical features to aggregate using the mode.
            Defaults to ["tarif_type", "counter_statue", "counter_code",
            "reading_remarque", "counter_type"].
        num_agg (str, optional): Aggregation method for numerical features in cols_to_agg_num.
            Defaults to "mean".

    Returns:
        pd.DataFrame: updated DataFrame
    """
    df_num = df_invoice.groupby("client_id")[cols_to_agg_num].agg(num_agg)
    df_mode = df_invoice.groupby("client_id")[cols_to_agg_mode].apply(
        lambda x: x.mode().iloc[0])
    df_ges = pd.concat([df_num, df_mode], axis=1)
    df_ges.reset_index(inplace=True)
    return df_ges


def agg_invoice_num_mode_monthly_weighting(
        df_invoice: pd.DataFrame,
        cols_to_agg_num=["months_number",
                         "invoice_date",
                         "counter_coefficient"],
        cols_to_agg_num_weighted=["consommation_level_1", "consommation_level_2",
                                  "consommation_level_3", "consommation_level_4",
                                  ],
        cols_to_agg_mode=["tarif_type", "counter_statue",
                          "counter_code", "reading_remarque",
                          "counter_type"],
        num_agg="mean") -> pd.DataFrame:
    """ Aggregate invoice data by client_id, using the mean for numerical features in
        cols_to_agg_num, the weighted mean for numerical features in cols_to_agg_num_weighted, 
        and the mode for categorical features in cols_to_agg_mode.
    Args:
        df_invoice (pd.DataFrame): invoice data
        cols_to_agg_num (list, optional): Numerical features to aggregate using the mean.
            Defaults to ["months_number", "invoice_date", "counter_coefficient"].
        cols_to_agg_num_weighted (list, optional): Numerical features to aggregate using the
            weighted mean. Defaults to ["consommation_level_1","consommation_level_2",
            "consommation_level_3","consommation_level_4", ].
        cols_to_agg_mode (list, optional): Categorical features to aggregate using the mode.
            Defaults to ["tarif_type", "counter_statue", "counter_code",
            "reading_remarque", "counter_type"].
        num_agg (str, optional): Aggregation method for numerical features in cols_to_agg_num.
            Defaults to "mean".

    Returns:
        pd.DataFrame: updated DataFrame
    """
    # Aggregation of weighted numerical features by months_number
    df_num_weighted = df_invoice.groupby(
        "client_id")[cols_to_agg_num_weighted+["months_number"]].sum()
    for col in cols_to_agg_num_weighted:
        df_num_weighted[col] = df_num_weighted[col] / \
            df_num_weighted["months_number"]
    df_num_weighted.drop(columns="months_number", inplace=True)
    # Aggregation of numerical and categorical features
    df_num = df_invoice.groupby("client_id")[cols_to_agg_num].agg(num_agg)
    df_mode = df_invoice.groupby("client_id")[cols_to_agg_mode].apply(
        lambda x: x.mode().iloc[0])
    df_ges = pd.concat([df_num, df_mode, df_num_weighted], axis=1)
    df_ges.reset_index(inplace=True)
    return df_ges



def agg_cons_monthly_weighting(df, cols_to_agg_num_weighted, suffix=""):
    df_monthly_weighted = df.groupby(
    ["client_id"])[cols_to_agg_num_weighted+["months_number"]].sum()
    for col in cols_to_agg_num_weighted:
        df_monthly_weighted[col+suffix] = df_monthly_weighted[col] / \
            df_monthly_weighted["months_number"]
        df_monthly_weighted.drop(columns=col, inplace=True)
    df_monthly_weighted.drop(columns="months_number", inplace=True)
    return df_monthly_weighted


def agg_invoice_smart(
        df_invoice,
cols_to_agg_min = ["invoice_date"],
cols_to_agg_num=["counter_coefficient"],
cols_to_agg_num_weighted=["consommation_level_1", "consommation_level_2",
                            "consommation_level_3", "consommation_level_4",
                            ],
cols_to_agg_mode=["tarif_type", "counter_statue",
                    "counter_code", "reading_remarque"],
num_agg="mean"):
    df_counter_type_elec = df_invoice[df_invoice.counter_type=="ELEC"]
    df_counter_type_gaz = df_invoice[df_invoice.counter_type=="GAZ"]

    df_monthly_weighted_elec = agg_cons_monthly_weighting(df_counter_type_elec, cols_to_agg_num_weighted, "_elec")

    df_monthly_weighted_gaz = agg_cons_monthly_weighting(df_counter_type_gaz, cols_to_agg_num_weighted, "_gaz")

    # aggregation of features by min
    df_min= df_invoice.groupby(["client_id"])[cols_to_agg_min].min()

    # add duration of customer relationship
    df_invoice['invoice_date'] = pd.to_datetime(df_invoice['invoice_date'])
    df_max_date = df_invoice.groupby(["client_id"])["invoice_date"].max()
    df_min_date = df_invoice.groupby(["client_id"])["invoice_date"].min()
    df_date = (df_max_date - df_min_date)
    # convert to months
    df_date_months = (df_date.dt.days / 30.44).apply(np.ceil).astype(int)
    df_date_months = pd.DataFrame(df_date_months).rename(columns={"invoice_date":"months_number"})

    # Aggregation of numerical and categorical features
    df_date = df_invoice.groupby(["client_id"])[["invoice_date"]].max()- df_invoice.groupby(["invoice_date"])[cols_to_agg_min].min()

    df_num = df_invoice.groupby(["client_id"])[cols_to_agg_num].agg(num_agg)
    df_mode = df_invoice.groupby(["client_id"])[cols_to_agg_mode].apply(
        lambda x: x.mode().iloc[0])
    #df_ges = pd.concat([df_num, df_mode, df_num_weighted], axis=1)
    df_ges = pd.concat([df_min, df_date_months, df_num,  df_mode, df_monthly_weighted_elec,df_monthly_weighted_gaz], axis=1)
    df_ges.fillna(0, inplace=True)
    df_ges.reset_index(inplace=True)
    return df_ges
