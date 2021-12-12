import functions as fx
import pandas as pd


mdm = fx.loadIpcXLSX('MDM/MDM.xlsx')
base = fx.loadYearCSV('Corte/cortetransversal.csv')

base = fx.intColumn(base, 'codmpio')

mdm = fx.formatColumnZero(mdm)
mdm = fx.intColumn(mdm, 'Código Entidad')
mdm = mdm.rename(columns={'Código Entidad': 'codmpio'})
mdm = mdm[mdm.Año.isin([2018])]

merge = pd.merge(mdm, base, how='inner', on='codmpio')
fx.exportFinalCSV(merge, 'MDM/mdm')
