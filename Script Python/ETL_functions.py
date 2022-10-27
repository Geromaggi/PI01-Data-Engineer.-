import pandas as pd 
import sqlalchemy as db

# ETL PARA LA TABLA PRODUCTOS
def etl_productos(dataframe):
    dataframe.drop(columns=['categoria1','categoria2','categoria3'],inplace=True)
    # eliminamos las columnas de las categorias. No son necesarias
    dataframe['nombre'] = dataframe['nombre'].str.split(r"\s\d*\s", expand=False).str[0].str.upper()
    #Normalizamos la columna poniendola toda en mayusculas y eliminar las cantidades. 
    dataframe['id'] = dataframe['id'].str.replace('-', '').astype(int)
    # tanto para esta tabla como para el resto, normalizaremos la columna id. 
    return dataframe

#ETL para la tabla sucursal

def elt_sucursal(dataframe):
    try:
        dataframe['id'] = dataframe['id'].str.replace('-', '').astype(int)
    except:
        print('id ya esta limpio')
        pass

    #verificamos si la columa id ya esta limpia y sino la normalizamos como hicimos con la tabla productos. 

    dataframe['banderaDescripcion'] = dataframe['banderaDescripcion'].str.upper()
    dataframe['comercioRazonSocial'] = dataframe['comercioRazonSocial'].str.upper()
    dataframe['localidad'] = dataframe['localidad'].str.upper()
    dataframe['direccion'] = dataframe['direccion'].str.upper()
    
    #todas las columnas en mayuscula. 
    return dataframe

#ETL para precios.
#esta funcion la usaremos para todos los datasets que tengan precios. 

def etl_precios (dataframe):
    columns = ['precio','sucursal_id','producto_id']
    
    #estableceremos un filtro, un indicador para ver si es conveniente o no dropear los valores nulos.
    null_values = dataframe.isna().sum().div(dataframe.shape[0]).mul(100).round()
    null_values.tolist()
    #esto nos devolvera una lista del porcentaje de valores nulos de cada columna. 

    #si los valores nulos <1% entonces dropeamos. 
    for i in null_values:
        if i < 1:
            dataframe.dropna(inplace=True)

    #limpiemos cada columna:
    #sucursal_id
    try:
        dataframe['sucursal_id'] = dataframe['sucursal_id'].str.replace('-', '').astype(int)
    except:
        print('sucursal_id ya esta limpio')
        pass

    #producto_id
    try:
        dataframe['producto_id'] = dataframe['producto_id'].str.replace('-', '').astype(int)
    except:
        print('producto_id ya esta limpio')
        pass

    #precio
    dataframe['precio'] = dataframe['precio'].apply(pd.to_numeric)

    return dataframe[columns]


