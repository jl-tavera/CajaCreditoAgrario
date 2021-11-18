#%%
import pandas as pd
import functions as fx

'''
PIVOT TABLES
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