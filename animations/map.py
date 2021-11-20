#%%
import pandas as pd
import geopandas as gpd
import animation as am
import matplotlib.pyplot as plt

'''
CHOROLOPLETH MAP CREATION
'''

map = am.loadGEOJSON('GeoJSON/Municipios.shp')
map = am.intColumn(map, 'ID_ESPACIA')


year_1952 = am.loadCodesCSV('Final/Years/year_1952_codes.csv')
year_1952 = am.pivotStats(year_1952, 'T - Numero')
year_1952 = am.intColumn(year_1952, 1952)


merge_1952 = pd.merge(year_1952, map, how = 'outer')
merge_1952 = am.fillNA(merge_1952)


merge_1962 = gpd.GeoDataFrame(merge_1952)

year_1962 = am.loadCodesCSV('Final/Years/year_1962_codes.csv')
year_1962 = am.pivotStats(year_1962, 'T - Numero')
year_1962 = am.intColumn(year_1962, 1962)


merge_1962 = pd.merge(year_1962, map, how = 'outer')
merge_1962 = am.fillNA(merge_1962, 1962)

print(merge_1962.head())


merge_1962 = gpd.GeoDataFrame(merge_1962)

vmin, vmax = 0, 5000
fig = merge_1962.plot(column=1962, cmap='Purples', figsize=(10,10), linewidth=0.8, edgecolor='0.8', vmin=vmin, vmax=vmax, 
                       legend=True, norm=plt.Normalize(vmin=vmin, vmax=vmax))

# remove axis of chart
fig.axis('off')
    
    # add a title
fig.set_title('Número de Prestamos Caja Agraria por Municipio', \
              fontdict={'fontsize': '25',
                         'fontweight' : '3'})
only_year = 1952
    
# position the annotation to the bottom left
fig.annotate(only_year,
            xy=(0.1, .225), xycoords='figure fraction',
            horizontalalignment='left', verticalalignment='top',
            fontsize=35)


chart = fig.get_figure()
chart.savefig( '1962', dpi=300)

