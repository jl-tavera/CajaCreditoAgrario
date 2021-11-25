import functions as fx
import pandas as pd 

'''
LOAD YEARS
'''

year_1952 = fx.loadCleanYearCSV('Final/Years/year_1952_codes.csv')
population = fx.loadPopulationXLSX('Population/Poblacion.xlsx')

norm_1952 = fx.normalizePopulation(year_1952, population, 1952)

fx.exportCodeYearsCSV(norm_1952, 'year_1952_pop')