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

merge_1952 = fx.joinCode(panel, year_1952)
merge_1953 = fx.joinCode(panel, year_1953)
merge_1954 = fx.joinCode(panel, year_1954)
merge_1955 = fx.joinCode(panel, year_1955)
merge_1956 = fx.joinCode(panel, year_1956)
merge_1957 = fx.joinCode(panel, year_1957)
merge_1958 = fx.joinCode(panel, year_1958)
merge_1959 = fx.joinCode(panel, year_1959)
merge_1960 = fx.joinCode(panel, year_1960)
merge_1961 = fx.joinCode(panel, year_1961)
merge_1962 = fx.joinCode(panel, year_1961)

fx.exportCodeYearsCSV(merge_1952, 'year_1952_codes')
fx.exportCodeYearsCSV(merge_1953, 'year_1953_codes')
fx.exportCodeYearsCSV(merge_1954, 'year_1954_codes')
fx.exportCodeYearsCSV(merge_1955, 'year_1955_codes')
fx.exportCodeYearsCSV(merge_1956, 'year_1956_codes')
fx.exportCodeYearsCSV(merge_1957, 'year_1957_codes')
fx.exportCodeYearsCSV(merge_1958, 'year_1958_codes')
fx.exportCodeYearsCSV(merge_1959, 'year_1959_codes')
fx.exportCodeYearsCSV(merge_1960, 'year_1960_codes')
fx.exportCodeYearsCSV(merge_1961, 'year_1961_codes')
fx.exportCodeYearsCSV(merge_1962, 'year_1962_codes')







