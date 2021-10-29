#%%
import functions as f
import pandas as pd

'''
DATA PREPARATION
'''

'''
1952
'''

year_1952 = f.load_year('DANE/1952.csv')
year_1952 = f.name_correction(year_1952)
year_1952 = f.number_correction(year_1952)
year_1952 = f.check_total(year_1952)

mun_1952 = f.get_names(year_1952, 'Oficina')

f.export(year_1952, '1952_clean')

'''
1953
'''

year_1953 = f.load_year2('DANE/1953.xlsx')

year_1953 = f.number_correction(year_1953)
year_1953 = f.check_total(year_1953)

mun_1953 = f.get_names(year_1953, 'Oficina')
mun_1953 = f.format_name(mun_1953)

dep_1953 = f.get_names(year_1953, 'Departamento')
dep_1953 = f.format_name(dep_1953)

year_1953 = year_1953.drop('Oficina', 1)
year_1953 = year_1953.drop('Departamento', 1)

year_1953= f.assign(year_1953, 'Oficina', mun_1953)
year_1953= f.assign(year_1953, 'Departamento', dep_1953)

year_1953 = f.rearrange(year_1953, 'Oficina', 0)
year_1953 = f.rearrange(year_1953, 'Departamento', 1)

f.export(year_1953, '1953_clean')

'''
1954
'''

year_1954 = f.load_year('DANE/1954.csv')
year_1954 = f.name_correction(year_1954)
year_1954 = f.number_correction(year_1954)
year_1954 = f.check_total(year_1954)

mun_1954 = f.get_mun(year_1954)

'''
1955
'''

# year_1955 = f.load_year('DANE/1955.csv')
# year_1955 = f.name_correction(year_1955)
# year_1955 = f.number_correction(year_1955)
# year_1955 = f.check_total(year_1955)



