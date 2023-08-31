import pandas as pd
import numpy as np

def convert_dtype_cat_date (df:pd.DataFrame)->pd.DataFrame:
    
    df_new =df.copy()
    convert_to_category = ['disrict', 'region', 'client_catg','tarif_type','counter_statue','counter_code', 'reading_remarque','counter_type']
    convert_to_datetime =['creation_date','invoice_date']

    for category in convert_to_category:
        df_new[category]=df_new[category].astype('category')
        
    df_new = df_new.rename(columns={'disrict':'district'})
   
    return df_new