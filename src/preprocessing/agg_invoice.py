""" Module to aggregate invoice data by client_id."""

import pandas as pd

def agg_invoice_num_mode_no_monthly_weighting(
        df_invoice,
        cols_to_agg_num=["consommation_level_1","consommation_level_2",
                          "consommation_level_3","consommation_level_4",
                          "counter_coefficient", "months_number",
                          "invoice_date"
                         ],
        cols_to_agg_mode = ["tarif_type", "counter_statue",
                            "counter_code", "reading_remarque",
                            "counter_type"],
        num_agg = "mean"):
    """ Aggregate invoice data by client_id, using the mean for numerical features in cols_to_agg_num, and the mode for categorical features in cols_to_agg_mode.
    Args:
        df_invoice (pd.DataFrame): invoice data
        cols_to_agg_num (list, optional): Numerical features to aggregate using the mean. Defaults to ["consommation_level_1","consommation_level_2", "consommation_level_3","consommation_level_4", "counter_coefficient", "months_number", "invoice_date"].
        cols_to_agg_mode (list, optional): Categorical features to aggregate using the mode. Defaults to ["tarif_type", "counter_statue", "counter_code", "reading_remarque", "counter_type"].
        num_agg (str, optional): Aggregation method for numerical features in cols_to_agg_num. Defaults to "mean".

    Returns:
        pd.DataFrame: updated DataFrame
    """
    df_num = df_invoice.groupby("client_id")[cols_to_agg_num].agg(num_agg)
    df_mode = df_invoice.groupby("client_id")[cols_to_agg_mode].apply(lambda x: x.mode().iloc[0])
    df_ges = pd.concat([df_num,df_mode], axis=1)
    df_ges.reset_index(inplace=True)
    return df_ges


def agg_invoice_num_mode_monthly_weighting(
        df_invoice:pd.DataFrame,
        cols_to_agg_num=["months_number",
                         "invoice_date",
                         "counter_coefficient"],
        cols_to_agg_num_weighted=["consommation_level_1","consommation_level_2",
                    "consommation_level_3","consommation_level_4",
                    ],
        cols_to_agg_mode = ["tarif_type", "counter_statue",
                            "counter_code", "reading_remarque",
                            "counter_type"],
        num_agg = "mean")->pd.DataFrame:
    """ Aggregate invoice data by client_id, using the mean for numerical features in cols_to_agg_num, the weighted mean for numerical features in cols_to_agg_num_weighted, 
        and the mode for categorical features in cols_to_agg_mode.
    Args:
        df_invoice (pd.DataFrame): invoice data
        cols_to_agg_num (list, optional): Numerical features to aggregate using the mean. Defaults to ["months_number", "invoice_date", "counter_coefficient"].
        cols_to_agg_num_weighted (list, optional): Numerical features to aggregate using the weighted mean. Defaults to ["consommation_level_1","consommation_level_2", "consommation_level_3","consommation_level_4", ].
        cols_to_agg_mode (list, optional): Categorical features to aggregate using the mode. Defaults to ["tarif_type", "counter_statue", "counter_code", "reading_remarque", "counter_type"].
        num_agg (str, optional): Aggregation method for numerical features in cols_to_agg_num. Defaults to "mean".

    Returns:
        pd.DataFrame: updated DataFrame
    """
    # Aggregation of weighted numerical features by months_number
    df_num_weighted= df_invoice.groupby("client_id")[cols_to_agg_num_weighted+["months_number"]].sum()
    for col in cols_to_agg_num_weighted: 
        df_num_weighted[col] = df_num_weighted[col]/ df_num_weighted["months_number"]
    df_num_weighted.drop(columns="months_number",inplace=True)
    # Aggregation of numerical and categorical features
    df_num = df_invoice.groupby("client_id")[cols_to_agg_num].agg(num_agg)
    df_mode = df_invoice.groupby("client_id")[cols_to_agg_mode].apply(lambda x: x.mode().iloc[0])
    df_ges = pd.concat([df_num,df_mode,df_num_weighted], axis=1)
    df_ges.reset_index(inplace=True)
    return df_ges