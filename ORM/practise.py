import psycopg2

connection = psycopg2.connect(  # -> \c db_name
    database = 'db_practice',
    user = 'alibekkokumov',
    password = '',
    host = 'localhost',
    port = '5432'
)
print('Database successfully opened')

cursor = connection.cursor()

# cursor.execute(
#     '''CREATE TABLE company(
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(100) NOT NULL,
#     city VARCHAR(50) NOT NULL
#     )
#     '''
# )
# print('Table succesfully created')
# connection.commit()
# connection.close()

# cursor = connection.cursor()
# cursor.execute(
#     '''INSERT INTO company(name,city) VALUES('IBM', 'Los Angeles'), ('Apple', 'Cupertino'),('HP', 'New York')'''
# )
# connection.commit()
# print('Inserted successfully')
# connection.close()

# cursor.execute(
#     '''INSERT INTO company(name,city) VALUES ('Samsung','Seoul')'''
# )

# cursor.execute(
#      '''INSERT INTO company(name,city) VALUES ('Toyota','Tokyo')'''
# )
# connection.commit()
# print('Inserted successfully')
# connection.close()

cursor = connection.cursor()
cursor.execute(
    '''
    SELECT * FROM company
    '''
)
print(cursor.fetchall())