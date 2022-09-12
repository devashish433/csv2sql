import csv
import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", password='', database='movieList')
print("database connector")


cursor = mydb.cursor()
csv_data = csv.reader(open("main2.csv"))

for row in csv_data:
    cursor.execute("INSERT INTO movies (MovieCode.Period.Crores.actor.STATUS) VALUES(%s,%s,%s,%s,%s)", row)
    print(row)

mydb.commit()
cursor.close()
print("DONE")