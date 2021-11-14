#%%
import functions as fx
import pandas as pd
import config as cf

'''
REAL PANEL DATA
'''

year_1952 = fx.loadCleanYearCSV('DANE/real/1952_r_clean.csv')
year_1953 = fx.loadCleanYearCSV('DANE/real/1953_r_clean.csv')
year_1954 = fx.loadCleanYearCSV('DANE/real/1954_r_clean.csv')
year_1955 = fx.loadCleanYearCSV('DANE/real/1955_r_clean.csv')
year_1956 = fx.loadCleanYearCSV('DANE/real/1956_r_clean.csv')
year_1957 = fx.loadCleanYearCSV('DANE/real/1957_r_clean.csv')
year_1958 = fx.loadCleanYearCSV('DANE/real/1958_r_clean.csv')
year_1959 = fx.loadCleanYearCSV('DANE/real/1959_r_clean.csv')
year_1960 = fx.loadCleanYearCSV('DANE/real/1960_r_clean.csv')
year_1961 = fx.loadCleanYearCSV('DANE/real/1961_r_clean.csv')

merge_1 = fx.mergeYears(year_1952, year_1953)
merge_2 = fx.mergeYears(merge_1, year_1954)
merge_3 = fx.mergeYears(merge_2, year_1955)
merge_4 = fx.mergeYears(merge_3, year_1956)
merge_5 = fx.mergeYears(merge_4, year_1957)
merge_6 = fx.mergeYears(merge_5, year_1958)
merge_7 = fx.mergeYears(merge_6, year_1959)
merge_8 = fx.mergeYears(merge_7, year_1960)

fx.exportPanel(merge_8, 'panel')

'''
Real Panel Data
'''



#    (_    /_\    _)
#    / `'--) (--'` \
#   /  _,-'\_/'-,_  \
#  /.-'     "     '-.\