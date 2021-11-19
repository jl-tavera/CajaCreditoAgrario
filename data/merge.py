import pandas as pd
import functions as fx

divipola = fx.loadDIVIPOLA('DIVIPOLA/DIVIPOLA.csv')
divipola = fx.nameDepID(divipola)

panel = fx.loadPanelCSV('Panel/panel.csv')

year_1952 = fx.loadCleanYearCSV('DANE/real/1952_r_clean.csv')
year_1952 = fx.nameDepYearID(year_1952)

compare = fx.compareDIVIPOLA(panel, divipola)
merge = fx.mergeDIVIPOLA(divipola, year_1952)

fx.exportYear(merge, '1952_p', 's')





