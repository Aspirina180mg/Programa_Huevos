create database huevos;
use huevos;
CREATE TABLE productos (
  id int not null auto_increment,
  nombre varchar(255) not null,
  valor int not null,
  PRIMARY KEY (id)
);
insert into productos (nombre, valor) 
values 
	('Gallina', '50'), 
	('Pato', '150'), 
  ('Codorniz', '50'), 
  ('Avestruz', '800');
create table despachos (
id int not null auto_increment,
rut varchar(255) not null,
nombre varchar (255) not null,
tipo int not null,
convenio int not null,
direccion varchar(255) not null,
cantidad int not null,
valor_unitario int not null,
valor_total int not null,
primary key (id),
foreign key(tipo) references productos(id)
);
select * from despachos;
insert into despachos (rut, nombre, tipo, convenio, direccion, cantidad, valor_unitario, valor_total) values (
'18992359-7', 'Misael García Torres', 1, 1, 'Cerro Santa Rosa 3515 Block 4 Departamento 404, Iquique', 100, 50, 50000);
