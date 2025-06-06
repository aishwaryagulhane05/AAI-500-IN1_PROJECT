# Contains functions related to data loading and preprocessing.

# Examples of functions:
    ## Loading datasets from CSV/JSON or databases.
    ## Handling missing values (imputation, removal).
    ## Encoding categorical variables.
    ## Scaling or normalizing numerical features.
    ## Splitting data into train/test sets.

# Helps keep your main workflow clean by modularizing data preparation code.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import missingno as msno
import category_encoders as ce
import janitor
from sklearn.impute import SimpleImputer, KNNImputer
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler
from sklearn.ensemble import IsolationForest
from sklearn.cluster import DBSCAN
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from scipy import stats
from feature_engine.outliers import Winsorizer
from fuzzywuzzy import fuzz
import warnings
warnings.filterwarnings("ignore")

# Checking if data has any special characters
import re


# Regular expression for special characters (non-alphanumeric)
def get_values_with_special_chars(df, column_name):
    """
    arguments:  a DataFrame and a column name 
    output:     returns a list of values containing special characters from that column
    """
    return df[df[column_name].apply(lambda x: bool(re.search(r'[^a-zA-Z0-9 ]', str(x))))][column_name].tolist()

#-------

def clean_dataframe_text(df):
    """
    Removes emojis and special characters from all string columns in the dataframe.
    Keeps only alphanumeric characters and spaces.
    If you want to apply this only to specific columns (e.g., ['ProductNo', 'CustomerName']), modify the loop:

    for col in ['ProductNo', 'CustomerName']:
    df[col] = df[col].apply(clean_text)
    """
    # Emoji pattern
    emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U00002500-\U00002BEF"
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        u"\U0001f926-\U0001f937"
        u"\U00010000-\U0010ffff"
        u"\u200d"
        u"\u2640-\u2642"
        u"\u2600-\u2B55"
        u"\u23cf"
        u"\u23e9"
        u"\u231a"
        u"\ufe0f"
        u"\u3030"
        "]+", flags=re.UNICODE)

    def clean_text(text):
        text = str(text)
        text = emoji_pattern.sub('', text)                      # Remove emojis
        text = re.sub(r'[^A-Za-z0-9 ]+', '', text)              # Remove special characters
        return text.strip()

    # Apply cleaning only on object (string) columns
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].apply(clean_text)

    return df


#-------
def clean_numeric_columns(df, cols=None, remove_zeros=False, remove_negatives=False,
                          outlier_method='iqr', drop_outliers=True):
    """
    Cleans numeric columns:
    - Optionally removes zero and negative values
    - Optionally removes outliers based on IQR or Z-score

    Parameters:
    - df: DataFrame
    - cols: list of columns to clean (if None, cleans all numeric columns)
    - remove_zeros: bool – if True, collects and removes zero values
    - remove_negatives: bool – if True, collects and removes negative values
    - outlier_method: 'iqr'(default) or 'zscore'
    - drop_outliers: bool – if True, removes rows with outliers

    Returns:
    - df_clean: cleaned DataFrame
    - df_neg: DataFrame containing rows with negative values (if any)
    - df_zero: DataFrame containing rows with zero values (if any)
    """
    df_clean = df.copy()
    df_neg = pd.DataFrame()
    df_zero = pd.DataFrame()
    
    if cols is None:
        cols = df_clean.select_dtypes(include=[np.number]).columns

    for col in cols:
        if remove_negatives:
            neg_rows = df_clean[df_clean[col] < 0]
            df_neg = pd.concat([df_neg, neg_rows])
            df_clean = df_clean[df_clean[col] >= 0]

        if remove_zeros:
            zero_rows = df_clean[df_clean[col] == 0]
            df_zero = pd.concat([df_zero, zero_rows])
            df_clean = df_clean[df_clean[col] != 0]

        # Outlier bounds
        if outlier_method == 'iqr':
            Q1 = df_clean[col].quantile(0.25)
            Q3 = df_clean[col].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
        elif outlier_method == 'zscore':
            mean = df_clean[col].mean()
            std = df_clean[col].std()
            lower_bound = mean - 3 * std
            upper_bound = mean + 3 * std
        else:
            raise ValueError("Invalid outlier_method. Use 'iqr' or 'zscore'.")

        if drop_outliers:
            df_clean = df_clean[(df_clean[col] >= lower_bound) & (df_clean[col] <= upper_bound)]

    return df_clean, df_neg, df_zero

#-----------

def clean_numeric_columns_replace_outliers(df, cols=None, method='iqr', replace_with='median'):
    """
    Detects outliers in numeric columns and replaces them with mean or median.
    
    Parameters:
    - df: pandas DataFrame
    - cols: list of columns to clean (default: all numeric columns)
    - method: 'iqr' or 'zscore'
    - replace_with: 'mean' or 'median'
    
    Returns: cleaned DataFrame
    """
    df_clean = df.copy()
    
    if cols is None:
        cols = df_clean.select_dtypes(include=[np.number]).columns
    
    for col in cols:
        if method == 'iqr':
            Q1 = df_clean[col].quantile(0.25)
            Q3 = df_clean[col].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
        elif method == 'zscore':
            mean = df_clean[col].mean()
            std = df_clean[col].std()
            lower_bound = mean - 3 * std
            upper_bound = mean + 3 * std
        else:
            raise ValueError("Invalid method. Use 'iqr' or 'zscore'.")
        
        # Replace outliers
        replacement_value = df_clean[col].median() if replace_with == 'median' else df_clean[col].mean()
        df_clean[col] = df_clean[col].apply(
            lambda x: replacement_value if x < lower_bound or x > upper_bound else x
        )
        
    return df_clean

#---------
def clean_object_columns(df, remove_values=['Unspecified', 'Unknown', '-', 'nan']):
    """
    Cleans all object columns in the dataframe:
    - Strips whitespace
    - Removes special characters (optional)
    - Standardizes to title case
    - Replaces empty strings and unwanted placeholder values with np.nan
    """
    for col in df.select_dtypes(include='object').columns:
        df[col] = df[col].astype(str).str.strip()                           # Remove leading/trailing spaces
        df[col] = df[col].str.replace(r'\s+', ' ', regex=True)             # Collapse multiple spaces
        df[col] = df[col].str.replace(r'[^\w\s]', '', regex=True)          # Remove special characters
        df[col] = df[col].str.title()                                      # Title case standardization
        
        # Replace unwanted placeholders with NaN
        df[col] = df[col].replace(remove_values, np.nan, regex=False)
        df[col] = df[col].replace('', np.nan)                              # Replace empty strings with NaN
        
    return df
# ----------

def track_observations(observation, obs_type='finding', log_list=[]):
    """
    Tracks observations with types in a persistent list without duplicates.

    Parameters:
        observation (str): The observation to record.
        obs_type (str): Type of observation - one of ['finding', 'conclusion', 'cleaning'].
        log_list (list): (Optional) Persistent list storing all observations as dicts.

    Returns:
        list of dict: Updated list of observations with their types.
    """
    valid_types = ['finding', 'conclusion', 'cleaning', 'to_change']
    if obs_type not in valid_types:
        raise ValueError(f"Invalid obs_type '{obs_type}'. Must be one of {valid_types}.")

    # Check for duplicates before adding
    exists = any(
        entry['observation'] == observation and entry['type'] == obs_type
        for entry in log_list
    )
    if not exists:
        log_list.append({'observation': observation, 'type': obs_type})
    return log_list




