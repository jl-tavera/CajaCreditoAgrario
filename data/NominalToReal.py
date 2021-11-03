#%%
import functions as fx
import pandas as pd
import config as cf

ipc = fx.loadIpcXLSX('IPC/IPC.xlsx')

# year_1952 = fx.loadCleanYearCSV('DANE/Nominal/1952_i_clean.csv')
# year_1952 = fx.nominalToRealValues(year_1952, ipc, 1952)

# fx.exportYear(year_1952, '1952_r_clean', 'r')

year_1953 = fx.loadCleanYearCSV('DANE/Nominal/1953_i_clean.csv')
year_1953 = fx.nominalToRealValues(year_1953, ipc, 1953)

fx.exportYear(year_1953, '1953_r_clean', 'r')
