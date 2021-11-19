#%%
import pandas as pd
import geopandas as gpd
import animation as am
import matplotlib.pyplot as plt

'''
CHOROLOPLETH MAP CREATION
'''

map = am.loadGEOJSON('GeoJSON/Municipios.shp')
map.plot()
plt.show()