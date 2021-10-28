#%%
import config as cf 
import pandas as pd
import re
from unicodedata import normalize

'''
LOADING FUNCTIONS
'''

def load_year(path):
    route = cf.data_dir.replace('/scr', '') + path
   
    year = pd.read_csv(route)

    return year 

def load_year2(path):
    route = cf.data_dir.replace('/scr', '') + path
   
    year = pd.read_excel(route)

    return year 

'''
FORMAT & CLEANING FUNCTIONS
'''

def format_numbers(df, col): 
    for i, row in df.iterrows(): 
        row[col] =  row[col].replace('.', '')
        row[col] =  row[col].replace(',', '')
        row[col] =  row[col].replace('•', '')
        row[col] =  row[col].replace('%', '')
        row[col] =  row[col].replace(':', '')
        row[col] =  row[col].replace(' ', '')
        row[col] =  row[col].replace('I', '1')
        row[col] =  row[col].replace('l', '1')
  
    return df


def number_correction(df):
    for col in df.columns: 
         df[col] = df[col].apply(str)

    for col in df.columns: 
        if col != 'Oficina':
            format_numbers(df, col)

    for col in df.columns: 
       if col != 'Oficina':
         df[col] = pd.to_numeric(df[col])

    return df

def name_correction(df): 
  
    for i, row in df.iterrows():
        row['Oficina'] = row['Oficina'].replace('.', '')
        row['Oficina'] = row['Oficina'].replace(',', '')
        row['Oficina'] = row['Oficina'].replace('•', '')
        row['Oficina'] = row['Oficina'].replace('%', '')
        row['Oficina'] = row['Oficina'].replace(':', '')
        row['Oficina'] = row['Oficina'].replace('*', '')
        row['Oficina'] = row['Oficina'].replace('á', 'a')
        row['Oficina'] = row['Oficina'].replace('é', 'e')
        row['Oficina'] = row['Oficina'].replace('í', 'i')
        row['Oficina'] = row['Oficina'].replace('ó', 'o')
        row['Oficina'] = row['Oficina'].replace('ú', 'u')
        
        if row['Oficina'][0] == ' ': 
            row['Oficina'] = row['Oficina'][1:]

        lower = row['Oficina'].lower()
        row['Oficina'] = lower

    return df


def str_correction(df): 
    for i, row in df.iterrows():
        s = row['Oficina']
        s = re.sub( 
            r"([^n\u0300-\u036f]|n(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]+", r"\1", 
            normalize( "NFD", s), 0, re.I
        )
        s = normalize( 'NFC', s)
        row['Oficina'].lower()
        
    return df

def check_total(df):  
    df['Check - Valor'] = ((df['CP - Valor'] + df['MP - Valor']) - df['T - Valor'] )
    df['Check - Numero'] = ((df['CP - Numero'] + df['MP - Numero']) - df['T - Numero'] )
    return df

def lower(df): 
    df['Oficina'].str.lower()
    return df

def get_mun(df): 
    mun = []
    for i, row in df.iterrows():
        mun.append(row['Oficina'] )

    return mun

def format_mun(lst): 
    mun = []
    for i in lst: 
        i = i.replace('.', '')
        i = i .replace(',', '')
        i = i .replace('•', '')
        i = i .replace('%', '')
        i = i .replace(':', '')
        i = i .replace('*', '')
        i = i .replace('á', 'a')
        i = i .replace('é', 'e')
        i = i .replace('í', 'i')
        i = i .replace('ó', 'o')
        i = i .replace('ú', 'u')

        i = i.lower()
        mun.append(i)

    return mun

def assign(df, name, lst):
    df.loc[:, name] = lst 

    return df

def rearrange(df, name): 
    first_col = df.pop(name)
    df.insert(0, name, first_col)

    return df

'''
CLEAN DATABASES
'''

'''
COMPARE FUNCTIONS
'''
def compare_mun(lst1, lst2): 
    diff = []
    for i in lst1: 
        if i not in lst2: 
            diff.append(i)
    return diff 


'''
EXPORT FUNCTIONS
'''

