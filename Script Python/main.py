import pandas as pd
from sql import *
from ETL_functions import *
#importamos las librerias necesarias. 

#crearemos funciones de carga incremental que nos hagan un proceso de etl sobre nuestro dataframe que sera el parametro de la funcion. Y luego 
#gracias a que importamos nuestro script de la carga hacia nuestra base de datos mysql, moveremos nuestro dataframe asi alli. 
def carga_incremental(file_path):
    file = pd.read_csv(f'{file_path}',delimiter='|') #leemos y transformamos en un archivo .csv
    
    file.drop_duplicates(inplace=True)#tiramos los duplicados
    file.drop(file[file.sucursal_id.isnull() == True].index, inplace=True) #dropeamos los nulos en id_sucursal
    file.precio.fillna(0.0, inplace=True)#rellenamos con cero los campos de la columna precio que son nulos. 
    for i in range(1,3):
        file.iloc[:,i] = file.iloc[:,i].astype('string') #transformamos a string. 

    file.to_sql('new_precios', con = conexion, if_exists='append', index=False)



def carga_incremental2 (file_path):
    file = pd.read_csv(f'{file_path}')
    file = etl_precios(file)

    file.to_sql('new_precios', con=conexion, index=False)

carga_incremental('/home/gero/Documentos/HENRY/LAB I/Proyecto 1 DE/Dataset carga incremental/precios_test_carga_incremental.txt')
