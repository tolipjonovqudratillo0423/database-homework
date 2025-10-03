sql="""
create table users(
    id bigserial primary key,
    fullname varchar(50) not null,
    year date not null,
    group_id varchar(100) references groups.group_id not null
);
create table if not exists groups(
id bigserial 

)





"""
insert_sql = """
insert into users (id, fullname, year, group_id) values (1, 'Say Pleven', '19.02.2004', 'IB4805');
insert into users (id, fullname, year, group_id) values (2, 'Bronson Hackleton', '20.11.1996', 'LH5700');
insert into users (id, fullname, year, group_id) values (3, 'Christabella Hannent', '30.10.1996', 'CX5049');
insert into users (id, fullname, year, group_id) values (4, 'Zarla Varcoe', '25.12.1996', 'DL2657');
insert into users (id, fullname, year, group_id) values (5, 'Odessa Chesshyre', '28.02.1997', 'UA6595');
insert into users (id, fullname, year, group_id) values (6, 'Kyle Grzeszczak', '03.03.1997', 'WN1044');
insert into users (id, fullname, year, group_id) values (7, 'Clo Bullingham', '27.02.2001', 'TG5846');
insert into users (id, fullname, year, group_id) values (8, 'Gabrielle Craighead', '11.02.1994', 'WN3368');
insert into users (id, fullname, year, group_id) values (9, 'Norry Macari', '04.08.2004', 'CX5398');
insert into users (id, fullname, year, group_id) values (10, 'Eddy Edwardson', '01.02.2001', 'SQ1946');
insert into users (id, fullname, year, group_id) values (11, 'Juan Chesterfield', '17.04.1992', 'AF1768');
insert into users (id, fullname, year, group_id) values (12, 'Bettina Theobalds', '08.11.2002', 'AV4922');
insert into users (id, fullname, year, group_id) values (13, 'Ryley Mandeville', '14.07.2010', 'SA9580');
insert into users (id, fullname, year, group_id) values (14, 'Vinita Hiddersley', '19.12.1991', 'KE9708');
insert into users (id, fullname, year, group_id) values (15, 'Boone Theobald', '21.05.1995', 'AV6698');
"""

show_sql = """
select * from user where year>'01.01.2000'; """

