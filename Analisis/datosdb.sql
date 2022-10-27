use datosdb;

select * from precios
limit 10; #vemos los datos. 

#Este el query que haremos para ver si funciona.
select avg(pre.precio) as promedio_sucursal from sucursales as s 
join precios as pre on (s.id = pre.sucursal_id)
where s.id = '91688';

#creamos una tabla donde llevaremos registro de los triggers
drop table if exists fact_precios;
create table if not exists fact_precios(
	`usuario`  varchar(30),
    `fecha_modificacion` datetime
);
#El trigger es un disparador que usaremos para ver si efectivamente la carga incremental se realizo o no. 
create trigger fact_precios after insert on precios
for each row
insert into fact_precios(usuario,fecha_modificacion)
values(current_user(),now());

#El siguiente query lo usaremos para insertar/unir la tabla de precios con los nuevos precios.
insert into precios 
	select * from new_precios;
    
#vemos con este query la tabla de los registros sobre los triggers. 
select * from fact_precios;