# src/common_imports.py
!pip install tabulate

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
from tabulate import tabulate

# Optional: Add __all__ to control * imports
__all__ = [
    'pd', 'np', 'plt', 'sns', 'msno', 'ce', 'janitor',
    'SimpleImputer', 'KNNImputer',
    'StandardScaler', 'MinMaxScaler', 'RobustScaler',
    'IsolationForest', 'DBSCAN', 'Pipeline',
    'train_test_split', 'LinearRegression', 'mean_squared_error',
    'stats', 'Winsorizer', 'fuzz', 'warnings'
]
