import functions as fx
import pandas as pd


alf2018 = fx.loadLiteracyXLSX('Literacy/alf2018.xlsx')
base = fx.loadYearCSV('Corte/cortetransversal.csv')

base = fx.intColumn(base, 'codmpio')

alf2018 = fx.formatColumnZero(alf2018)
alf2018 = fx.intColumn(alf2018, 'Código Entidad')

alf2018 = alf2018[alf2018.Año.isin([2018])]
alf2018 = alf2018.rename(columns={'Código Entidad': 'codmpio', 'Dato Numérico':'alf_A2018'})
alf2018 = alf2018[['codmpio','alf_A2018']]
alf2018 = fx.format_2018(alf2018)

merge = pd.merge(alf2018, base, how='inner', on='codmpio')
fx.rearrange(merge, 'alf_A2018', 16)
fx.exportFinalCSV(merge, '2018/alf2018')
