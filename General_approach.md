# Fraud detection approach



* Customer multiple invoices problem
   * deal with multiple invoices per customer
   * aggregate invoices over mean consumption per customer_id


* Initial team task distribution
   * identify interesting variables
   * decide on which variables to drop
   * clean remaining data set (outliers)
   * analyse data set fo skewness, etc.
   * Aggregate customers
   * Base model (use logical rules, e.g. frauds related to districts, number of invoices, etc.)
   * Decide on models to use (test runs with different models on smaller data sets - test by each team member)


Fraud Detection
### **Value of Product:**
   * Identify potential candidates involved in fraudulent meter-reading activities, safe money

### **Prediction:**
   * Customer is fraudulent

### **Evaluation Metric:**
   * ROC-AUC (recommended and given by Zindi)

### **Baseline Model:**
   * Customers in client_category 51, counter_code 40 or 25 and consumptions levels 1-4 <= 10.000 are more likely to be fraudulent

def basemodel_predict_proba(df:pd.DataFrame)->pd.Series:
    y_pred = (df.client_catg == 51)  | (df.counter_code.isin([40,25])) #| ((df.consommation_level_1 <10000)& (df.consommation_level_2 <10000)& (df.consommation_level_3 <10000)& (df.consommation_level_4 <10000))
    y_proba = pd.Series(np.zeros(len(df)))
    y_proba.index = df.index
    y_proba[y_pred] = 1
    return y_proba

### Score:
   * ROC-AUC score = 0.5122781967869612



### Data Cleaning
    * drop counter number
    * counter coeff - drop outliers
    * convert date time
    * drop outliers for months
    * 

