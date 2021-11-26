#%%
import config as cf
import pandas as pd

'''
LOADING FUNCTIONS
'''


def loadYearCSV(path):

    route = cf.data_dir.replace('/App', '') + path
    year = pd.read_csv(route)
    return year


def loadYearXLSX(path):

    route = cf.data_dir.replace('/App', '') + path
    year = pd.read_excel(route)
    return year


def loadCleanYearCSV(path):

    route = cf.export_dir.replace('/App', '') + path
    year = pd.read_csv(route)
    return year


def loadIpcXLSX(path):
    
    route = cf.data_dir.replace('/App', '') + path  
    ipc = pd.read_excel(route)
    ipc = ipc.reset_index(
            level=None, drop=False, inplace=False, 
            col_level=0, col_fill= '')

    return ipc

def loadPanelCSV(path):
    
    route = cf.export_dir.replace('/App', '') + path  
    panel = pd.read_csv(route)
    panel = panel.reset_index(
            level=None, drop=False, inplace=False, 
            col_level=0, col_fill= '')

    return panel

def loadPanelXLSX(path): 
    route = cf.data_dir.replace('/App', '') + path
    panel = pd.read_excel(route)

    return panel


def loadDIVIPOLA(path):
    
    route = cf.data_dir.replace('/App', '') + path  
    divipola = pd.read_csv(route)
    divipola = divipola.reset_index(
            level=None, drop=False, inplace=False, 
            col_level=0, col_fill= '')

    return divipola

def loadPopulationXLSX(path):
    
    route = cf.data_dir.replace('/App', '') + path  
    population = pd.read_excel(route)
    population = population.reset_index(
            level=None, drop=False, inplace=False, 
            col_level=0, col_fill= '')

    return population

def loadControlsXLSX(path):
    
    route = cf.data_dir.replace('/App', '') + path  
    controls = pd.read_excel(route)
    controls = controls.reset_index(
            level=None, drop=False, inplace=False, 
            col_level=0, col_fill= '')

    return controls

def loadGroupedCSV(path):
    
    route = cf.export_dir.replace('/App', '') + path  
    controls = pd.read_csv(route)
    controls = controls.reset_index(
            level=None, drop=False, inplace=False, 
            col_level=0, col_fill= '')

    return controls

def loadLiteracyXLSX(path):
    
    route = cf.data_dir.replace('/App', '') + path  
    controls = pd.read_excel(route)
    controls = controls.reset_index(
            level=None, drop=False, inplace=False, 
            col_level=0, col_fill= '')

    return controls
'''
FORMAT & CLEANING FUNCTIONS
'''


def formatNumbers(df, col):
    for i, row in df.iterrows():
        row[col] = row[col].replace('.', '')
        row[col] = row[col].replace(',', '')
        row[col] = row[col].replace('•', '')
        row[col] = row[col].replace('%', '')
        row[col] = row[col].replace(':', '')
        row[col] = row[col].replace(';', '')
        row[col] = row[col].replace(' ', '')
        row[col] = row[col].replace('I', '1')
        row[col] = row[col].replace('l', '1')

    return df


def formatDecimal(lst): 
    num = []
    for i in lst:
        i = i//10
        num.append(i)

    return num


def numberCorrection(df):

    col_names = ['Oficina', 'Departamento']

    for col in df.columns:
        df[col] = df[col].apply(str)

    for col in df.columns:
        if col not in col_names:
            formatNumbers(df, col)

    for col in df.columns:
        if col not in col_names:
            df[col] = pd.to_numeric(df[col])

    return df


def nameCorrection(df):

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


def checkTotal(df):
    df['Check - Valor'] = (
        (df['CP - Valor'] + df['MP - Valor']) - df['T - Valor'])
    df['Check - Numero'] = (
        (df['CP - Numero'] + df['MP - Numero']) - df['T - Numero'])
    return df

def checkTotalLP(df):
    df['Check - Valor'] = (
        (df['CP - Valor'] + df['MP - Valor'] + df['LP - Valor']) 
                                - df['T - Valor'])
    df['Check - Numero'] = (
        (df['CP - Numero'] + df['MP - Numero'] + df['LP - Numero'])
                                 - df['T - Numero'])
    return df

def lower(df):

    col_names = ['Oficina', 'Departamento']
    for name in col_names:
        df[name].str.lower()
    return df


def getNames(df, col):
    names = []
    for i, row in df.iterrows():
        names.append(row[col])

    return names


def formatName(lst):
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

def createNewCol(df, name, value, pos): 
    lst = [value]*len(df)

    df = assign(df, name, value)
    df = rearrange(df, name, pos)

    return df

def nameDepYearID(df): 
    df['id'] = df['Departamento'].astype(str) + df['Oficina'].astype(str)
    return df

def nameDepID(df): 
    df['id'] = df['Nombre Departamento'].astype(str) + df['Nombre Municipio'].astype(str)
    df["id"].str[:-1]
    return df

def intColumn(df, column): 
    df[column] = df[column].astype(float)

    return df

'''
COMPARE FUNCTIONS
'''


def compareMun(lst1, lst2):
    diff = []
    for i in lst1:
        if i not in lst2:
            diff.append(i)
    return diff

def compareDIVIPOLA(df1,df2): 
    df1['id'] = df1['Departamento'].astype(str) + df1['Oficina'].astype(str)
    df2['id'] = df2['Nombre Departamento'].astype(str) + df2['Nombre Municipio'].astype(str)

    id_divipola = getNames(df2, 'id')
    id_divipola = formatName(id_divipola)

    id_panel = getNames(df1, 'id')
    compare = compareMun(id_panel, id_divipola)
    compare = list(dict.fromkeys(compare))

    return compare

def initialYear(controls, list_1952, list_1962):
    dummy_mpio = []
    for j in list_1962: 
        if j not in list_1952: 
            dummy_mpio.append(j)
    
    controls['tratamiento'] = 0

    for i, row in controls.iterrows():
        if row['codmpio'] in list_1952: 
            controls = controls.drop(i)

    for j, row in controls.iterrows():
        if row['codmpio'] in dummy_mpio: 
            controls.at[j, 'tratamiento'] = 1

        
    
    return controls 


'''
MERGE FUNCTIONS
'''

def mergeYears(df1, df2): 
    df = df1.copy()
    df = df.append(df2, ignore_index=True)
    df = df.sort_values(['Departamento', 'Oficina', 'Anio'])
    df = df.drop('Unnamed: 0', 1)
    df = df.reset_index()
    df = df.drop('index', 1)

    return df


def mergeYearsCodes(df1, df2): 
    df = df1.copy()
    df = df.append(df2, ignore_index=True)
    df = df.sort_values(['Departamento', 'cod_mpio', 'Anio'])
    df = df.reset_index()
    df = df.drop('index', 1)

    return df

def mergeStats(df1, df2): 
    df = df1.copy()
    df = df.append(df2, ignore_index=True)
    df = df.sort_values(['Departamento', 'Anio'])

    return df

def joinCode(panel, year): 
    panel = nameDepYearID(panel)
    panel.drop_duplicates(subset ="id",
                     keep = 'last', inplace = True)

    panel = panel[['Cod Dep', 'Cod Mun', 'id']]
    year = nameDepYearID(year)

    merge = pd.merge(panel, year)
    merge = merge.drop('Unnamed: 0', 1)
    merge = merge.drop('Unnamed: 0.1', 1)
    merge = merge.drop('id', 1)

    return merge

'''
PIVOT FUNCTIONS
'''

def pivotStats(df, var): 
    df = pd.pivot_table(
            df,
            values = var, 
            index=['Departamento'], 
            columns = 'Anio').reset_index()

    return df

def pivotPanel(df, var): 
    df = pd.pivot_table(
            df,
            values = var, 
            index=['Oficina'], 
            columns = 'Anio').reset_index()

    return df


'''
DATA FUNCTIONS
'''


def nominalToRealValues(df, ipc, year):
    col_names = ['Oficina', 'Departamento']

    for i, row in ipc.iterrows():
        if row['Anio'] == year: 
            deft = row['Base 1952']
            break 

    for col in df.columns:
        if (col not in col_names) and ('Valor' in col):
            df[col].astype(float)
            df[col] = df[col]/deft
    
    return df 
        

def statsDepartment(df): 
    col_names = []
    for col in df.columns: 
        if col != 'Anio': 
            col_names.append(col)
    df_stats = df.groupby(['Departamento'])[col_names].sum()

    return df_stats

def normalizePopulation(df, population, year):
    
    col_names = ['Oficina', 'Departamento']
    
    population = population[['cod_mpio', year]]
    df = df.rename(columns = {'Cod Mun': 'cod_mpio'})
    
    merge = pd.merge(df, population)

    for col in df.columns:
        if (col not in col_names) and ('Valor' in col):
            merge[col].astype(float)
            merge[col] = merge[col]/merge[year]
            merge[col] = merge[col].round(decimals=2)
    
    merge = merge.reset_index()
    merge = merge.rename(columns = {year : 'Poblacion'})
    merge = merge.drop("Unnamed: 0",axis=1)
    merge = merge.drop("index",axis=1)

    merge = rearrange(merge, 'Poblacion', 5)


    return merge
    
def averagesFinal(df):
    col_names = []
    for col in df.columns:
        if type(col) == str: 
            if 'Valor' in col:
                col_names.append(col)

    for col in df.columns:
        if (col in col_names )and ('T' not in col): 
            prefix = col[:5]

            df[prefix + str('Promedio')] = df[col]/ df['numero_prestamos']

        elif (col in col_names )and ('T' in col): 
            prefix = col[:4]

            df[prefix + str('Promedio')] = df[col]/ df['numero_prestamos']

    return df 
        
'''
EXPORT FUNCTIONS
'''


def exportYear(df, name, type):
    if type == 'r':
        route = cf.export_dir.replace('/App', '') + '/DANE/real/'
    if type == 'i': 
        route = cf.export_dir.replace('/App', '') + '/DANE/nominal/'
    if type == 's': 
        route = cf.export_dir.replace('/App', '') + 'DANE/stats/'
    df.to_csv(route + str(name) + '.csv')

    return None

def exportPanelCSV(df, name):
    route = cf.export_dir.replace('/App', '') + 'Panel/'
    df.to_csv(route + str(name) + '.csv')

    return None

def exportPanelXLSX(df, name):
    route = cf.export_dir.replace('/App', '') + 'Panel/'
    df.to_excel(route + str(name) + '.xlsx')

    return None

def exportCodeYearsCSV(df, name):
    route = cf.export_dir.replace('/App', '') + 'Final/Years/'
    df.to_csv(route + str(name) + '.csv')

    return None

def exportFinalCSV(df, name):
    route = cf.export_dir.replace('/App', '') + 'Final/'
    df.to_csv(route + str(name) + '.csv')

    return None


#    (_    /_\    _)
#    / `'--) (--'` \
#   /  _,-'\_/'-,_  \
#  /.-'     "     '-.\
