#%%
import pandas as pd
import geopandas as gpd
import animation as am
import matplotlib.pyplot as plt

'''
CHOROLOPLETH MAP CREATION
'''

map = am.loadGEOJSON('GeoJSON/Municipios.shp')
panel = am.loadPanel('Panel/panel_input.xlsx')

am.exportPanelXLSX(panel, 'panel_id.xlsx')