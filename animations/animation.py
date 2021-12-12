import pandas as pd
import geopandas as gpd
import config as cf
import matplotlib as plt

'''
LOADING FUNCTIONS
'''

def loadGEOJSON(path):
    route = cf.data_dir.replace('/animations', '') + path
    map = gpd.read_file(route)

    return map

def loadPanel(path): 
    route = cf.data_dir.replace('/App', '') + path
    panel = pd.read_excel(route)

    return panel

def loadCodesCSV(path): 
    route = cf.export_dir.replace('/animations', '') + path
    year = pd.read_csv(route)

    return year

def loadStatsCSV(path): 
    route = cf.export_dir.replace('/animations', '') + 'DANE/stats/' + path
    stats = pd.read_csv(route)

    return stats


'''
DATA FUNCTIONS
'''
def fillNA(df): 
    df = df.fillna(0)
    return df

def intColumn(df, column): 
    df[column] = df[column].astype(int)

    return df

def sumRows(df): 
    df2 = df.agg(df.agg(['sum']))

    return df2

def neighborsMap(gdf): 

    gdf["Vecinos"] = None  

    for index, mpio in gdf.iterrows():   

        neighbors = gdf[~gdf.geometry.disjoint(mpio.geometry)].ID_ESPACIA.tolist()
        neighbors = [ id_espacia for id_espacia in neighbors if mpio.ID_ESPACIA != id_espacia ]
        gdf.at[index, "Vecinos"] = ", ".join(neighbors)
    
    gdf =gdf.rename(columns = {'ID_ESPACIA': 'codmpio'})
    gdf = gdf.loc[:, ['codmpio', 'Vecinos']] 
    
    return gdf
    '''
PIVOT CODES
'''

def pivotStats(df, var): 
    df = pd.pivot_table(
            df,
            values = var, 
            index=['Cod Mun'], 
            columns = 'Anio').reset_index()
    df = df.rename({'Cod Mun': 'ID_ESPACIA'}, axis='columns')
    df['ID_ESPACIA'] = df['ID_ESPACIA'].astype(int)

    return df

def pivotDepStats(df, var): 
    df = pd.pivot_table(
            df,
            values = var, 
            index=['Anio'], 
            columns = 'Departamento').reset_index()


    return df

'''
EXPORT FUNCTIONS
'''

def exportPanelXLSX(df, name):
    route = cf.export_dir.replace('/animations', '') 
    df.to_excel(route + str(name) + '.xlsx')

    return None

def titleMap(df, year, min, max): 
    fig = df.plot(column=year, 
                        cmap='Greens', 
                        figsize=(8,8), 
                        linewidth=0.8, 
                        edgecolor='0.8', 
                        vmin= min, 
                        vmax= max, 
                       legend=True, 
                       norm= plt.colors.Normalize(vmin= min, vmax=max))

    fig.axis('off')
    fig.annotate(year,
            xy=(0.1, .225), 
            xycoords='figure fraction',
            horizontalalignment='left', 
            verticalalignment='top',
            fontsize=36,
            weight = 'bold')

    chart = fig.get_figure()
    chart.suptitle("Número de Prestamos por Municipio", 
                fontsize =  25,
                weight = 'bold')

    path = 'output/Maps/Animation/' + str(year)
    chart.savefig( path, dpi=300)

    pass

def titleMap2(df, year, min, max): 
    fig = df.plot(column=year, 
                        cmap='Greens', 
                        figsize=(8,8), 
                        linewidth=0.8, 
                        edgecolor='0.8', 
                        vmin= min, 
                        vmax= max, 
                       legend=True, 
                       norm= plt.colors.Normalize(vmin= min, vmax=max))

    fig.axis('off')
    fig.annotate(year,
            xy=(0.1, .225), 
            xycoords='figure fraction',
            horizontalalignment='left', 
            verticalalignment='top',
            fontsize=36,
            weight = 'bold')

    chart = fig.get_figure()
    chart.suptitle("Valor de Prestamos por Municipio", 
                fontsize =  25,
                weight = 'bold')

    path = 'output/Maps/Animation2/' + str(year)
    chart.savefig( path, dpi=300)

    pass

def untitledMap(df, year, min, max): 
    fig = df.plot(column=year, 
                        cmap='Greens', 
                        figsize=(8,8), 
                        linewidth=0.8, 
                        edgecolor='0.8', 
                        vmin= min, 
                        vmax= max, 
                       legend=True, 
                       norm= plt.colors.Normalize(vmin= min, vmax=max))

    fig.axis('off')
    fig.annotate(year,
            xy=(0.1, .225), 
            xycoords='figure fraction',
            horizontalalignment='left', 
            verticalalignment='top',
            fontsize=36,
            weight = 'bold')

    chart = fig.get_figure()
    path = 'output/Maps/Subplot/' + str(year)
    chart.savefig( path, dpi=300)

    pass

