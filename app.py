import pypyodbc as pyodbc
import psycopg2

# conx_str = "DRIVER={ODBC Driver 17 for SQL Server};SERVER=LAPTOP-P1OQJO0O\MSSQLSERVER03;DATABASE=MyNewDB;UID=vishnupadma;PWD=vishnusql"
# conx_str = "DRIVER={MySQL ODBC 8.0 ANSI Driver};SERVER=localhost;DATABASE=mydbone;UID=vistest;PWD=vispass"
conx_str = "DRIVER={PostgreSQL ANSI};SERVER=localhost;DATABASE=visdb;UID=vistuname;PWD=visps"

conx = pyodbc.connect(conx_str)  # Creating connection object

cursor = conx.cursor()  # Creating a cursor obj to to the operations

#conx_query = "select * from newemployee"
# conx_query = "select * from tabone"
conx_query = "select * from vistb"

cursor.execute(conx_query)
data = cursor.fetchall()
print(data)


print(pyodbc.drivers())


# conn = psycopg2.connect(
#     user='vistuname',
#     password='visps',
#     host='127.0.0.1',
#     port='5432',
#     database='visdb'
# )
# cursor = conn.cursor()
# cursor.execute('SELECT * FROM vistb')
# for row in cursor:
#     print(row)
# conn.close()






