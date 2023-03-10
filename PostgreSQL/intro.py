# PostgreSQL - система управления базами данных(СУБД/DBMS)
# Это ряд программ и инструментов позволяющих создавать БД, управлять ею и сманилировать данными внутри БД(CRUD)

# Postgres - сама база данных, она реалицонная, то есть данные хранятся в виде таблиц и таблицы имеют связи между собой(relations)

# SQL(Structured Query Language) - декларативный язык структурированных запросов,
# он принимется для создания и управления данными

'-----------------------------------------------------------------------------------------------------'
# Типы полей в Postgres
# 1.Numeric  types:
#         a.smallint(2bytes) -> -32767 to 32767
        # b. integer(4 bytes) -> -214700 to 2147000
        # c. bigint(8 bytes) -> ...
        # d. serial (4bytes) -> auto-increment(integer, 1-2147000)
        # c. real(4 bytes) -  число с плавающей точкой, вещественное число 
        # f. double precision(8 bytes) - real но только с двойной точностью 
    
#2. Character types:
    # a. varchar(кол-во 255) - можем указать макс кол-во символов в ручную. Если мы не указали максимальное кол-во символов
    # в 50, а запомнили только 10, то остальные 40 не заполнятся
    # b. char(255) - если не заполним все символы то остальные заполнятся пробелами
    # c. text - неограниченное кол-во символов 

#3. Boolean types
    # boolean(1byte) -> True/False

#4. date - календарная дата(год. месяц. день)

# 5. location - координатная точка -> (245, -12)(x,y)





'-----------------------------------------------------------------------------------------------------'
# constrains(ограничения):
#     1. CHECK <column> > 5 - проверка данных по условию 
#     2. UNIQUE - только уникальные данные 
#     3. NOT NULL - обязательно к заполнению
#     4. DEFAULT - добавляет дефолтное значение 
#     5. Primary key(для установки идентификатора данных в таблице)
#     5. FOREIGN KEY (для установки связи между таблицами)

'----------------------------------------------------------------------------------------------------'

# Вход 
# mac: psql postgres
# psql -> для входа через своего юзера

# \q -> выход из СУБД

# \du -> список всех юзеров

# \l -> список всех баз данных

# \c <dbnname> -> команда для подключения к бд
        # \dt -> список таблиц в бд
        # \d <table name> подробная информация про таблицу

# ИМПОРТ данных при помощи файла
# psql -U <username> -d <database> -f <path_to_file> 

# CREATE DATABASE <dbname>; -> команда для создания бд 
# DROP ...-> удаление

# CREATE USER <username> WITH PASSWORD '<password>'; - команда для создания юзера

# ALTER USER <username> WITH SUPERUSER: команда для изменения статуса юзера на суперюзера

# SELECT <column> FROM <table>; команда для получения данных 

# WHERE: используется для филтрации по полям, будут выводиться только те данные которые соответствуют условию WHERE

# Синтаксис: SELECT <row> FROM <tablename> WHERE <row> = 'чему либо'

# SELECT * FROM products WHERE meat = 'Becon'
# SELECT * FROM products WHERE meat in  ('Becon', 'Beef');
'-----------------------------------------------------------------------------------------------------'


#WHERE: используется для филтрации по полям. будут выводиться только те данные которые соответствуют условию WHERE.

# Синтаксис: SELECT: <row> FROM <tablename> WHERE <row> = 'чему либо'

# SELECT * FROM products WHERE meat = 'Becon';
# SELECT * FROM products WHERE meat in ('Becon', 'Beef');

# and: оператор и, множества условий

# операторы сравнения: <,>,>=,<=,=,<>
# BETWEEN условия между
# Select * from products WHERE id BETWEEN 3 and 8;
# Select * from products WHERE id <= 8 and id >= 3;

#ORDER BT: сортировка по входящим данным по убыванию либо по возрастанию

    # ASC(ПО ВОЗРОСТАНИЮ) И DESC(ПО УБЫВАНИЮ)

# SELECT <row> FROM <table> ORDER BY <row> [ASC/DESC];

# LIMIT: позволяет нам вернуть данные в огранниченном количестве
# SELECT <row> FROM <table> LIMIT 1;


# LIKE: выводит результат который сообветсвует введеному шаблому зависит от регистра!!!!
# ILIKE: не зависит от регистра
# СИНТАКСИС: SELECT * FROM products WHERE name LIKE 'S%';


# DISTINCT: позволяет нам убрать дубликаты и возвращает только уникальные значения 

# SELET DISTINCT name FROM products;

'-----------------------------------------------------------------------------------------------------'

# DROP DATABASE <name_of_db>; удаление бд

# DROP TABLE <name_of_table>; удаление таблицы

# INSERT INTO <tablename> (<columns>) VALUES
#     (datas_to_columns); - команда для заполнения данных в таблицу

    # INSERT INTO cities (name, location)
    # VALUES('Biskek', '(42.52, 74.59')
# CREATE USER <username> WITH PASSWORD '<password>' 

# Обновить данные
# UPDATE <tablename> SET <row> = <new_value>
# WHERE <row> = <value>; - команда для обновления данных
# Указываем после WHERE то какой объект обновить

# DELETE FROM <tablename> WHERE <column> = <data>; - команда для удаления юзера

'Task 2'
# SELECT plaintext FROM wordform WHERE plaintext ILIKE 'a%';

'Task 4'
# SELECT AVG(totalparagraphs) FROM work WHERE genretype = 't';

'Task 5'
# SELECT title FROM work WHERE totalwords >=(SELECT AVG(totalwords) FROM work);

'Task 6'
# SELECT character.charname, speechcount, work.title FROM character LEFT JOIN character_work ON character.charid
#  = character_work.charid LEFT JOIN work ON character_work.workid = work.workid

'-----------------------------------------------------------------------------------------------------'

# Связи между таблицами(relations):
#     1. Один к одному(One-to-One) - человек паспорт
#     2. Один ко многим(One-to-Many) - человек и банковские карты
#     3. Много ко многим(Many-to-Many) - студенты и преподы

# JOIN - оператор, который позволяет в запросах SELECT брать данные из нескольких таблиц

# INNER JOIN() - достаются все записи, у которых есть связь

# FULL JOIN - достаются все записи с обеих таблиц

# LEFT JOIN - достает все записи с левой таблицы, а с правой только те записи у которых есть связь с левой таблицей

# RIGHT JOIN - достает все записи с правой таблицы, а с леовй только те записи у которых есть связь с правой таблицей

# * где 'левая' таблица эта та таблица которая записана до join, а 'правая' таблица это таблица которая записана после join
