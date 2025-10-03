sql="""
create table if not exists departemnet (
    id bigserial primary key,
    departament_name varchar(100) not null,
    departament_id varchar(100) not null ); 
    
    
create table if not exists employees (
    id bigserial primary key,
    fullname varchar(50) not null,
    year date not null,
    departament_id varchar(100) not null references departement(departament_id) 
);


select e.fullname, d.departament_name from employees e join departement d on e.departament_id = d.departament_id;   
"""