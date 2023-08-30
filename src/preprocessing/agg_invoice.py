import pandas as pd

def agg_invoice_num_mode_no_monthly_weighting(
        df_invoice,
        cols_to_agg_mean=["consommation_level_1","consommation_level_2",
                          "consommation_level_3","consommation_level_4",
                          "counter_coefficient", "months_number",
                          "invoice_date"
                         ],
        cols_to_agg_mode = ["tarif_type", "counter_statue",
                            "counter_code", "reading_remarque",
                            "counter_type"],
        num_agg = "mean"):
    df_num =df_invoice.head(100).groupby("client_id")[cols_to_agg_num].agg(num_agg)
    df_mode = df_invoice.head(100).groupby("client_id")[cols_to_agg_mode].apply(lambda x: x.mode().iloc[0])
    df_ges = pd.concat([df_num,df_mode], axis=1)
    df_ges = df_num
    df_ges.reset_index(inplace=True)
    return df_ges


