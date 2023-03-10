# ORM(Object-Relational Mapping) - технология программирования, благодаря которой 
# разработчики могут использовать язык программирования ждя взаимодействия с реляционной
# базой данных (PosgreSQL, MySQL, OracleDB). Вместо того чтобы писать сырые запросы на операторах
# SQL, вы будете писать код ООП на языке программирования. Это очень сильно ускоряет разработку
# приложения и бд, особенно на начальных этапах.

from peewee import PostgresqlDatabase

db = PostgresqlDatabase(
    database = 'orm_db',
    user = 'alibekkokumov',
    password = '1',
    host = 'localhost',
    port = 5432
    
)

# db.connect()