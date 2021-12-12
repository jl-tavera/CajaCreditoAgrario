#%%
import pandas as pd
import geopandas as gpd
from shapely.geometry.geo import mapping
import animation as am
import matplotlib.pyplot as plt

'''
CHOROLOPLETH MAP CREATION
'''

'''
 MAP 
'''

map = am.loadGEOJSON('GeoJSON/Municipios.shp')
neighbors = am.neighborsMap(map)
map = am.intColumn(map, 'ID_ESPACIA')

am.exportPanelXLSX(neighbors, 'Neighbors/Vecinos')

'''
1952
'''

year_1952 = am.loadCodesCSV('Final/Years/year_1952_codes.csv')

year_1952_1 = am.pivotStats(year_1952, 'T - Numero')
year_1952_1 = am.intColumn(year_1952_1, 1952)

merge_1952_1 = pd.merge(year_1952_1, map, how = 'outer')
merge_1952_1 = am.fillNA(merge_1952_1)

year_1952_2 = am.pivotStats(year_1952, 'T - Valor')
year_1952_2 = am.intColumn(year_1952_2, 1952)

merge_1952_2 = pd.merge(year_1952_2, map, how = 'outer')
merge_1952_2 = am.fillNA(merge_1952_2)

merge_1952_1 = gpd.GeoDataFrame(merge_1952_1)
merge_1952_2 = gpd.GeoDataFrame(merge_1952_2)

am.titleMap(merge_1952_1, 1952, 0, 3000)
am.untitledMap(merge_1952_1, 1952, 0, 3000)

am.titleMap2(merge_1952_2, 1952, 0, 850000000)

'''
1953
'''

year_1953 = am.loadCodesCSV('Final/Years/year_1953_codes.csv')

year_1953_1 = am.pivotStats(year_1953, 'T - Numero')
year_1953_1 = am.intColumn(year_1953_1, 1953)

merge_1953_1 = pd.merge(year_1953_1, map, how = 'outer')
merge_1953_1 = am.fillNA(merge_1953_1)

year_1953_2 = am.pivotStats(year_1953, 'T - Valor')
year_1953_2 = am.intColumn(year_1953_2, 1953)

merge_1953_2 = pd.merge(year_1953_2, map, how = 'outer')
merge_1953_2 = am.fillNA(merge_1953_2)

merge_1953_1 = gpd.GeoDataFrame(merge_1953_1)
merge_1953_2 = gpd.GeoDataFrame(merge_1953_2)

am.titleMap(merge_1953_1, 1953, 0, 3200)
am.untitledMap(merge_1953_1, 1953, 0, 3200)

am.titleMap2(merge_1953_2, 1953, 0, 850000000)

'''
1954
'''

year_1954 = am.loadCodesCSV('Final/Years/year_1954_codes.csv')

year_1954_1 = am.pivotStats(year_1954, 'T - Numero')
year_1954_1 = am.intColumn(year_1954_1, 1954)

merge_1954_1 = pd.merge(year_1954, map, how = 'outer')
merge_1954_1 = am.fillNA(merge_1954_1)

year_1954_2 = am.pivotStats(year_1954, 'T - Valor')
year_1954_2 = am.intColumn(year_1954_2, 1954)

merge_1954_2 = pd.merge(year_1954, map, how = 'outer')
merge_1954_2 = am.fillNA(merge_1954_2)

merge_1954_1 = gpd.GeoDataFrame(merge_1954_1)
merge_1954_2 = gpd.GeoDataFrame(merge_1954_2)


am.titleMap(merge_1954_1, 1954, 0, 3400)
am.untitledMap(merge_1954_1, 1954, 0, 3400)

am.titleMap(merge_1954_2, 1954, 0, 3400)

'''
1955
'''

year_1955 = am.loadCodesCSV('Final/Years/year_1955_codes.csv')
year_1955 = am.pivotStats(year_1955, 'T - Numero')
year_1955 = am.intColumn(year_1955, 1955)

merge_1955 = pd.merge(year_1955, map, how = 'outer')
merge_1955 = am.fillNA(merge_1955)

merge_1955 = gpd.GeoDataFrame(merge_1955)

am.titleMap(merge_1955, 1955, 0, 3500)
am.untitledMap(merge_1955, 1955, 0, 3500)

'''
1956
'''

year_1956 = am.loadCodesCSV('Final/Years/year_1956_codes.csv')
year_1956 = am.pivotStats(year_1956, 'T - Numero')
year_1956 = am.intColumn(year_1956, 1956)

merge_1956 = pd.merge(year_1956, map, how = 'outer')
merge_1956 = am.fillNA(merge_1956)

merge_1956 = gpd.GeoDataFrame(merge_1956)

am.titleMap(merge_1956, 1956, 0, 3700)
am.untitledMap(merge_1956, 1956, 0, 3700)

'''
1957
'''

year_1957 = am.loadCodesCSV('Final/Years/year_1957_codes.csv')
year_1957 = am.pivotStats(year_1957, 'T - Numero')
year_1957 = am.intColumn(year_1957, 1957)

merge_1957 = pd.merge(year_1957, map, how = 'outer')
merge_1957 = am.fillNA(merge_1957)

merge_1957 = gpd.GeoDataFrame(merge_1957)

am.titleMap(merge_1957, 1957, 0, 3000)
am.untitledMap(merge_1957, 1957, 0, 3000)

'''
1958
'''

year_1958 = am.loadCodesCSV('Final/Years/year_1958_codes.csv')
year_1958 = am.pivotStats(year_1958, 'T - Numero')
year_1958 = am.intColumn(year_1958, 1958)

merge_1958 = pd.merge(year_1958, map, how = 'outer')
merge_1958 = am.fillNA(merge_1958)

merge_1958 = gpd.GeoDataFrame(merge_1958)

am.titleMap(merge_1958, 1958, 0, 3700)
am.untitledMap(merge_1958, 1958, 0, 3700)

'''
1959
'''

year_1959 = am.loadCodesCSV('Final/Years/year_1959_codes.csv')
year_1959 = am.pivotStats(year_1959, 'T - Numero')
year_1959 = am.intColumn(year_1959, 1959)

merge_1959 = pd.merge(year_1959, map, how = 'outer')
merge_1959 = am.fillNA(merge_1959)

merge_1959 = gpd.GeoDataFrame(merge_1959)

am.titleMap(merge_1959, 1959, 0, 4200)
am.untitledMap(merge_1959, 1959, 0, 4200)

'''
1960
'''

year_1960 = am.loadCodesCSV('Final/Years/year_1960_codes.csv')
year_1960 = am.pivotStats(year_1960, 'T - Numero')
year_1960 = am.intColumn(year_1960, 1960)

merge_1960 = pd.merge(year_1960, map, how = 'outer')
merge_1960 = am.fillNA(merge_1960)

merge_1960 = gpd.GeoDataFrame(merge_1960)

am.titleMap(merge_1960, 1960, 0, 4400)
am.untitledMap(merge_1960, 1960, 0, 4400)

'''
1962
'''

year_1962 = am.loadCodesCSV('Final/Years/year_1962_codes.csv')
year_1962 = am.pivotStats(year_1962, 'T - Numero')
year_1962 = am.intColumn(year_1962, 1962)

merge_1962 = pd.merge(year_1962, map, how = 'outer')
merge_1962 = am.fillNA(merge_1962)

merge_1962 = gpd.GeoDataFrame(merge_1962)

am.titleMap(merge_1962, 1962, 0, 5000)
am.untitledMap(merge_1962, 1962, 0, 5000)
