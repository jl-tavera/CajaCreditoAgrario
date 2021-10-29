#%%
import config as cf 
import pandas as pd
import re
from unicodedata import normalize

'''
LOADING FUNCTIONS
'''

def load_year(path):
    route = cf.data_dir.replace('/App', '') + path 
    year = pd.read_csv(route)

    return year 

def load_year2(path):
    route = cf.data_dir.replace('/App', '') + path 
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

    col_names = ['Oficina', 'Departamento']

    for col in df.columns: 
         df[col] = df[col].apply(str)

    for col in df.columns: 
        if col not in col_names:
            format_numbers(df, col)

    for col in df.columns: 
       if col not in col_names:
         df[col] = pd.to_numeric(df[col])

    return df

def name_correction(df): 

    col_names = ['Oficina', 'Departamento']
    for name in col_names: 
        for i, row in df.iterrows():
            row[name] = row[name].replace('.', '')
            row[name] = row[name].replace(',', '')
            row[name] = row[name].replace('•', '')
            row[name] = row[name].replace('%', '')
            row[name] = row[name].replace(':', '')
            row[name] = row[name].replace('*', '')
            row[name] = row[name].replace('á', 'a')
            row[name] = row[name].replace('é', 'e')
            row[name] = row[name].replace('í', 'i')
            row[name] = row[name].replace('ó', 'o')
            row[name] = row[name].replace('ú', 'u')
            
            if row[name][0] == ' ': 
                row[name] = row[name][1:]

            lower = row[name].lower()
            row[name] = lower

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

    col_names = ['Oficina', 'Departamento']
    for name in col_names: 
        df[name].str.lower()
    return df

def get_names(df, col): 
    names = []
    for i, row in df.iterrows():
        names.append(row[col] )

    return names

def format_name(lst): 
    names = []
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
        names.append(i)

    return names

def assign(df, name, lst):
    df.loc[:, name] = lst 

    return df

def rearrange(df, name, pos): 
    first_col = df.pop(name)
    df.insert(pos, name, first_col)

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

def export(df, name): 
    route = cf.export_dir.replace('/App', '')
    df.to_csv( route + str(name)+ '.csv')

    return 
