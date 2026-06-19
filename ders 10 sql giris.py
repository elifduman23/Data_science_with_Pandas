import sqlite3
import os
def create_database():
    if os.path.exists("students.db"): #os.path  klasör yolu olur (her yerde düzgün çalışır) , kod students diye bir database var mı diye kontrol eder
        os.remove("students.db") # databaseyi siler

    conn=sqlite3.connect("students.db") # bağlantıyı kontrol eder
    cursor=conn.cursor() # bağlantıyı alıp gezinmeyi ve veri okuma veri değiştirme gibi işlemler yapmamızı sağlar
    return conn,cursor

def create_tables(cursor):
    cursor.execute('''
    CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    name VARCHAR NOT NULL,
    age INTEGER,
    email VARCHAR UNIQUE,
    city VARCHAR
    )
    ''')
    cursor.execute('''
       CREATE TABLE Courses (
       id INTEGER PRIMARY KEY,
       course_name VARCHAR NOT NULL,
       instructor TEXT,
       credits INTEGER
       )
       ''')
def insert_sample_data(cursor):
    students=[
        (1,"Elif Duman",21,"elif.duman@gmail.com","Elazığ")
        ,(2,"Yağmur Erdoğan",20,"yagmur.erdogan@gmail.com","Malatya")
        ,(3,"Sevcan Dizman",19,"sevcan.dizman@gmail.com","Tokat")
    ]

    cursor.executemany("INSERT INTO Students VALUES (?,?,?,?,?)",students) # birden fazla veri ekleyeceğimiz için executemany kullandık

    courses =[
        (1,"C# Programming","Ali Akdağ",5),
        (2,"Python Programming","Sinan Çetin",4),
        (3,"Data Scientists and Machine Learning","Atıl Samancıoğlu",4),
        (4,"Syber Security","Atıl Samancıoğlu",5)
    ]
    cursor.executemany("INSERT INTO Courses VALUES(?,?,?,?)",courses)
    print("Sample data inserted successfully")

def basic_all_operations(cursor):
    #SELECT ALL
    print("select all")
    cursor.execute("SELECT * FROM Students")
    records=cursor.fetchall()
    for row in records:
        #print(row)
        print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Email: {row[3]}, City: {row[4]}")

    #SELECT COLUMNS
    print("select columns")
    cursor.execute("SELECT name,age FROM Students")
    records =cursor.fetchall()
    print(records)
    # WHERE CLAUSE (FİLTRELEME YAPMAK)
    print("where clause")
    cursor.execute("SELECT * FROM Students WHERE age =21")
    records=cursor.fetchall()
    print(records)
    #WHERE WİTH STRİNG
    print("where with string")
    cursor.execute("SELECT * FROM Students WHERE City='Malatya'") # string den tek tırnak kullanılmalı yoksa hata verir
    records=cursor.fetchall()
    print(records)
    #ORDER BY AGE
    print("order by age") # aldığımız verileri(sonuçları) yaşa göre dizmek(sıralamak)
    cursor.execute("SELECT * FROM Students ORDER BY age")
    records=cursor.fetchall()
    for k in records:
        print(k)
    #LİMİT BY 2 # ilk 2 veriyi alır
    print("limit by 2")
    cursor.execute("SELECT * FROM Students LIMIT 2")
    records=cursor.fetchall()
    for i in records:
        print(i)
    print("LIKE ")
    print("ismi (E) harfi ile başlayanlar:")
    cursor.execute("SELECT * FROM Students WHERE name LIKE 'E%'")
    records=cursor.fetchall()
    print(records)
    print("ismi (n) harfi ile bitenler:")
    cursor.execute("SELECT * FROM Students WHERE name LIKE '%n'")
    records=cursor.fetchall()
    for k in records:
        print(k)
def sql_update_delete_insert_operations(cursor,conn):
    #İNSERT
    cursor.execute("INSERT INTO Students VALUES (4,'Merve Kahraman',21,'merve.kahraman@gmail.com','Elazığ')")
    conn.commit()
    #UPDATE
   # cursor.execute("UPDATE Students SET age =22 WHERE id=2") #id si 2olan verideki kişinin yaşını 22 olarak günceller
    #conn.commit()
    #DELETE
    cursor.execute("DELETE FROM Students WHERE id=4")
    conn.commit()
def aggregate_functions(cursor):
    #COUNT
    print("aggrate functions count")
    cursor.execute("SELECT COUNT(*) FROM Students")
    result=cursor.fetchall()
    print(result) #tuple olarak verir
    records=cursor.fetchone() # bir tane yazdırır
    print(records)
    print(result[0] [0])
    #AVERAGE
    print("average")
    cursor.execute("SELECT AVG(age) FROM Students")
    result=cursor.fetchone()
    print(result[0])
    #MAX-MIN
    print("max-min")
    cursor.execute("SELECT MAX(age),MIN(age) FROM Students")
    result=cursor.fetchall()
    print(result)
    #GROUP BY
    print("group by") #hangi şehirden kaç tane var,onu sayıyor
    cursor.execute("SELECT city, COUNT(*) FROM Students GROUP BY city")
    result=cursor.fetchall()
    print(result)

def cozum(cursor):
    print("çözüm:")
    print("***************")
    print("1) Bütün kursların bilgilerini getirin")
    cursor.execute("SELECT * FROM Students")
    print(cursor.fetchall())
    print("2) Sadece eğitmenlerin ismini ve ders ismi bilgilerini getirin")
    cursor.execute("SELECT course_name,instructor FROM Courses")
    records=cursor.fetchall()
    for k in records:
        print(k)
    print("3) Sadece 21 yaşındaki öğrencileri getirin")
    cursor.execute("SELECT * FROM Students WHERE age=21")
    print(cursor.fetchall())
    print("4) Sadece Chicago'da yaşayan öğrencileri getirin")
    cursor.execute("SELECT * FROM Students WHERE City='Tokat'")
    print(cursor.fetchall())
    print("5) Sadece 'Dr. Anderson' tarafından verilen dersleri getirin")
    cursor.execute("SELECT course_name FROM Courses WHERE instructor='Atıl Samancıoğlu'")
    records=cursor.fetchall()
    print("Atıl Samancıoğlu tarafından verilen kurslar:")
    for k in records:
        print(k)
    print("6) Sadece ismi 'A' ile başlayan öğrencileri getirin")
    cursor.execute("SELECT * FROM Students WHERE name LIKE 'E%'")
    print(cursor.fetchall())
    print("7) Sadece 3 ve üzeri kredi olan dersleri getirin")
    cursor.execute("SELECT * FROM Courses WHERE credits >=3")
    records=cursor.fetchall()
    for k in records:
        print(k)
    print("1) Öğrencileri alphabetic şekilde dizerek getirin")
    cursor.execute("SELECT * FROM Students ORDER BY name")
    records=cursor.fetchall()
    for k in records:
        print(f"Name: {k[1]}")
    print("2) 20 yaşından büyük öğrencileri, ismine göre sıralayarak getirin")
    cursor.execute("SELECT NAME FROM Students WHERE age>20 ORDER BY name ")
    records=cursor.fetchall()
    for k in records:
        print(k)
    print("3) Sadece 'New York' veya 'Chicago' da yaşayan öğrencileri getirin")
    cursor.execute("SELECT name FROM Students WHERE City IN ('Elazığ','Tokat')")
    records=cursor.fetchall()
    for k in records:
        print(k)
    print("4) Sadece 'New York' ta yaşamayan öğrencileri getirin")
    cursor.execute("SELECT name FROM Students WHERE City !='Elazığ'")
    records=cursor.fetchall()
    for k in records:
        print(k)
def main():
    conn,cursor=create_database()
    try:
        create_tables(cursor)
        insert_sample_data(cursor)
        basic_all_operations(cursor)
        sql_update_delete_insert_operations(cursor,conn)
        aggregate_functions(cursor)
        cozum(cursor)
        conn.commit() # cursor ın yani imlecin ysptığı işleri uygulamayı sağlar
    except sqlite3.Error as e:
        print(e) # e=exception yani hata mesajı
    finally:
        conn.close() # bu kısım mutlaka çalışır ve database bağlantısını kapatır bu kısım ı hep kullanmalıyız

if __name__=="__main__":
    main()
