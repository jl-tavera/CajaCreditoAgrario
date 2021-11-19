import pandas as pd
import geopandas as gpd
import config as cf

'''
LOADING FUNCTIONS
'''

def loadGEOJSON(path):
    route = cf.data_dir.replace('/App', '') + path
    map = gpd.read_file(route)

    return map


'''

'''