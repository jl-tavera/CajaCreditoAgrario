#%%
import pandas as pd
import functions as fx

'''
DEPARTMENT PANEL
'''

year_1952 = fx.loadCleanYearCSV('DANE/stats/1952_S_clean.csv')
year_1953 = fx.loadCleanYearCSV('DANE/stats/1953_s_clean.csv')
year_1954 = fx.loadCleanYearCSV('DANE/stats/1954_s_clean.csv')
year_1955 = fx.loadCleanYearCSV('DANE/stats/1955_s_clean.csv')
year_1956 = fx.loadCleanYearCSV('DANE/stats/1956_s_clean.csv')
year_1957 = fx.loadCleanYearCSV('DANE/stats/1957_s_clean.csv')
year_1958 = fx.loadCleanYearCSV('DANE/stats/1958_s_clean.csv')
year_1959 = fx.loadCleanYearCSV('DANE/stats/1959_s_clean.csv')
year_1960 = fx.loadCleanYearCSV('DANE/stats/1960_s_clean.csv')
year_1961 = fx.loadCleanYearCSV('DANE/stats/1961_s_clean.csv')
year_1962 = fx.loadCleanYearCSV('DANE/stats/1962_s_clean.csv')

merge_1 = fx.mergeStats(year_1952, year_1953)
merge_2 = fx.mergeStats(merge_1, year_1954)
merge_3 = fx.mergeStats(merge_2, year_1955)
merge_4 = fx.mergeStats(merge_3, year_1956)
merge_5 = fx.mergeStats(merge_4, year_1957)
merge_6 = fx.mergeStats(merge_5, year_1958)
merge_7 = fx.mergeStats(merge_6, year_1959)
merge_8 = fx.mergeStats(merge_7, year_1960)
merge_9 = fx.mergeStats(merge_8, year_1961)
merge_10 = fx.mergeStats(merge_9, year_1962)

fx.exportPanel(merge_10, 'panel_departamental')

panel = fx.loadPanelCSV('Stats/panel_departamental.csv')

'''
PIVOT TABLES
'''

panel_CP_Numero = fx.pivotStats(panel, 'CP - Numero')
panel_CP_Valor = fx.pivotStats(panel, 'CP - Valor')
panel_MP_Numero = fx.pivotStats(panel, 'MP - Numero')
panel_MP_Valor = fx.pivotStats(panel, 'MP - Valor')
panel_LP_Numero = fx.pivotStats(panel, 'LP - Numero')
panel_LP_Valor = fx.pivotStats(panel, 'LP - Valor')
panel_T_Numero = fx.pivotStats(panel, 'T - Numero')
panel_T_Valor = fx.pivotStats(panel, 'T - Valor')

fx.exportPanelCSV(panel_CP_Numero, 'CP - Numero')
fx.exportPanelCSV(panel_CP_Valor, 'CP - Valor')
fx.exportPanelCSV(panel_MP_Numero, 'MP - Numero')
fx.exportPanelCSV(panel_MP_Valor, 'MP - Valor')
fx.exportPanelCSV(panel_LP_Numero, 'LP - Numero')
fx.exportPanelCSV(panel_LP_Valor, 'LP - Valor')
fx.exportPanelCSV(panel_T_Numero, 'T - Numero')
fx.exportPanelCSV(panel_T_Valor, 'T - Valor')





#    (_    /_\    _)
#    / `'--) (--'` \
#   /  _,-'\_/'-,_  \
#  /.-'     "     '-.\