import MySQLdb
from configure import user, password

con = MySQLdb.connect(host='localhost', user=user,
                      password=password, database = "airline_reservation")
cursor = con.cursor()

# command = 'CREATE DATABASE airline_reservation'
# cursor.execute(command)

# command = 'CREATE TABLE registration(firstname VARCHAR(10),lastname VARCHAR(10),phonenumber VARCHAR(15), emailid nvarchar(255), password varchar(20),gender int, age VARCHAR(3))'
# cursor.execute(command)

# command = 'CREATE TABLE booking(firstname VARCHAR(10),lastname VARCHAR(10),phonenumber VARCHAR(15), emailid nvarchar(255), address varchar(200),gender int, age VARCHAR(3))'
# cursor.execute(command)

# command = "ALTER TABLE booking ADD pnr varchar(6);"
# cursor.execute(command)
