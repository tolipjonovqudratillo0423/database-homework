sql="""
create table users(
    id bigserial primary key,
    fullname varchar(50) not null,
    year date not null,
    group_id varchar(100) not null references groups(group_id) 
);
create table if not exists groups(
id bigserial primary key,
groups_name varchar(100) not null,
group_id varchar(100) not null

);




"""
isert_sql="""
INSERT INTO users (fullname, year, group_id) VALUES
('Say Pleven', '2004-02-19', 'G101'),
('Bronson Hackleton', '1996-11-20', 'G102'),
('Christabella Hannent', '1996-10-30', 'G103'),
('Zarla Varcoe', '1996-12-25', 'G104'),
('Odessa Chesshyre', '1997-02-28', 'G105'),
('Kyle Grzeszczak', '1997-03-03', 'G101'),
('Clo Bullingham', '2001-02-27', 'G102'),
('Gabrielle Craighead', '1994-02-11', 'G103'),
('Norry Macari', '2004-08-04', 'G104'),
('Eddy Edwardson', '2001-02-01', 'G105'),
('Juan Chesterfield', '1992-04-17', 'G101'),
('Bettina Theobalds', '2002-11-08', 'G102'),
('Ryley Mandeville', '2010-07-14', 'G103'),
('Vinita Hiddersley', '1991-12-19', 'G104'),
('Boone Theobald', '1995-05-21', 'G105');


INSERT INTO groups (groups_name, group_id) 
VALUES 
('Frontend Developers', 'G101'),
('Backend Developers', 'G102'),
('Cybersecurity Team', 'G103'),
('Data Science Enthusiasts', 'G104'),
('AI Researchers', 'G105');



"""


show_sql = """
select users.fullname ,users.year,groups.groups_name  from users join groups on users.group_id = groups.group_id; """

