table_sql = """
create table if not exists books(
    id bigserial primary key,
    title varchar(100) not null,
    Author: varchar(100) not null)
    
)"""
change_name_sql = """
alter table books rename column title to book_title""" 