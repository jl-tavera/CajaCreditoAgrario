#%%
import pandas as pd
import geopandas as gpd
import animation as am
import matplotlib.pyplot as plt
import bar_chart_race as bcr

'''
LOAD STATS
'''

year_1952 = am.loadStatsCSV('1952_s_clean.csv')
year_1952 = am.pivotDepStats(year_1952, 'T - Numero')

year_1953 = am.loadStatsCSV('1953_s_clean.csv')
year_1953 = am.pivotDepStats(year_1953, 'T - Numero')

year_1954 = am.loadStatsCSV('1954_s_clean.csv')
year_1954 = am.pivotDepStats(year_1954, 'T - Numero')

year_1955 = am.loadStatsCSV('1955_s_clean.csv')
year_1955 = am.pivotDepStats(year_1955, 'T - Numero')

year_1956 = am.loadStatsCSV('1956_s_clean.csv')
year_1956 = am.pivotDepStats(year_1956, 'T - Numero')

year_1957 = am.loadStatsCSV('1957_s_clean.csv')
year_1957 = am.pivotDepStats(year_1957, 'T - Numero')

year_1958 = am.loadStatsCSV('1958_s_clean.csv')
year_1958 = am.pivotDepStats(year_1958, 'T - Numero')

year_1959 = am.loadStatsCSV('1959_s_clean.csv')
year_1959 = am.pivotDepStats(year_1959, 'T - Numero')

year_1960 = am.loadStatsCSV('1960_s_clean.csv')
year_1960 = am.pivotDepStats(year_1960, 'T - Numero')

year_1962 = am.loadStatsCSV('1962_s_clean.csv')
year_1962 = am.pivotDepStats(year_1962, 'T - Numero')

chart = year_1952.append(year_1953)
chart = chart.append(year_1954)
chart = chart.append(year_1955)
chart = chart.append(year_1956)
chart = chart.append(year_1957)
chart = chart.append(year_1958)
chart = chart.append(year_1959)
chart = chart.append(year_1960)
chart = chart.append(year_1962)
chart = am.fillNA(chart)
chart = chart.set_index('Anio')

bcr.bar_chart_race(df=chart, filename= None)



