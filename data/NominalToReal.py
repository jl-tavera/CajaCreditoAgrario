#%%
import functions as fx
import pandas as pd
import config as cf

'''
IPC
'''

ipc = fx.loadIpcXLSX('IPC/IPC.xlsx')

'''
1952
'''

year_1952 = fx.loadCleanYearCSV('DANE/nominal/1952_i_clean.csv')
year_1952 = fx.nominalToRealValues(year_1952, ipc, 1952)

fx.exportYear(year_1952, '1952_r_clean', 'r')

'''
1953
'''

year_1953 = fx.loadCleanYearCSV('DANE/nominal/1953_i_clean.csv')
year_1953 = fx.nominalToRealValues(year_1953, ipc, 1953)

fx.exportYear(year_1953, '1953_r_clean', 'r')

'''
1954
'''

year_1954 = fx.loadCleanYearCSV('DANE/nominal/1954_i_clean.csv')
year_1954 = fx.nominalToRealValues(year_1954, ipc, 1954)

fx.exportYear(year_1954, '1954_r_clean', 'r')

'''
1955
'''

year_1955 = fx.loadCleanYearCSV('DANE/nominal/1955_i_clean.csv')
year_1955 = fx.nominalToRealValues(year_1955, ipc, 1955)

fx.exportYear(year_1955, '1955_r_clean', 'r')

'''
1956
'''

year_1956 = fx.loadCleanYearCSV('DANE/nominal/1956_i_clean.csv')
year_1956 = fx.nominalToRealValues(year_1956, ipc, 1956)

fx.exportYear(year_1956, '1956_r_clean', 'r')

'''
1957
'''

year_1957 = fx.loadCleanYearCSV('DANE/nominal/1957_i_clean.csv')
year_1957 = fx.nominalToRealValues(year_1957, ipc, 1957)

fx.exportYear(year_1957, '1957_r_clean', 'r')

'''
1958
'''

year_1958 = fx.loadCleanYearCSV('DANE/nominal/1958_i_clean.csv')
year_1958 = fx.nominalToRealValues(year_1958, ipc, 1958)

fx.exportYear(year_1958, '1958_r_clean', 'r')

'''
1959
'''

year_1959 = fx.loadCleanYearCSV('DANE/nominal/1959_i_clean.csv')
year_1959 = fx.nominalToRealValues(year_1959, ipc, 1959)

fx.exportYear(year_1959, '1959_r_clean', 'r')

'''
1960
'''

year_1960 = fx.loadCleanYearCSV('DANE/nominal/1960_i_clean.csv')
year_1960 = fx.nominalToRealValues(year_1960, ipc, 1960)

fx.exportYear(year_1960, '1960_r_clean', 'r')

'''
1961
'''

year_1961 = fx.loadCleanYearCSV('DANE/nominal/1961_i_clean.csv')
year_1961 = fx.nominalToRealValues(year_1961, ipc, 1961)

fx.exportYear(year_1961, '1961_r_clean', 'r')

'''
1962
'''

year_1962 = fx.loadCleanYearCSV('DANE/nominal/1962_i_clean.csv')
year_1962 = fx.nominalToRealValues(year_1962, ipc, 1962)

fx.exportYear(year_1962, '1962_r_clean', 'r')


#    (_    /_\    _)
#    / `'--) (--'` \
#   /  _,-'\_/'-,_  \
#  /.-'     "     '-.\
