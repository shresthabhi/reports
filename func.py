import pandas as pd
import numpy as np
import re
import os
import gdown
from datetime import datetime
import json
# from IPython import display


def read_drive_csv(url = '', date_columns = None):
    url = 'https://drive.google.com/uc?id=' + url.split('/')[-2]
    return pd.read_csv(url, parse_dates = date_columns)

def read_drive_excel(url = '', date_columns = None):
    file_id = url.split('/d/')[1].split('/')[0]
    url = f'https://drive.google.com/uc?export=download&id={file_id}'
    return pd.read_excel(url, parse_dates = date_columns)

def lower_and_join_columns(data):
    new_column_names = {}

    for col in data.columns:
        new_column_names[col] = str.join('_', re.sub(r'[^a-zA-Z\s_]', '', col).lower().strip().split(' '))
    return data.rename(columns = new_column_names)

def convert_and_fill_nan(data):
    for col in data.columns:
        if(data[col].dtype == 'object'):
            data[col] = data[col].fillna('NaN')
            data[col] = data[col].astype('str')
    return data

def convert_to_int(x):
    try:
        return np.int64(x)
    except:
        return np.nan
    
def fill_intNA(data, columns):
    for col in columns:
        data[col] = data[col].fillna(np.nan)

    return data
    
def convert_col_to_int(data, columns):
    for col in columns:
        data[col] = data[col].apply(convert_to_int)
        print('converted {}'.format(col))
    
    return data

def convert_col_to_int_astype(data, columns):
    for col in columns:
        # data[col] = data[col].astype(np.float64).fillna(np.nan).astype(np.int64)
        data[col] = data[col].astype('Int64')
        # data[col] = data[col].fillna(pd.NA)
    return data

def read_large_csv(url = ''):
    output = "data.csv"
    
    file_id = url.split("/d/")[1].split("/")[0]
    
    base_url = "https://drive.google.com/uc?id="
    modified_url = base_url + file_id
    gdown.download(modified_url, output, quiet=False)

    return pd.read_csv(output)
