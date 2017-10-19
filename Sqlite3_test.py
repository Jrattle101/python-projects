import sqlite3
connection=sqlite3.connect("test.db")

cursor=connection.cursor()

cursor.execute("""DROP TABLE person;""")

sql_command="""
CREATE TABLE person(
    id int PRIMARY KEY,
    fname varchar(20),
    lname varchar(30),
    gender char(1),
    birth_date DATE);"""

cursor.execute(sql_command)

sql_command="""Insert into person(id, fname, lname, gender, birth_date)
    VALUES (null, 'jason', 'adams', 'm', '1986-04-16');"""
cursor.execute(sql_command)


connection.commit()

connection.close()
