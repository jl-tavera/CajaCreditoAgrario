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
# year_1952 = fx.createNewCol(year_1952, 'LP - Numero', 0, 6)
# year_1952 = fx.createNewCol(year_1952, 'LP - Valor', 0, 7)
# year_1952 = fx.createNewCol(year_1952, 'Anio', 1952, 2)
# year_1952 = year_1952.drop('Check - Valor', 1)
# year_1952 = year_1952.drop('Check - Numero', 1)

# mun_1952 = fx.getNames(year_1952, 'Oficina')

# fx.exportYear(year_1952, '1952_i_clean', 'i')

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

# year_1953 = fx.createNewCol(year_1953, 'LP - Numero', 0, 6)
# year_1953 = fx.createNewCol(year_1953, 'LP - Valor', 0, 7)
# year_1953 = fx.createNewCol(year_1953, 'Anio', 1953, 2)

# year_1953 = year_1953.drop('Check - Valor', 1)
# year_1953 = year_1953.drop('Check - Numero', 1)

# fx.exportYear(year_1953, '1953_i_clean', 'i')

'''
1954
'''

# year_1954 = fx.loadYearCSV('DANE/1954.csv')

# year_1954 = fx.nameCorrection(year_1954)
# year_1954 = fx.numberCorrection(year_1954)
# year_1954 = fx.checkTotal(year_1954)
# year_1954 = fx.createNewCol(year_1954, 'LP - Numero', 0, 6)
# year_1954 = fx.createNewCol(year_1954, 'LP - Valor', 0, 7)
# year_1954 = fx.createNewCol(year_1954, 'Anio', 1954, 2)
# year_1954 = year_1954.drop('Check - Valor', 1)
# year_1954 = year_1954.drop('Check - Numero', 1)

# mun_1954 = fx.getNames(year_1954, 'Oficina')

# fx.exportYear(year_1954, '1954_i_clean', 'i')

'''
1955
'''

# year_1955 = fx.loadYearCSV('DANE/1955.csv')

# year_1955 = fx.nameCorrection(year_1955)
# year_1955 = fx.numberCorrection(year_1955)
# year_1955 = fx.checkTotal(year_1955)
# year_1955 = fx.createNewCol(year_1955, 'LP - Numero', 0, 6)
# year_1955 = fx.createNewCol(year_1955, 'LP - Valor', 0, 7)
# year_1954 = fx.createNewCol(year_1955, 'Anio', 1955, 2)
# year_1955 = year_1955.drop('Check - Valor', 1)
# year_1955 = year_1955.drop('Check - Numero', 1)

# mun_1955 = fx.getNames(year_1955, 'Oficina')

# fx.exportYear(year_1955, '1955_i_clean', 'i')

'''
1956
'''

# year_1956 = fx.loadYearCSV('DANE/1956.csv')

# year_1956 = fx.nameCorrection(year_1956)
# year_1956 = fx.numberCorrection(year_1956)
# year_1956 = fx.checkTotal(year_1956)
# year_1956 = fx.createNewCol(year_1956, 'LP - Numero', 0, 6)
# year_1956 = fx.createNewCol(year_1956, 'LP - Valor', 0, 7)
# year_1956 = fx.createNewCol(year_1956, 'Anio', 1956, 2)
# year_1956 = year_1956.drop('Check - Valor', 1)
# year_1956 = year_1956.drop('Check - Numero', 1)

# mun_1956 = fx.getNames(year_1956, 'Oficina')

# fx.exportYear(year_1956, '1956_i_clean', 'i')

'''
1957
'''

# year_1957 = fx.loadYearCSV('DANE/1957.csv')

# year_1957 = fx.nameCorrection(year_1957)
# year_1957 = fx.numberCorrection(year_1957)
# year_1957 = fx.checkTotal(year_1957)
# year_1957 = fx.createNewCol(year_1957, 'LP - Numero', 0, 6)
# year_1957 = fx.createNewCol(year_1957, 'LP - Valor', 0, 7)
# year_1957 = fx.createNewCol(year_1957, 'Anio', 1957, 2)
# year_1957 = year_1957.drop('Check - Valor', 1)
# year_1957 = year_1957.drop('Check - Numero', 1)

# mun_1957 = fx.getNames(year_1957, 'Oficina')

# fx.exportYear(year_1957, '1957_i_clean', 'i')

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
# year_1958 = fx.createNewCol(year_1958, 'Anio', 1958, 2)

# year_1958 = year_1958.drop('Check - Valor', 1)
# year_1958 = year_1958.drop('Check - Numero', 1)

# fx.exportYear(year_1958, '1958_i_clean', 'i')

'''
1959
'''

# year_1959 = fx.loadYearXLSX('DANE/1959.xlsx')

# year_1959 = fx.numberCorrection(year_1959)
# year_1959 = fx.checkTotalLP(year_1959)

# mun_1959 = fx.getNames(year_1959, 'Oficina')
# mun_1959 = fx.formatName(mun_1959)

# dep_1959 = fx.getNames(year_1959, 'Departamento')
# dep_1959 = fx.formatName(dep_1959)

# year_1959 = year_1959.drop('Oficina', 1)
# year_1959 = year_1959.drop('Departamento', 1)

# year_1959 = fx.assign(year_1959, 'Oficina', mun_1959)
# year_1959 = fx.assign(year_1959, 'Departamento', dep_1959)

# year_1959 = fx.rearrange(year_1959, 'Oficina', 0)
# year_1959 = fx.rearrange(year_1959, 'Departamento', 1)
# year_1959 = fx.createNewCol(year_1959, 'Anio', 1959, 2)

# year_1959 = year_1959.drop('Check - Valor', 1)
# year_1959 = year_1959.drop('Check - Numero', 1)

# fx.exportYear(year_1959, '1959_i_clean', 'i')

'''
1960
'''

# year_1960 = fx.loadYearXLSX('DANE/1960.xlsx')
# year_1960 = fx.numberCorrection(year_1960)
# year_1960 = fx.checkTotalLP(year_1960)

# mun_1960 = fx.getNames(year_1960, 'Oficina')
# mun_1960 = fx.formatName(mun_1960)

# dep_1960 = fx.getNames(year_1960, 'Departamento')
# dep_1960 = fx.formatName(dep_1960)

# year_1960 = year_1960.drop('Oficina', 1)
# year_1960 = year_1960.drop('Departamento', 1)

# year_1960 = fx.assign(year_1960, 'Oficina', mun_1960)
# year_1960 = fx.assign(year_1960, 'Departamento', dep_1960)

# year_1960 = fx.rearrange(year_1960, 'Oficina', 0)
# year_1960 = fx.rearrange(year_1960, 'Departamento', 1)
# year_1960 = fx.createNewCol(year_1960, 'Anio', 1960, 2)

# year_1960 = year_1960.drop('Check - Valor', 1)
# year_1960 = year_1960.drop('Check - Numero', 1)

# fx.exportYear(year_1960, '1960_i_clean', 'i')


'''
1961
'''

# year_1961 = fx.loadYearXLSX('DANE/1961.xlsx')
# year_1961 = fx.numberCorrection(year_1961)
# year_1961 = fx.checkTotalLP(year_1961)

# mun_1961 = fx.getNames(year_1961, 'Oficina')
# mun_1961 = fx.formatName(mun_1961)

# dep_1961 = fx.getNames(year_1961, 'Departamento')
# dep_1961 = fx.formatName(dep_1961)

# year_1961 = year_1961.drop('Oficina', 1)
# year_1961 = year_1961.drop('Departamento', 1)

# year_1961 = fx.assign(year_1961, 'Oficina', mun_1961)
# year_1961 = fx.assign(year_1961, 'Departamento', dep_1961)

# year_1961 = fx.rearrange(year_1961, 'Oficina', 0)
# year_1961 = fx.rearrange(year_1961, 'Departamento', 1)
# year_1961 = fx.createNewCol(year_1961, 'Anio', 1961, 2)

# year_1961 = year_1961.drop('Check - Valor', 1)
# year_1961 = year_1961.drop('Check - Numero', 1)

# fx.exportYear(year_1961, '1961_i_clean', 'i')

'''
1962
'''

year_1962 = fx.loadYearCSV('DANE/1962.csv')

year_1962 = fx.nameCorrection(year_1962)
year_1962 = fx.numberCorrection(year_1962)
year_1962 = fx.checkTotal(year_1962)

fx.exportYear(year_1962, '1962_i_clean', 'i')

#    (_    /_\    _)
#    / `'--) (--'` \
#   /  _,-'\_/'-,_  \
#  /.-'     "     '-.\
