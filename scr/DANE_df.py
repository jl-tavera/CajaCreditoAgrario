#%%
import config as cf
import pandas as pd

'''
LOADING FUNCTIONS
'''

def load_year(path):
    route = cf.data_dir + path
    year = pd.read_csv(route)
    return year 


year_1952 = load_year('DANE/1952.csv')
year_1953 = load_year('DANE/1953.csv')


'''
FORMAT FUNCTIONS
'''

def format_numbers(df, col): 
    for i, row in df.iterrows(): 
        row[col] =  row[col].replace('.', '')
        row[col] =  row[col].replace(',', '')
        row[col] =  row[col].replace('•', '')
        row[col] =  row[col].replace('%', '')
        row[col] =  row[col].replace(':', '')
  
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


        row['Oficina'] = row['Oficina'].lower()

    return df

def check_total(df):  
    df['Check - Valor'] = ((df['CP - Valor'] + df['MP - Valor']) - df['T - Valor'] )
    df['Check - Numero'] = ((df['CP - Numero'] + df['MP - Numero']) - df['T - Numero'] )
    return df

def get_mun(df): 
    mun = []
    for i, row in df.iterrows():
        mun.append(row['Oficina'] )

    return mun

'''
CLEAN DATABASES
'''

year_1952 = name_correction(year_1952)
year_1952 = number_correction(year_1952)
year_1952 = check_total(year_1952)

year_1952.to_csv('1952')
mun_1952 = get_mun(year_1952)

year_1953 = name_correction(year_1953)
year_1953 = number_correction(year_1953)
year_1953 = check_total(year_1953)

year_1953.to_csv('1953')
mun_1953 = get_mun(year_1953)



