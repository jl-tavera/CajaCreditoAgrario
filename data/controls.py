import pandas as pd
import functions as fx

year_1952 = fx.loadCleanYearCSV('Final/Years/year_1952_codes.csv')
year_1962 = fx.loadCleanYearCSV('Final/Years/year_1962_codes.csv')
panel = fx.loadCleanYearCSV('Final/Panel/Panel.csv')
times = fx.loadCleanYearCSV('Final/Panel/times.csv')
controls = fx.loadControlsXLSX('Controls/controles.xlsx')
literacy = fx.loadLiteracyXLSX('Literacy/Literacy.xlsx')
education = fx.loadLiteracyXLSX('Education/cambio_educ.xlsx')


grouped = fx.loadGroupedCSV('Final/Grouped/Grouped.csv')
grouped = grouped.rename(columns= {'cod_mpio': 'codmpio'})
grouped = fx.intColumn(grouped, 'codmpio')

cod_1962 = fx.getNames(year_1962, 'Cod Mun')
cod_1952 = fx.getNames(year_1952, 'Cod Mun')

controls = fx.initialYear(controls, cod_1952, cod_1962)
controls = fx.intColumn(controls, 'codmpio')

merge = pd.merge(grouped, controls, on='codmpio', how='right')
merge = merge.drop('index_x', axis = 1)
merge = merge.fillna(0)
merge = fx.rearrange(merge, 'municipio', 1)
merge = fx.rearrange(merge, 'depto', 3)
merge = merge.drop('Anio', 1)
merge = merge.drop('Poblacion', 1)
merge = merge.drop('Cod Dep', 1)

literacy = pd.pivot_table(literacy, 
                index=['CodigoDANE'], 
                values = 'alfabetismo', 
                columns='Anio').reset_index()

literacy = literacy.rename(columns={'CodigoDANE': 'codmpio'})

merge2 = pd.merge(literacy, merge, on='codmpio', how='right')
merge2 = fx.rearrange(merge2, 1918 , 28)
merge2 = fx.rearrange(merge2, 1938 , 28)
merge2 = fx.rearrange(merge2, 1951 , 28)
merge2 = fx.rearrange(merge2, 1964 , 28)
merge2 = fx.rearrange(merge2, 1973 , 28)

merge3 = pd.merge(times, merge2, on='codmpio', how='right')
merge3 = merge3.drop('Unnamed: 0', axis = 1)
merge3 = fx.rearrange(merge3, 'numero_prestamos' , 29)
merge3 = merge3.fillna(0)
merge3 = fx.averagesFinal(merge3)
merge3 = merge3.fillna(0)

merge4 = pd.merge(education, merge3, on='codmpio', how='right')
merge4 = merge4.fillna(0)


fx.exportFinalCSV(merge4,'Regression/Final.csv')



