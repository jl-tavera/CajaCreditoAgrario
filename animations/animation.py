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

    return df

'''
EXPORT FUNCTIONS
'''

def exportPanelXLSX(df, name):
    route = cf.export_dir.replace('/animations', '') 
    df.to_excel(route + str(name) + '.xlsx')

    return None


