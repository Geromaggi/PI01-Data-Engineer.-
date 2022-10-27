import pandas as pd
import sqlalchemy as db
#este script lo usaremos para la conexion a nuestra base de datos mysql.
#Para ellos definiremos las variables necesarias.
database_username='root' 
database_password='GeroMaggi10!' 
database_ip='localhost'
database_name='datosdb' 
#Aqui abajo vemos los comandos correspondientes para realizar dicha conexion. 
database_conection=db.create_engine(f'mysql+pymysql://{database_username}:{database_password}@{database_ip}/{database_name}')
conexion=database_conection.connect()
metadata=db.MetaData()