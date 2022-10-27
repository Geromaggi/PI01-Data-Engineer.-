#                                         SOY HENRY - PROYECTO INDIVIDUAL 01 - DATA ENGINEER 

![HenryLogo](https://d31uz8lwfmyn8g.cloudfront.net/Assets/logo-henry-white-lg.png)

# Introduccion
Bienvenidos! 
El proyecto que contiene este repositorio consiste en un proceso de ETL (extract, transform and load) a partir de un conjunto de datasets dados. 
Para la realizacion de este proyecto se utilizaron las siguientes _herramientas_:

_ Python (Pandas, SQLalchemy,entre otras)

_ MySQL

_ Jupyter Notebooks

Ademas, se muestran las siguientes _habilidades_:

_ Analisis de los datos. 

_ Toma de Decisiones sobre los datos

_ ETL 

A continuacion veremos cada instancia del proceso ETL:

![image](https://user-images.githubusercontent.com/93155829/198329380-2c1cd3b2-a560-48a2-b7b0-0108a5421261.png)

# Extraccion

Los datasets fueron brindados por el equipo de SoyHenry por medio de un repositorio de github. Se trataban de diferentes extensiones (.csv, .parquet, .json, .xlsx). Estos estan presentes en la carpeta llamada Datasets de este mismo repositorio. Una de las decisiones tomadas sobre esto, fue llevar todos los datasets a un unico formato (.csv) para mejor trabajo. 

En esta instancia es necesario tener criterios. Entre ellos, criterios de actualizacion, completitud, fiabilidad, accesibilidad, etc. Al ser dados por el equipo de SoyHenry, no nos vamos a detener en analizar estos criterios, porque sabemos que los datos son fiables y estan listos para la siguiente instancia.

# Transformacion

La fase de transformación de un proceso ETL aplica una serie de reglas de negocio o funciones, sobre los datos extraídos para convertirlos en datos que serán cargados. Esta fase requiere tiempo, paciencia y un analisis abarcativo y a la vez meticuloso de los datos. Como resultado de este analisis, se ha llegado a la conclusion que algunos datasets requerian de diferentes transformaciones. Las principales decisiones que se tomaron fueron:

- Normalizar los datos. Esto quiere decir llevarlos al mismo formato y tipo.
- Limpiar los valores nulos. Para esto fue llevado a cabo un indicador, en el cual observamos el porcentaje total de valores nulos de cada columna del dataframe. Si este porcentaje era mayor que 1%, los valores nulos se eliminaba. Sino quedaban a considerador del programador. 
- Deteccion de Outliers. No se han encontrado outliers.

Estas decisiones, estan mejor justificadas y explicadas en los respectivos archivos. (script de pyhton o jupyter notebook)

Todo este paso ha sido realizado a traves de Python, utilizando en la mayoria de las veces la liberia pandas, util para el manejo de dataframes. 


# Carga

Una vez completada la transformacion de los datos, el ultimo paso que debemos realizar para terminar nuestro proceso ETL es la carga. La base de datos que usaremos va a ser MySQL (Workbench). Esto proceso lo realizamos usando la libreria SQLalchemy de Python, que nos logro conectar nuestro dataframes ya limpios a MySQL. 

En MySQL tan solo probaremos que nuestra base de datos funcione correctamente ejecutando un query especifico. Ademas se muestra un proceso de carga incremental de un archivo, y esto se puede ver con un indicador (trigger) que creamos.  


# Conclusion

Agradezco a todos! Aqui les dejo el diagrama de flujo de trabajo del ETL realizado para el proyecto 1 de data engineer.



![image](https://user-images.githubusercontent.com/93155829/198322033-17cac59d-c662-477e-87d1-a22cfbb35301.png)
