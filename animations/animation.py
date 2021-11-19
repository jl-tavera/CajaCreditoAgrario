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

'''
EXPORT FUNCTIONS
'''

def exportPanelXLSX(df, name):
    route = cf.export_dir.replace('/animations', '') 
    df.to_excel(route + str(name) + '.xlsx')

    return None
