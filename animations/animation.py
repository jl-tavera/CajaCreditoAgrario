import pandas as pd
import geopandas as gpd
import config as cf

'''
LOADING FUNCTIONS
'''

def loadGEOJSON(path):
    route = cf.data_dir.replace('/animations', '') + path
    map = gpd.read_file(route)

    return map

def loadPanel(path): 
    route = cf.data_dir.replace('/App', '') + path
    panel = pd.read_excel(route)

    return panel

def loadCodesCSV(path): 
    route = cf.export_dir.replace('/animations', '') + path
    year = pd.read_csv(route)

    return year

def loadStatsCSV(path): 
    route = cf.export_dir.replace('/animations', '') + 'DANE/stats/' + path
    stats = pd.read_csv(route)

    return stats


'''
DATA FUNCTIONS
'''
def fillNA(df): 
    df = df.fillna(0)
    return df

def intColumn(df, column): 
    df[column] = df[column].astype(int)

    return df


'''
PIVOT CODES
'''

def pivotStats(df, var): 
    df = pd.pivot_table(
            df,
            values = var, 
            index=['Cod Mun'], 
            columns = 'Anio').reset_index()
    df = df.rename({'Cod Mun': 'ID_ESPACIA'}, axis='columns')
    df['ID_ESPACIA'] = df['ID_ESPACIA'].astype(int)

    return df

def pivotDepStats(df, var): 
    df = pd.pivot_table(
            df,
            values = var, 
            index=['Anio'], 
            columns = 'Departamento').reset_index()


    return df

'''
EXPORT FUNCTIONS
'''

def exportPanelXLSX(df, name):
    route = cf.export_dir.replace('/animations', '') 
    df.to_excel(route + str(name) + '.xlsx')

    return None

#    (_    /_\    _)
#    / `'--) (--'` \
#   /  _,-'\_/'-,_  \
#  /.-'     "     '-.\