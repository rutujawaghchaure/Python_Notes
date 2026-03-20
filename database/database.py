import mysql.connector
from openpyxli import Workbook
from openpyxl.styles import Alignment,Font,Border,Side
wb=Workbook()
ws=wb.active



conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db_mydatabase"
)
cursor=conn.cursor()
# id=int(input("enter id:"))
name=input("enter name:")
age=int(input("enter age:"))
city=input("enter city:")

def student_data(name,age,city):
    sql="INSERT INTO students(name,age,city) VALUES(%s,%s,%s)"
    values=(name,age,city)
    cursor.execute(sql,values)
    conn.commit()
    print("Data inserted successfully")
student_data(name,age,city)






