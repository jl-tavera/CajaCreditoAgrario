#%%
import functions as fx
'''
DATA PREPARATION
'''

'''
1952
'''

# year_1952 = fx.loadYearCSV('DANE/1952.csv')

# year_1952 = fx.nameCorrection(year_1952)
# year_1952 = fx.numberCorrection(year_1952)
# year_1952 = fx.checkTotal(year_1952)

# mun_1952 = fx.getNames(year_1952, 'Oficina')

# fx.export(year_1952, '1952_clean')

'''
1953
'''

# year_1953 = fx.loadYearXLSX('DANE/1953.xlsx')

# year_1953 = fx.numberCorrection(year_1953)
# year_1953 = fx.checkTotal(year_1953)

# mun_1953 = fx.getNames(year_1953, 'Oficina')
# mun_1953 = fx.formatName(mun_1953)

# dep_1953 = fx.getNames(year_1953, 'Departamento')
# dep_1953 = fx.formatName(dep_1953)

# year_1953 = year_1953.drop('Oficina', 1)
# year_1953 = year_1953.drop('Departamento', 1)

# year_1953 = fx.assign(year_1953, 'Oficina', mun_1953)
# year_1953 = fx.assign(year_1953, 'Departamento', dep_1953)

# year_1953 = fx.rearrange(year_1953, 'Oficina', 0)
# year_1953 = fx.rearrange(year_1953, 'Departamento', 1)

# fx.export(year_1953, '1953_clean')

'''
1954
'''

# year_1954 = fx.loadYearCSV('DANE/1954.csv')

# year_1954 = fx.nameCorrection(year_1954)
# year_1954 = fx.numberCorrection(year_1954)
# year_1954 = fx.checkTotal(year_1954)

# mun_1954 = fx.getNames(year_1954, 'Oficina')

# fx.export(year_1954, '1954_clean')

'''
1955
'''

# year_1955 = fx.loadYearCSV('DANE/1955.csv')

# year_1955 = fx.nameCorrection(year_1955)
# year_1955 = fx.numberCorrection(year_1955)
# year_1955 = fx.checkTotal(year_1955)

# mun_1955 = fx.getNames(year_1955, 'Oficina')

# fx.export(year_1955, '1955_clean')

'''
1956
'''

# year_1956 = fx.loadYearCSV('DANE/1956.csv')

# year_1956 = fx.nameCorrection(year_1956)
# year_1956 = fx.numberCorrection(year_1956)
# year_1956 = fx.checkTotal(year_1956)

# mun_1956 = fx.getNames(year_1956, 'Oficina')

# fx.export(year_1956, '1956_clean')

'''
1957
'''

# year_1957 = fx.loadYearCSV('DANE/1957.csv')

# year_1957 = fx.nameCorrection(year_1957)
# year_1957 = fx.numberCorrection(year_1957)
# year_1957 = fx.checkTotal(year_1957)

# mun_1957 = fx.getNames(year_1957, 'Oficina')

# fx.export(year_1957, '1957_clean')

'''
1958
'''

# year_1958 = fx.loadYearXLSX('DANE/1958.xlsx')

# year_1958 = fx.numberCorrection(year_1958)
# year_1958 = fx.checkTotalLP(year_1958)

# mun_1958 = fx.getNames(year_1958, 'Oficina')
# mun_1958 = fx.formatName(mun_1958)

# dep_1958 = fx.getNames(year_1958, 'Departamento')
# dep_1958 = fx.formatName(dep_1958)

# year_1958 = year_1958.drop('Oficina', 1)
# year_1958 = year_1958.drop('Departamento', 1)

# year_1958 = fx.assign(year_1958, 'Oficina', mun_1958)
# year_1958 = fx.assign(year_1958, 'Departamento', dep_1958)

# year_1958 = fx.rearrange(year_1958, 'Oficina', 0)
# year_1958 = fx.rearrange(year_1958, 'Departamento', 1)

# fx.export(year_1958, '1958_clean')

'''
1959
'''

year_1959 = fx.loadYearXLSX('DANE/1959.xlsx')

year_1959 = fx.numberCorrection(year_1959)
year_1959 = fx.checkTotalLP(year_1959)

mun_1959 = fx.getNames(year_1959, 'Oficina')
mun_1959 = fx.formatName(mun_1959)

dep_1959 = fx.getNames(year_1959, 'Departamento')
dep_1959 = fx.formatName(dep_1959)

year_1959 = year_1959.drop('Oficina', 1)
year_1959 = year_1959.drop('Departamento', 1)

year_1959 = fx.assign(year_1959, 'Oficina', mun_1959)
year_1959 = fx.assign(year_1959, 'Departamento', dep_1959)

year_1959 = fx.rearrange(year_1959, 'Oficina', 0)
year_1959 = fx.rearrange(year_1959, 'Departamento', 1)


#    (_    /_\    _)
#    / `'--) (--'` \
#   /  _,-'\_/'-,_  \
#  /.-'     "     '-.\
