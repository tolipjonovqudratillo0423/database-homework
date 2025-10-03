sql="""
create table users(
    id bigserial primary key,
    fullname varchar(50) not null,
    year date not null,
    group_id varchar(100) not null
);



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

#RESULT 

# postgres=# select * from users; 
#  id |       fullname       |    year    | group_id 
# ----+----------------------+------------+----------
#   1 | Say Pleven           | 2004-02-19 | IB4805
#   2 | Bronson Hackleton    | 1996-11-20 | LH5700
#   3 | Christabella Hannent | 1996-10-30 | CX5049
#   4 | Zarla Varcoe         | 1996-12-25 | DL2657
#   5 | Odessa Chesshyre     | 1997-02-28 | UA6595
#   6 | Kyle Grzeszczak      | 1997-03-03 | WN1044
#   7 | Clo Bullingham       | 2001-02-27 | TG5846
#   8 | Gabrielle Craighead  | 1994-02-11 | WN3368
#   9 | Norry Macari         | 2004-08-04 | CX5398
#  10 | Eddy Edwardson       | 2001-02-01 | SQ1946
#  11 | Juan Chesterfield    | 1992-04-17 | AF1768
#  12 | Bettina Theobalds    | 2002-11-08 | AV4922
#  13 | Ryley Mandeville     | 2010-07-14 | SA9580
#  14 | Vinita Hiddersley    | 1991-12-19 | KE9708
#  15 | Boone Theobald       | 1995-05-21 | AV6698
# (15 строк)

# postgres=# select * from users where year > '01.01.2000'; 
#  id |     fullname      |    year    | group_id 
# ----+-------------------+------------+----------
#   1 | Say Pleven        | 2004-02-19 | IB4805
#   7 | Clo Bullingham    | 2001-02-27 | TG5846
#   9 | Norry Macari      | 2004-08-04 | CX5398
#  10 | Eddy Edwardson    | 2001-02-01 | SQ1946
#  12 | Bettina Theobalds | 2002-11-08 | AV4922
#  13 | Ryley Mandeville  | 2010-07-14 | SA9580
# (6 строк)

# postgres=# 
