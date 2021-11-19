import pandas as pd
import functions as fx

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
year_1962 = fx.loadCleanYearCSV('DANE/real/1962_r_clean.csv')

panel = fx.loadPanelXLSX('Panel/panel_input.xlsx')
merge = fx.joinCode(panel, year_1952)

fx.exportCodeYearsCSV(merge, 'year_1952_codes')







