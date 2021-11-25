
import functions as fx
import pandas as pd 

'''
LOAD YEARS
'''

year_1952 = fx.loadCleanYearCSV('Final/Years/year_1952_codes.csv')
year_1953 = fx.loadCleanYearCSV('Final/Years/year_1953_codes.csv')
year_1954 = fx.loadCleanYearCSV('Final/Years/year_1954_codes.csv')
year_1955 = fx.loadCleanYearCSV('Final/Years/year_1955_codes.csv')
year_1956 = fx.loadCleanYearCSV('Final/Years/year_1956_codes.csv')
year_1957 = fx.loadCleanYearCSV('Final/Years/year_1957_codes.csv')
year_1958 = fx.loadCleanYearCSV('Final/Years/year_1958_codes.csv')
year_1959 = fx.loadCleanYearCSV('Final/Years/year_1959_codes.csv')
year_1960 = fx.loadCleanYearCSV('Final/Years/year_1960_codes.csv')
year_1962 = fx.loadCleanYearCSV('Final/Years/year_1962_codes.csv')

population = fx.loadPopulationXLSX('Population/Poblacion.xlsx')

'''
NORMALIZE POPULATION
'''

norm_1952 = fx.normalizePopulation(year_1952, population, 1952)
norm_1953 = fx.normalizePopulation(year_1953, population, 1953)
norm_1954 = fx.normalizePopulation(year_1954, population, 1954)
norm_1955 = fx.normalizePopulation(year_1955, population, 1955)
norm_1956 = fx.normalizePopulation(year_1956, population, 1956)
norm_1957 = fx.normalizePopulation(year_1957, population, 1957)
norm_1958 = fx.normalizePopulation(year_1958, population, 1958)
norm_1959 = fx.normalizePopulation(year_1959, population, 1959)
norm_1960 = fx.normalizePopulation(year_1960, population, 1960)
norm_1962 = fx.normalizePopulation(year_1962, population, 1962)

'''
MERGE PANEL 
'''

merge_1 = fx.mergeYearsCodes(norm_1952, norm_1953)
merge_2 = fx.mergeYearsCodes(merge_1, norm_1954)
merge_3 = fx.mergeYearsCodes(merge_2, norm_1955)
merge_4 = fx.mergeYearsCodes(merge_3, norm_1956)
merge_5 = fx.mergeYearsCodes(merge_4, norm_1957)
merge_6 = fx.mergeYearsCodes(merge_5, norm_1958)
merge_7 = fx.mergeYearsCodes(merge_6, norm_1959)
merge_8 = fx.mergeYearsCodes(merge_7, norm_1960)
merge_9 = fx.mergeYearsCodes(merge_8, norm_1962)

'''
GROUPED DATA
'''

grouped = merge_9.groupby(['cod_mpio']).sum()

'''
EXPORT FILES
'''

fx.exportFinalCSV(norm_1952, 'Population/1952')
fx.exportFinalCSV(norm_1953, 'Population/1953')
fx.exportFinalCSV(norm_1954, 'Population/1954')
fx.exportFinalCSV(norm_1955, 'Population/1955')
fx.exportFinalCSV(norm_1956, 'Population/1956')
fx.exportFinalCSV(norm_1957, 'Population/1957')
fx.exportFinalCSV(norm_1958, 'Population/1958')
fx.exportFinalCSV(norm_1959, 'Population/1959')
fx.exportFinalCSV(norm_1960, 'Population/1960')
fx.exportFinalCSV(norm_1962, 'Population/1962')
fx.exportFinalCSV(merge_9, 'Panel/Panel')
fx.exportFinalCSV(grouped, 'Grouped/Grouped')
