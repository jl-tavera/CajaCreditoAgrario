#%%
import functions as f
import pandas as pd
import sys


year_1952 = f.load_year('DANE/1952.csv')
year_1953 = f.load_year('DANE/1953.csv')

year_1952 = f.name_correction(year_1952)
year_1952 = f.number_correction(year_1952)
year_1952 = f.check_total(year_1952)

mun_1952 = f.get_mun(year_1952)

year_1953 = f.name_correction(year_1953)
year_1953 = f.number_correction(year_1953)
year_1953 = f.check_total(year_1953)

mun_1953 = f.get_mun(year_1953)