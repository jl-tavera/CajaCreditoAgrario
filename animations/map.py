#%%
import pandas as pd
import geopandas as gpd
import animation as am
import matplotlib.pyplot as plt

'''
CHOROLOPLETH MAP CREATION
'''

map = am.loadGEOJSON('GeoJSON/Municipios.shp')
am.exportPanelXLSX(map, 'mapa')


year_1952 = am.loadCodesCSV('Final/Years/year_1952_codes.csv')
year_1952 = am.pivotStats(year_1952, 'T - Numero')

merge_1952 = pd.concat(year_1952, map)


