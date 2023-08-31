import pandas as pd
import numpy as np

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
    df_num = df_invoice.groupby("client_id")[cols_to_agg_num].agg(num_agg)
    df_mode = df_invoice.groupby("client_id")[cols_to_agg_mode].apply(lambda x: x.mode().iloc[0])
    df_ges = pd.concat([df_num,df_mode], axis=1)
    df_ges.reset_index(inplace=True)
    return df_ges


def agg_invoice_num_mode_monthly_weighting(
        df_invoice,
        cols_to_agg_num=["months_number",
                         "invoice_date",
                         "counter_coefficient"],
        cols_to_agg_num_weighted=["consommation_level_1","consommation_level_2",
                    "consommation_level_3","consommation_level_4",
                    ],
        cols_to_agg_mode = ["tarif_type", "counter_statue",
                            "counter_code", "reading_remarque",
                            "counter_type"],
        num_agg = "mean"):

    df_num_weighted= df_invoice.groupby("client_id")[cols_to_agg_num_weighted+["months_number"]].sum()
    for col in cols_to_agg_num_weighted: 
        df_num_weighted[col] = df_num_weighted[col]/ df_num_weighted["months_number"]
    df_num_weighted.drop(columns="months_number",inplace=True)
    df_num = df_invoice.groupby("client_id")[cols_to_agg_num].agg(num_agg)
    df_mode = df_invoice.groupby("client_id")[cols_to_agg_mode].apply(lambda x: x.mode().iloc[0])
    df_ges = pd.concat([df_num,df_mode,df_num_weighted], axis=1)
    df_ges.reset_index(inplace=True)
    return df_ges