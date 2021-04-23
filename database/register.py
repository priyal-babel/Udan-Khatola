import MySQLdb
from configure import user, password

con = MySQLdb.connect(host='localhost', user=user,
                      password=password, database = "airline_reservation")
cursor = con.cursor()

# command = 'CREATE DATABASE airline_reservation'
# cursor.execute(command)