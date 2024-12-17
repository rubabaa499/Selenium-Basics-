import mysql.connector

con=mysql.connector.connect(host="localhost", port=3306, user="root", paswd="root123", database="mydb")
curs=con.cursor()
curs.execute("insert into student values('Labiba', 27)")
con.commit()
con.close()

print("Finished.....")