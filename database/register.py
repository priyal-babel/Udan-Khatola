import MySQLdb
from configure import user, password

con = MySQLdb.connect(host='localhost', user=user,
                      password=password, database="airline_reservation")
cursor = con.cursor()

command = 'CREATE DATABASE if not exists airline_reservation'
cursor.execute(command)

command = 'CREATE TABLE if not exists registration(firstname VARCHAR(10),lastname VARCHAR(10),phonenumber VARCHAR(15), emailid nvarchar(255), password varchar(20),gender int, age VARCHAR(3))'
cursor.execute(command)

command = '''CREATE TABLE if not exists booking(
                        firstname VARCHAR(10),
                        lastname VARCHAR(10),
                        phonenumber VARCHAR(15),
                        emailid nvarchar(255),
                        address varchar(200),
                        gender int,
                        age VARCHAR(3),
                        pnr varchar(6),
                        source varchar(20),
                        destination varchar(20),
                        date varchar(15),
                        time varchar(20),
                        airline_name varchar(20),
                        class varchar(20),
                        seat varchar(3))'''
cursor.execute(command)
