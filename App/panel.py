#%%
import functions as fx
import pandas as pd
import config as cf


year_1952 = fx.loadCleanYearCSV('DANE/1952_clean.csv')
year_1953 = fx.loadCleanYearCSV('DANE/1953_clean.csv')
year_1954 = fx.loadCleanYearCSV('DANE/1954_clean.csv')
year_1955 = fx.loadCleanYearCSV('DANE/1955_clean.csv')
year_1956 = fx.loadCleanYearCSV('DANE/1956_clean.csv')
year_1957 = fx.loadCleanYearCSV('DANE/1957_clean.csv')
year_1958 = fx.loadCleanYearCSV('DANE/1958_clean.csv')
year_1959 = fx.loadCleanYearCSV('DANE/1959_clean.csv')
year_1960 = fx.loadCleanYearCSV('DANE/1960_clean.csv')

merge_1 = fx.mergeYears(year_1952, year_1953)
merge_2 = fx.mergeYears(merge_1, year_1954)
merge_3 = fx.mergeYears(merge_2, year_1955)
merge_4 = fx.mergeYears(merge_3, year_1956)
merge_5 = fx.mergeYears(merge_4, year_1957)
merge_6 = fx.mergeYears(merge_5, year_1958)
merge_7 = fx.mergeYears(merge_6, year_1959)
merge_8 = fx.mergeYears(merge_7, year_1960)


fx.exportPanel(merge_8, 'Panel')