import mysql.connector
import os
from tabulate import tabulate

config=mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='db_akademik-0549'

)

def nim():
    nim = input("Masukkan NIM : ")
    cursor = config.cursor()
    sql = "SELECT * FROM tbl_students_0549 WHERE nim=%s"
    val = (nim,)
    cursor.execute(sql,val)
    results = cursor.fetchone()
    print(results)

def limit():
    headers = ['no','nim','nama','jk','jurusan','alamat']
    limit = int(input("Masukkan Limit: "))
    cursor = config.cursor()
    sql = "SELECT * FROM tbl_students_0549 Limit %d"%(limit)
    cursor.execute(sql)
    results = cursor.fetchall()
    print(tabulate(results,headers=headers,tabletfmt="grid"))
    

def all_data():
    cursor = config.cursor()
    sql = "SELECT * FROM tbl_students_0549"
    cursor.execute(sql)
    results = cursor.fetchall()
    for data in results:
        print(data)
         
    
def menu():
    no =input('Pilih Menu> ')
    if no == '1':
        all_data()

    elif no == '2':
        limit()

    elif no == '3':
        nim()
        
if __name__=='__main__':
    while(True):
        menu()

        
    
